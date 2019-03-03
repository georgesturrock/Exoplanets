#### This WORKS!
# ACI scoring program
# import things required by this script
import json
import numpy as np
import pandas as pd
import os
import pickle
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestClassifier

from azureml.core.model import Model

# load the model
def init():
    global model
    # retrieve the path to the model file using the model name
    model_path = Model.get_model_path('rfClfJL.p')
    model = joblib.load(model_path)

# Passes data to the model and returns the prediction
def run(raw_data):
    #data = np.array(json.loads(raw_data)['data'])
	data = np.array(json.loads(raw_data))
	df = pd.DataFrame.from_records(data)
    # make prediction
	y_hat = model.predict_proba(df)
	return json.dumps(y_hat.tolist())