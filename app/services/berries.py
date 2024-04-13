import os
import asyncio
from statistics import median, variance, mean
from collections import Counter

import requests
import httpx

from app.libs.core.logger import get_logger
from app.schemas.berries import BerriesStats


Logger = get_logger(__name__)

class BerriesService():

    url = os.getenv("POKE_API_URL")

    @classmethod
    async def _get_all_data(cls) -> list[dict]:
        """
        This function calls the PokeAPI asynchronously to get the information
        of every available berry
        """

        # Make a call to PokeAPI to berry's root endpoint
        response_count = requests.get(cls.url)
        Logger.info(f'Response code of PokeAPI: {response_count.status_code}')

        # Get the count of available berries from previous response
        number_of_berries = response_count.json()['count']
        Logger.info(f'Number of berries found: {number_of_berries}')

        # Make asynchronous calls to the PokeAPI assuming that the berries' ids
        # are continuous from 1 to `number_of_berries`
        async with httpx.AsyncClient() as client:
            tasks = [
                client.get(f'{cls.url}/{str(i)}')
                for i in range(1, number_of_berries + 1) # Here's the assumption made
            ]
            responses = await asyncio.gather(*tasks)
            return [response.json() for response in responses]

    @classmethod
    def _get_all_names(cls, berries_data: list[dict]) -> list[str]:
        """
        Generates a list of berries names
        """

        return [berry['name'] for berry in berries_data]

    @classmethod
    def _calculate_stats(cls, berries_data: list[dict]) -> dict:
        """
        This function calculates stats from all available berries
        """

        # Get a list of only `growth_time` attribute of all berries
        growth_times = [berry['growth_time'] for berry in berries_data]

        # Build stats
        stats = {
            'min_growth_time': min(growth_times),
            'median_growth_time': median(growth_times),
            'max_growth_time': max(growth_times),
            'variance_growth_time': variance(growth_times),
            'mean_growth_time': mean(growth_times),
            'frequency_growth_time': dict(Counter(growth_times))
        }

        return stats

    @classmethod
    async def get_stats(cls):
        """
        Generates statistics of available berries in the PokeAPI
        """

        Logger.info('Fetching not cached info from PokeAPI')

        # Call PokeAPI asynchronously to get necessary berries data
        berries_data = await cls._get_all_data()

        # Start building response object
        results = {
            # Get names using fetched data from the PokeAPI
            'berries_names': cls._get_all_names(berries_data)
        }

        # Calculate stats using fetched data from the PokeAPI
        stats = cls._calculate_stats(berries_data)

        # Add stats to response object
        results.update(stats)

        # Converts the response object into pydantic model for type validations
        berries_stats = BerriesStats.model_validate(results)

        return berries_stats
