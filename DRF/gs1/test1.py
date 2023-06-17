import requests
import json

URL = "http://127.0.0.1:8000/student/create/"

data = {
    "name": 'Ronin',
    "roll": 209,
    "city": 'China Town'
}

json_data = json.dumps(data)
res = requests.post(url=URL, data=json_data)

data = res.json()
print(data)