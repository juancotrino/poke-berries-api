info = {
    'title': 'PokeBerryAPI',

    'version': '0.1.0',

    'description': """
## Introduction
This API performs statistical calulation of numerical data of available berries in [this API](https://pokeapi.co/docs/v2#berries)

## Content
This API only supoorts the endpoint `GET berries/allBerryStats` which should output a JSON like this:

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

    """,

    'contact':{
        'name': 'Juan Cotrino',
        'url':'https://github.com/juancotrino',
        'email': 'juan.cotrino@outlook.com'
        },

    'tags_metadata': [
        {
        "name": "Berries",
        "description": "Berries routes"
        },
    ]
}
