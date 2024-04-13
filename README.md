# poke-berries-api

API that performs statistical analysis of some berries.

## Motivation

This is a technical test presented to Globant.

## Test description

### Goal

Create a Poke-berries statistics API.

### General rules

- Commit your changes to a public repository in GitHub.
- Add a README.md with instructions to run the code.
- Support the following endpoints:
  - GET /allBerryStats

    - Response:
      ```json
      {
          "berries_names": [...],
          "min_growth_time": "", // time, int
          "median_growth_time": "", // time, float
          "max_growth_time": "", // time, int
          "variance_growth_time": "", // time, float
          "mean_growth_time": "", // time, float
          "frequency_growth_time": "", // time, {growth_time: frequency, ...}
      }
      ```
    This endpoint should consume an external API to get the proper info, here
    is the documentation page: https://pokeapi.co/docs/v2#berries

- The data must be human-readable.
- Use environment variables for configuration.
- The response must include the content-type header (application/json)
- Functions must be tested with pytest.

### Extra points

- Upload and deploy the solution to a free cloud service for example PythonEverywhere.
- Use a containering system like docker
- Use a Python library (example: Matplotlib) to create a Histogram graph and display the image in a plain html.
- Keep a cache of 2 minutes of the data. You can use a persistent layer for this.

## Running the API

first install pyenv
install virtualenv
create a 3.11.1 virtualenv
pip install -r requirements.txt
create a .env file with

  POKE_API_URL="https://pokeapi.co/api/v2/berry"
  REDIS_HOST="redis://localhost"

python main.py
