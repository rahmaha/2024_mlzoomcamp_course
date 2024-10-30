# ## Load the model

import pickle

from flask import Flask
from flask import request
from flask import jsonify

dv_path = 'dv.bin'
model_path = 'model2.bin'

#load and read file
def load_file(file):
    with open(file, 'rb') as f_in: 
        return pickle.load(f_in)
    
dv = load_file(dv_path)
model = load_file(model_path)

app = Flask('credit-score')
@app.route('/q6_predict', methods=['POST'])

def q6_predict():
    customer = request.get_json()
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    get_credit = y_pred >= 0.5

    result = {
        'get_credit_probability': float(y_pred),
        'get_credit': bool(get_credit)
    }
    
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0', port = 9696)
