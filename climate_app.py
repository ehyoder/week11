### Step 4 - Climate App

# Import flask
from flask import flask

# Create app
app = Flask(__name__)

# Define what to do when the user hits the index route
@app.route("/")
def home():
    print("test")
    return "string"

# Query for the dates and temps from last year
# Convert query results to a dictionary using date as the key and tobs as the value
# Return the json of dict
# Return a json list of stations from dataset
# Return a json list of tobs for the previous year
# Return a json list of the min temp, avg temp, and max temp for given start-end range
# When given the start only, calculate 'TMIN', 'TAVG', and 'TMAX' for all dates greater than and equal to the start date
# When given the start and end date, calculate above for dates between the start and end date inclusive

# Jsonify - convert api data into a valid json response object