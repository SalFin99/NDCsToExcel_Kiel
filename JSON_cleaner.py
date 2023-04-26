import json

def cleanJSON():
    # Load the JSON data
    with open('climate_targets.json') as f:
        data = json.load(f)

    for country in data:
        country_dict=data[country]

        del country_dict['country_name']
        del country_dict['region_id']
        del country_dict['region_name']

    return data
