import json

file_path = "data/russian-cities.json"


def match_exact(cityName: str):
    with open(file_path, 'r') as file:
        cities = json.load(file)
    result = [city for city in cities if city['name'].lower() ==
              cityName.lower()]
    # print(result)
    return result
