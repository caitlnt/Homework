
#CTa - HW-13 - BellyButton Biodiversity
# Part 01
# !pip install flask_sqlalchemy


import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


from flask import Flask, jsonify, render_template
app = Flask(__name__)


#################################################
# Database Setup
#################################################
dbfile = os.path.join('db', 'belly_button_biodiversity.sqlite')
engine = create_engine(f"sqlite:///{dbfile}")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Samples_Metadata = Base.classes.samples_metadata
OTU = Base.classes.otu
Samples = Base.classes.samples

# Create our session (link) from Python to the DB
session = Session(engine)


#Part 01 - Route
@app.route("/")
def index():
    df_bbd = pd.read_csv('Resources/bbd_samples.csv')
    df_bbd_index = df_bbd.set_index('otu_id')
    results = list(df_bbd_index)
    
    df_list = list(np.ravel(results))
    return render_template("index.html", df_list = df_list)


@app.route('/names')
def names():
    df_bbd = pd.read_csv('Resources/bbd_samples.csv')
    df_bbd_index = df_bbd.set_index('otu_id')
    results = list(df_bbd_index)
    
    df_list = list(np.ravel(results))
    return jsonify(df_list)


@app.route('/otu')
def otu():
    df_bbd = pd.read_csv('Resources/bbd_otu_id.csv')
    df_bbd_index = df_bbd.set_index('otu_id')
    results = df_bbd_index['lowest_taxonomic_unit_found']
    
    df_list = list(np.ravel(results))
    return jsonify(df_list)


@app.route('/metadata/<sample>')
def metadata(sample):
    df_bbd = pd.read_csv('Resources/bbb_metadata.csv')
    df_bbd_mindex = df_bbd.set_index('SAMPLEID')
    sampleID = int(sample.replace("BB_",""))
    df_sample = df_bbd_mindex.loc[sampleID]
    df_sample["SAMPLEID"] = sampleID
    results = df_sample[["AGE","BBTYPE","ETHNICITY","GENDER","LOCATION","SAMPLEID"]]
    
    df_list = results.to_dict()
    return jsonify(df_list)


@app.route('/wfreq/<samplewf>')
def wfreq(samplewf):
    df_bbd = pd.read_csv('Resources/bbb_metadata.csv')
    df_bdd_windex = df_bdd.set_index('SAMPLEID')
    samplewfID = int(samplewf.replace("BB_",""))
    df_wf = df_windex.loc[[samplewfID],['WFREQ']]
    results = df_wf["WFREQ"].item()
        
    return jsonify(results)



@app.route('/samples/<sample>')
def sample(sample = 'BB_943'):
    df_bdd = pd.read_csv('Resources/bbd_samples.csv')
    df_sample_filter = df_bdd.filter(items = [sample,'otu_id'])
    df_sample_sort = df_sample_filter.sort_values(by=sample, ascending=False)
    df_sample_nonzero_nan = df_sample_sort[df_sample_sort > 0]
    df_sample_nonzero = df_sample_nonzero_nan.dropna().head(10)
    sample_values = df_sample_nonzero[sample].tolist()
    otu_ids = df_sample_nonzero['otu_id'].tolist()
    results = [{'otu_ids':otu_ids,'sample_values':sample_values}]

    return jsonify(results)


# run the python script through anaconda prompt

if __name__ == "__main__":
   app.run(debug=True)


