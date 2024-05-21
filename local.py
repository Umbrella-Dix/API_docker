import requests


res = requests.get("http://localhost/api/main")

print(res.json())