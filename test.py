import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"name": 'Python tutorial', 'views': 100000, "likes": 800},
    {"name": 'JS tutorial', 'views': 50000, "likes": 22},
    {"name": 'Go tutorial', 'views': 2000, "likes": 58},
]

# Put
for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

# Delete
# response = requests.delete(BASE + "video/2")
# print(response)

# Get
response = requests.get(BASE + "video/2")
print(response.json())

# Update
response = requests.patch(BASE + "video/2", {'views': 22, 'likes': 9678})
print(response.json())