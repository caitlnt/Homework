import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
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

#################################################
# Flask Setup
#################################################
climateapp = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Avalable Routes:<br/>"
        f"/api/v1.0/precipitation - List of Dates and Temperatures<br/>"

        f"/api/v1.0/stations"
        f"- List of invoice totals per country<br/>"

        f"/api/v1.0/tobs"
        f"- Temperature Observations (tobs)<br/>"

        f"/api/v1.0/<start>"
        f"- List of start dates<br/>"

        f"/api/v1.0/<start>/<end>"
        f"- List of start and end dates<br/>"
    )


@app.route("/api/v1.0/precipitation")
def countries():
    """Return a list of all billing countries"""
    # Query all countries from the Invoices table
    results = session.query(Invoices.BillingCountry).\
        group_by(Invoices.BillingCountry).all()

    # Convert list of tuples into normal list
    countries_list = list(np.ravel(results))

    return jsonify(countries_list)


@app.route("/api/v1.0/stations")
def totals():
    """Return a list invoice totals by country.

    Each item in the list is a dictionary with keys `country` and `total`"""
    # Query all countries from the Invoices table
    results = session.query(Invoices.BillingCountry, func.sum(Invoices.Total)).\
        group_by(Invoices.BillingCountry).\
        order_by(func.sum(Invoices.Total).desc()).all()

    # Create a list of dicts with `country` and `total` as the keys and
    invoice_totals = []
    for result in results:
        row = {}
        row["country"] = result[0]
        row["total"] = float(result[1])
        invoice_totals.append(row)

    return jsonify(invoice_totals)


@app.route("/api/v1.0/tobs")
def postal_codes(country='USA'):
    """Return a list of billing postal codes for a country."""
    results = session.query(Invoices.BillingPostalCode).\
        filter(Invoices.BillingCountry == country).\
        group_by(Invoices.BillingPostalCode).all()

    postal_codes_list = list(np.ravel(results))

    return jsonify(postal_codes_list)


@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def total_items(country='USA'):
    """Return the invoice items total for a specific country."""
    # Calculate the total for a given country
    items_total = session.query(func.sum(Items.UnitPrice * Items.Quantity)).\
        filter(Invoices.InvoiceId == Items.InvoiceId).\
        filter(Invoices.BillingCountry == country).scalar()

    return jsonify(float(items_total))


@app.route("/api/v1.0/postalcodes/totals")
@app.route("/api/v1.0/postalcodes/totals/<country>")
def total_per_postalcode(country='USA'):
    """Return a list of invoice totals per postal code for a given country."""
    # Calculate invoice item totals per postal code for a given country
    sel = [
        Invoices.BillingPostalCode,
        func.sum(Items.UnitPrice * Items.Quantity)]

    results = session.query(*sel).\
        filter(Invoices.InvoiceId == Items.InvoiceId).\
        filter(Invoices.BillingCountry == country).\
        group_by(Invoices.BillingPostalCode).\
        order_by(func.sum(Items.UnitPrice * Items.Quantity).desc()).all()

    # Create a dictionary from the row data and append to a list of all_passengers
    invoice_totals_per_postalcode = []
    for result in results:
        row = {}
        row["postal_code"] = result[0]
        row["invoice_total"] = float(result[1])
        invoice_totals_per_postalcode.append(row)

    return jsonify(invoice_totals_per_postalcode)


if __name__ == '__main__':
    app.run()
