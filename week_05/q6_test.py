import requests


url = "http://localhost:9696/q6_predict"


client = {"job": "management", "duration": 400, "poutcome": "success"}
response = requests.post(url, json=client).json()

print(response)