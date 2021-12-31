"""
 - A small API for managing cocktail recipes.
"""

import os
from dotenv import load_dotenv
from flask.templating import render_template

from pymongo.collection import Collection, ReturnDocument

from flask import Flask, request, url_for, jsonify
from flask_pymongo import PyMongo
from pymongo.errors import DuplicateKeyError

#from model import PowerPlant
#from objectid import PydanticObjectId

# Configure Flask & Flask-PyMongo:
load_dotenv()
app = Flask(__name__)
app.config["MONGO_URI"] = os.environ["MONGODB_URI"]
pymongo = PyMongo(app)

# Get a reference to the recipes collection.
# Uses a type-hint, so that your IDE knows what's happening!
power_plants: Collection = pymongo.db.power_plants


@app.errorhandler(404)
def resource_not_found(e):
    """
    An error-handler to ensure that 404 errors are returned as JSON.
    """
    return jsonify(error=str(e)), 404


@app.route('/')
def index():
   return render_template('/index.html')


def get_plant_bycountry(country: str):
   result = power_plants.aggregate([
      {
         '$search': {
            'index': 'default',
            'text': {
               'query': country,
               'path': 'country_long'
            }
         }
      },
      {
         '$limit': 5
      },
      {
         '$project': {
            '_id': 0,
            'country_long': 1,
            'name': 1
         }
      }
   ])
   return result


def get_fuels(country):
   """
   Accumulate capacities for each fuel type for a given country
   """
   result = power_plants.aggregate([
      {
         # Search country
         '$search': {
            'index': 'default',
            'text': {
               'query': country,
               'path': 'country_long'
            }
         }
      },
      {
         # Accumulate capacity by fuel type
         '$group':
         {
            '_id': '$primary_fuel',
            'totCapacity': {
               '$sum': {'$toDecimal': '$capacity_mw'}
            }
         }
      }
   ])
   return result


@app.route('/<string:country>', methods=["GET"])
def search(country):
   fuels = get_fuels(country)
   result = [f for f in fuels]
   return render_template('/fuels.html', country=country, result=result)
