import requests

data = {"state": "sp"}

req = requests.post("http://127.0.0.1:5000/api/state/sao&paulo")#, json=data)
print(req.content)
