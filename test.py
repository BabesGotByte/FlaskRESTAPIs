import requests

BASE = "http://127.0.0.1:5000/"

# response = requests.get2(BASE + "Hello")
# response = requests.get(BASE + "Hello/person2")
# response = requests.post(BASE + "Hello/anshul/24", {"greet":"hello"})
# response = requests.post(BASE + "Video/1", {"name":"Song","likes":20,"dislikes":15,"followers":1000})
# print(response.json())
# response = requests.get(BASE + "Video/3")
# print(response.json())

data = [
{"name":"Song1","likes":10,"dislikes":2,"followers":1000},
{"name":"Song2","likes":20,"dislikes":4,"followers":2000},
{"name":"Song3","likes":30,"dislikes":6,"followers":3000},
{"name":"Song4","likes":40,"dislikes":8,"followers":4000},
{"name":"Song5","likes":50,"dislikes":10,"followers":5000}
]

for i in range(len(data)):
	response = requests.post(BASE + "Video/"+str(i), data[i])
	print(response.json())

response = requests.delete(BASE + "Video/2")
print(response)
response = requests.get(BASE + "Video/2")
print(response.json())