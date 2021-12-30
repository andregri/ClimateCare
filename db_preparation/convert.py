# This is code is developed started from
# https://www.geeksforgeeks.org/convert-csv-to-json-using-python/

import csv
import json
import os
from dotenv import load_dotenv

# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):
     
    # create a dictionary
    data = {}
     
    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
         
        # Convert each row into a dictionary
        # and add it to data
        for id, rows in enumerate(csvReader):
            data[id] = rows
 
    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


def main():
    # Load config from a .env file:
    load_dotenv()

    path = os.environ['GPPDB_PATH']
    csvFilePath = path + '.csv'
    jsonFilePath = path + '.json'
    
    # Call the make_json function
    make_json(csvFilePath, jsonFilePath)


if __name__ == "__main__":
    main()