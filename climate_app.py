### Step 4 - Climate App

# Import flask
from flask import flask, jsonify
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Create app
app = Flask(__name__)

# Define what to do when the user hits the index route
@app.route("/")
def home():
    print("This is the Hawaii Climate Analysis App")
    return jsonify

# Query for the dates and temps from last year
# Convert query results to a dictionary using date as the key and tobs as the value
# Return the json of dict

# Return a json list of stations from dataset
@app.route("list of stations")

# Return a json list of tobs for the previous year
@app.route("list of tobs")

# Return a json list of the min temp, avg temp, and max temp for given start-end range
@app.route("tmin, tavg, tmax")
# When given the start only, calculate 'TMIN', 'TAVG', and 'TMAX' for all dates greater than and equal to the start date
# When given the start and end date, calculate above for dates between the start and end date inclusive
