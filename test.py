import requests

BASE = "http://127.0.0.1:5000/"

# response = requests.get2(BASE + "Hello")
# response = requests.get(BASE + "Hello/person2")
# response = requests.post(BASE + "Hello/anshul/24", {"greet":"hello"})
response = requests.post(BASE + "Video/1", {"name":"Song","likes":20,"dislikes":15,"followers":1000})
print(response.json())
response = requests.get(BASE + "Video/3")
print(response.json())