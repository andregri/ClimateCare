# Starting from
# https://www.mongodb.com/developer/quickstart/python-quickstart-crud/

import json
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pprint import pprint

def main():
    # Load config from a .env file:
    load_dotenv()

    # Load json file
    POWER_PLANT_DATASET = os.environ['GPPDB_PATH'] + '.json'
    with open(POWER_PLANT_DATASET) as jsonf:
        power_plants = json.load(jsonf)

        pprint(power_plants[0])

        # Connect to your MongoDB cluster:
        # MONGODB_URI = os.environ['MONGODB_URI']
        # client = MongoClient(MONGODB_URI)

        # Insert the first element
        # climate_db = client['climate']
        # collection = climate_db['power_plants']

        # insert_result = collection.insert_one(power_plants[0])
        # print(insert_result)

if __name__ == "__main__":
    main()