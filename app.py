import os
from dotenv import load_dotenv
from flask.templating import render_template

from pymongo.collection import Collection

from flask import Flask
from flask_pymongo import PyMongo

import db

#from model import PowerPlant
#from objectid import PydanticObjectId

def create_app(test_config=None):
   # Configure Flask & Flask-PyMongo:
   load_dotenv()
   app = Flask(__name__, instance_relative_config=True)
   app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY=os.environ["SECRET_KEY"],
        # MongoDB uri
        MONGO_URI=os.environ["MONGODB_URI"],
   )

   pymongo = PyMongo(app)

   # Get a reference to the recipes collection.
   # Uses a type-hint, so that your IDE knows what's happening!
   power_plants: Collection = pymongo.db.power_plants


   @app.errorhandler(404)
   def resource_not_found(e):
      """
      An error-handler to ensure that 404 errors are returned as JSON.
      """
      return render_template('404.html')


   @app.route('/')
   def index():
      return render_template('/index.html')


   @app.route('/credits')
   def credits():
      return render_template('credits.html')


   @app.route('/contact')
   def contact():
      return render_template('contact.html')


   @app.route('/country/<string:country>', methods=["GET"])
   def search(country):
      fuels = db.get_fuels(power_plants, country)
      result = [f for f in fuels]
      title = country.upper()
      return render_template('/search.html', search_title=title, result=result)


   @app.route('/fuel/<string:fuel>', methods=['GET'])
   def search_top_five(fuel):
      countries = db.top_five_byfuel(power_plants, fuel)
      result = [f for f in countries]
      title = 'TOP 5 ' + fuel.upper() + ' ENERGY PRODUCERS'
      return render_template('/search.html', search_title=title, result=result)

   return app