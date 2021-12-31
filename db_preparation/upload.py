# Starting from
# https://www.mongodb.com/developer/quickstart/python-quickstart-crud/

import json
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pprint import pprint
import argparse

def upload(mongo_uri, json_path, db, collection):
    """Upload the JSON dataset to MongoDB"""
    with open(json_path) as jsonf:
        # Load json dataset
        power_plants = json.load(jsonf)

        # Connect to your MongoDB cluster:
        client = MongoClient(mongo_uri)

        # Load dataset to db
        climate_db = client[db]
        collection = climate_db[collection]

        #insert_result = collection.insert_one(power_plants[0])
        insert_result = collection.insert_many(power_plants)
        print(insert_result.inserted_ids)


def main():
    # Parse command args
    parser = argparse.ArgumentParser(description='Upload json dataset to MongoDB')
    parser.add_argument('cloud', action='store_false',
                        help='upload to MongoDB Atlas')
    args = parser.parse_args()

    # Load config from a .env file:
    load_dotenv()

    # Select MongoDB local or cloud
    if args.cloud:
        print('Upload to cloud')
        mongodb_uri = os.environ['MONGODB_URI']
    else:
        print('Upload locally')
        mongodb_uri = 'mongodb://localhost:27017'

    # Load json file
    dataset_path = os.environ['GPPDB_PATH'] + '.json'
    upload(mongodb_uri, dataset_path, 'climate', 'power_plants')


if __name__ == "__main__":
    main()