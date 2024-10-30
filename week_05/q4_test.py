
import requests

url = 'http://localhost:9696/q4_predict'
client = {"job": "student", "duration": 280, "poutcome": "failure"}

response = requests.post(url, json=client).json()
print(response)


