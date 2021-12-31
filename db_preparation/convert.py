# This is code is developed started from
# https://www.geeksforgeeks.org/convert-csv-to-json-using-python/

import csv
import json
import os
from dotenv import load_dotenv
import pycountry_convert as pc

CONTINENTS = {
    'AQ': 'Antarctica',
    'NA': 'North America',
    'SA': 'South America', 
    'AS': 'Asia',
    'OC': 'Australia',
    'AF': 'Africa',
    'EU': 'Europe'
}

# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath, predicate):
     
    # create a dictionary
    data = {}
     
    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
         
        # Convert each row into a dictionary
        # and add it to data
        data = [predicate(row) for row in csvReader]
 
    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


def add_continent(data):
    # https://stackoverflow.com/questions/55910004/get-continent-name-from-country-using-pycountry
    country_alpha3 = data['country']
    
    # Convert country to country code
    """try:
        country_code = pc.country_name_to_country_alpha2(country, cn_name_format="default")
    except KeyError:
        if country == 'Cote DIvoire':
            country = 'Ivory Coast'
            data['country_long'] = country
        else:
            pass"""
    
    # Convert country code to continent code
    try:
        country_alpha2 = pc.country_alpha3_to_country_alpha2(country_alpha3)
        continent_code = pc.country_alpha2_to_continent_code(country_alpha2)

    except KeyError:
        if country_alpha3 == 'ATA': # Antarctica
            continent_code = 'AQ'
        elif country_alpha3 == 'KOS': # Kosovo
            continent_code = 'EU'
        elif country_alpha3 == 'ESH': # Western Sahara
            continent_code = 'AF'
        else:
            print(data['country_long'], data['country'])
            raise

    data['continent'] = CONTINENTS[continent_code]
    return data


def main():
    # Load config from a .env file:
    load_dotenv()

    path = os.environ['GPPDB_PATH']
    csvFilePath = path + '.csv'
    jsonFilePath = path + '.json'
    
    # Call the make_json function
    make_json(csvFilePath, jsonFilePath, add_continent)


if __name__ == "__main__":
    main()