
#CTa-HW09-Surf's Up
#Part 04 - Climate App

import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Create an engine for the hawaii.sqlite database
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to the measurement and station tables
Measurement = Base.classes.measurement
Station = Base.classes.station


# Create our session (link) from Python to the DB
session = Session(engine)


# Flask Setup

app = Flask(__name__)

# set up object for Flask for future references


# route takes you to certain endpoints in the URL. where data can be accessed.

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Avalable Routes:<br/><br/>"
		
        f"/api/v1.0/precipitation"
		f" - Precipitation query<br/><br/>"
		

        f"/api/v1.0/stations"
        f" - List of stations<br/><br/>"
		

        f"/api/v1.0/tobs"
        f" - List of Temperature Observations (tobs)<br/><br/>"
		

        f"/api/v1.0/<start>"
        f" - Enter Start Date<br/><br/>"
		

        f"/api/v1.0/<start>/<end>"
        f" - Enter Start and End Date<br/><br/>"
		
    )


@app.route("/api/v1.0/precipitation")
def precip():
    #Return a list of all precipitation
    results = session.query(measurement.date, measurement.prcp).\
	filter(measurement.date.between('2016-08-23','2017-08-23')).all()

    # Convert list of tuples into normal list
    
    precip_list = list(np.ravel(results))

    return jsonify(precip_list)


@app.route("/api/v1.0/stations")
def station():
    #Return a list stations
    results = session.query(station.station,station.name).all()

    station_list = list(np.ravel(results))

    return jsonify(station_list)
	
@app.route("/api/v1.0/tobs")
def tobs():
    #Return a list tobs
    results = session.query(measurement.date, measurement.prcp).\
	filter(measurement.date.between('2016-08-23','2017-08-23')).all()

    # Convert list of tuples into normal list
    
    tobs_list = list(np.ravel(results))

    return jsonify(tobs_list)


@app.route("/api/v1.0/<start>")
def start(start='2016-08-23'):

	#start defaults to 1 year range
	
	results = session.query(func.min(measurement.tobs),func.max(measurement.tobs),func.avg(measurement.tobs)).filter(measurement.date.between(start,'2017-08-23')).all()

	# Convert list of tuples into normal list
	sdate_list = list(np.ravel(results))
	return jsonify(sdate_list)
    

@app.route("/api/v1.0/<sdate>,<edate>")
def startrange(sdate='2016-08-23',edate='2017-08-23'):


if __name__ == '__main__':
    app.run()