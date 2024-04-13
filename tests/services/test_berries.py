import pytest

from statistics import median, variance, mean
from collections import Counter

from app.services.berries import BerriesService

@pytest.mark.asyncio
async def test__get_all_data():
    """
    Test that the response is not empty
    """

    data = await BerriesService._get_all_data()
    assert len(data) > 0

def test__get_all_names():
    """
    Test integrity of names list
    """

    test_data = [
        {
            'name': 'berry0',
            'other_key': 'other_value'
        },
        {
            'name': 'berry1',
            'other_key': 'other_value'
        },
        {
            'name': 'berry2',
            'other_key': 'other_value'
        },
    ]

    names = BerriesService._get_all_names(test_data)

    # Test that all names were extracted entirely
    assert len(test_data) == len(names)

    # Test that the names were extracted correctly
    assert names == ['berry0', 'berry1', 'berry2']

def test__calculate_stats():
    """
    Test integrity of statistics
    """

    test_data = [
        {
            'name': 'berry0',
            'growth_time': 1
        },
        {
            'name': 'berry1',
            'growth_time': 3
        },
        {
            'name': 'berry2',
            'growth_time': 5
        },
    ]

    growth_times = [berry['growth_time'] for berry in test_data]

    stats = BerriesService._calculate_stats(test_data)

    assert (
        stats['min_growth_time'] == min(growth_times) and
        isinstance(stats['min_growth_time'], int)
    )
    assert (
        stats['median_growth_time'] == median(growth_times) and
        isinstance(stats['median_growth_time'], float | int)
    )
    assert (
        stats['max_growth_time'] == max(growth_times) and
        isinstance(stats['max_growth_time'], int)
    )
    assert (
        stats['variance_growth_time'] == variance(growth_times) and
        isinstance(stats['variance_growth_time'], float | int)
    )
    assert (
        stats['mean_growth_time'] == mean(growth_times) and
        isinstance(stats['mean_growth_time'], float | int)
    )
    assert (
        stats['frequency_growth_time'] == dict(Counter(growth_times)) and
        isinstance(stats['frequency_growth_time'], dict)
    )

@pytest.mark.asyncio
async def test_get_stats():
    """
    Test completeness of response
    """

    keys = (
        'berries_names',
        'min_growth_time',
        'median_growth_time',
        'max_growth_time',
        'variance_growth_time',
        'mean_growth_time',
        'frequency_growth_time'
    )

    berries_stats = await BerriesService.get_stats()
    assert all(key in berries_stats.model_dump() for key in keys)
