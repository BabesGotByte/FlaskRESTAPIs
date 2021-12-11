from flask import Flask, request
from flask_restful import Api,Resource

app = Flask(__name__)
api = Api(app)


names = {
"person1" : {"name": "person1", "age":19, "stream":"science"},
"person2" : {"name": "person2", "age":20, "stream":"arts"},
"person3" : {"name": "person3", "age":21, "stream":"commerce"}
}

books = {}

class HelloWorld(Resource):
	def get(self):
		return {"requestType":"Get"}
	# def get(self,name):
	# 	return names[name]
	def post(self,name,age):
		print(request.form)
		return {"requestType":"Post", "Name" : name, "Age" : age}

# api.add_resource(HelloWorld, "/Hello/<string:name>")	
# api.add_resource(HelloWorld, "/Hello")	
api.add_resource(HelloWorld, "/Hello/<string:name>/<int:age>")	


if __name__ == "__main__":
	app.run(debug=True)
