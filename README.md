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

## Testing

To test the functions that do all the internal logic, just run in the terminal:

```bash
pytest -v
```

## Running the API locally

To run the API locally, it is necessary to have a virtual environment already created with python `3.11.1`. You can use `venv` or `pyenv`. I personally use `pyenv` and the instructions to install it and create a virtual environment are [here](https://akrabat.com/creating-virtual-environments-with-pyenv/)

Once the virtual environment is created with the right python version, simply run in the terminal:

```bash
pip install -r requirements.txt
```
_Note: This may take a while depending on your internet connection and your machine._

After the installation of all necessary dependencies, you will need to create a `.env` file in the root of the project. This is where some variables needed by the application itself are defined.

In order for this specific use case to work, the `.env` file, should look like this:

```.env
POKE_API_URL="https://pokeapi.co/api/v2/berry"
REDIS_HOST="redis://localhost"
```

Now we are ready to run the API locally. Just run in the terminal:

```bash
python main.py
```

Now you can go to your preferred browser and open http://0.0.0.0:8000/berries/allBerryStats and the response should look like this:

```JSON
{
  "berries_names": [
    "cheri",
    "chesto",
    "pecha",
    ...
    "custap",
    "jaboca",
    "rowap"
  ],
  "min_growth_time": 2,
  "median_growth_time": 15,
  "max_growth_time": 24,
  "variance_growth_time": 62.47197420634921,
  "mean_growth_time": 12.859375,
  "frequency_growth_time": {
    "2": 5,
    "3": 5,
    "4": 3,
    "5": 5,
    "6": 4,
    "8": 7,
    "12": 1,
    "15": 5,
    "18": 17,
    "24": 12
  }
}
```

_Note: If you are using MacOS and Safari, sometimes because of firewall configurarion, the previous address won't work. Please use this one instead http://127.0.0.1:8000/berries/allBerryStats_

## Extra points

### Containerization

Docker was used to containerize the application. See [Dockerfile](Dockerfile). The containerization was made so that the image would work in AWS Lambda environment.

### CI/CD

A Github Actions workflow was created so that a docker image is created, and then push into an AWS ECR repository and later update the Lambda to deploy it with the latest version of the image.

### Histogram

To access the Histogram requested, please use the endpoint `/berries/allBerryStatsHistogram`.

### Cache

An instance of Redis was used for this. Locally works just fine with the instructions seen before. However in the AWS Lambda service there is an issue described later on.

### Running the API on the Cloud

This API has been also deployed to a AWS Lambda function and it is accesible [here](https://6m4gqhpckefhwxaxoufl5cprxi0wqkhu.lambda-url.us-east-2.on.aws/). Please note that because it is using a Lambda, probably it will take a few seconds to start the first time it is called.

#### _Side note_

The implementation in AWS Lambda is working partially. There's an issue when using Redis from ElastiCache and I haven't been able to detect it. Maybe someone that knows more AWS can spot the issue. However, the service is up and running and you can check the Swagger documentation going [here](https://6m4gqhpckefhwxaxoufl5cprxi0wqkhu.lambda-url.us-east-2.on.aws/docs).
