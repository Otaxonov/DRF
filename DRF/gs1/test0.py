import requests

URL = "http://127.0.0.1:8000/student/1/"

res = requests.get(url=URL)

data = res.json()

print(data)