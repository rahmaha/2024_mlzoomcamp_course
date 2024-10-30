
import pickle

dv_path = 'dv.bin'
model_path = 'model1.bin'

#load and read file
def load_file(file):
    with open(file, 'rb') as f_in: 
        return pickle.load(f_in)

def predict(customer):
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    return y_pred

dv = load_file(dv_path)
model = load_file(model_path)
customer = {"job": "management", "duration": 400, "poutcome": "success"}

print(predict(customer))