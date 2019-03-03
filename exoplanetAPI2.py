#### THIS ONE WORKS ####
# GCP Flask API
# Dependencies
from flask import Flask, request, jsonify
from sklearn.externals import joblib
import traceback
import pandas as pd
import numpy as np

# Your API definition
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if rf:
        try:
            json_ = request.json
            print(json_)
            query = pd.DataFrame.from_records([json_])

            prediction = list(rf.predict_proba(query))

            return jsonify({'prediction': str(prediction)})

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')

if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 5000 # If you don't provide any port the port will be set to 12345

    rf = joblib.load("rfClfJL.p") # Load "model.pkl"
    print ('Model loaded')
    model_columns = joblib.load("rfClfJL.p") # Load "model_columns.pkl"
    print ('Model columns loaded')

    app.run(port=port, debug=True)