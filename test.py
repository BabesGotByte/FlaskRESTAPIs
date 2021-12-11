import requests

BASE = "http://127.0.0.1:5000/"

# response = requests.get2(BASE + "Hello")
# response = requests.get(BASE + "Hello/person2")
response = requests.post(BASE + "Hello/anshul/24", {"greet":"hello"})
print(response.json())