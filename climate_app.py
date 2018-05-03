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
    return(
        f"This is the Hawaii Climate Analysis App"
        f"Avalable Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start/end"
    )

# Query for the dates and temps from last year
# Convert query results to a dictionary using date as the key and tobs as the value
# Return the json of dict

# Return a json list of stations from dataset
@app.route("/api/v1.0/stations")
    def  results = session.query(Station.stations).all()
    # Unravel results into an array
    stations = list(np.ravel(results))
    return jsonify(stations)

# Return a json list of tobs for the previous year
@app.route("api/v1.0/tobs")
    def  results = session.query(Measurement.tobs).all()
    # Unravel results into an array
    stations = list(np.ravel(results))
    return jsonify(tobs)

# Return a json list of the min temp, avg temp, and max temp for given start-end range
@app.route("/api/v1.0/temp/start/end")
    def results = session.query
# When given the start only, calculate 'TMIN', 'TAVG', and 'TMAX' for all dates greater than and equal to the start date
# When given the start and end date, calculate above for dates between the start and end date inclusive

if __name__ == "__main__":
    app.run(debug=True)