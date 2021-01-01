import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "video/1", {"name": 'Python tutorial 1', 'views': 100000, "likes": 10})
response = requests.get(BASE + "video/1")
print(response.json())