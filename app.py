from flask import Flask, render_template
import datetime   # This will be needed later
import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load config from a .env file:
load_dotenv()

# Connect to your MongoDB cluster:
MONGODB_URI = os.environ['MONGODB_URI']
client = MongoClient(MONGODB_URI)

# List all the databases in the cluster:
for db_info in client.list_database_names():
   print(db_info)

#app = Flask(__name__)
#
#@app.route('/')
#def index():
#    return render_template('index.html')