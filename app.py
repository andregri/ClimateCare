"""
 - A small API for managing cocktail recipes.
"""

import os
from dotenv import load_dotenv

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
recipes: Collection = pymongo.db.power_plants


@app.errorhandler(404)
def resource_not_found(e):
    """
    An error-handler to ensure that 404 errors are returned as JSON.
    """
    return jsonify(error=str(e)), 404

#
#@app.route("/cocktails/")
#def list_cocktails():
#    """
#    GET a list of cocktail recipes.
#
#    The results are paginated using the `page` parameter.
#    """
#
#    page = int(request.args.get("page", 1))
#    per_page = 10  # A const value.
#
#    # For pagination, it's necessary to sort by name,
#    # then skip the number of docs that earlier pages would have displayed,
#    # and then to limit to the fixed page size, ``per_page``.
#    cursor = recipes.find().sort("name").skip(per_page * (page - 1)).limit(per_page)
#
#    cocktail_count = recipes.count_documents({})
#
#    links = {
#        "self": {"href": url_for(".list_cocktails", page=page, _external=True)},
#        "last": {
#            "href": url_for(
#                ".list_cocktails", page=(cocktail_count // per_page) + 1, _external=True
#            )
#        },
#    }
#    # Add a 'prev' link if it's not on the first page:
#    if page > 1:
#        links["prev"] = {
#            "href": url_for(".list_cocktails", page=page - 1, _external=True)
#        }
#    # Add a 'next' link if it's not on the last page:
#    if page - 1 < cocktail_count // per_page:
#        links["next"] = {
#            "href": url_for(".list_cocktails", page=page + 1, _external=True)
#        }
#
#    return {
#        "recipes": [Cocktail(**doc).to_json() for doc in cursor],
#        "_links": links,
#    }
#