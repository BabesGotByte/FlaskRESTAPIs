from flask import Flask, request
from flask_restful import Api,Resource,reqparse,abort

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
# api.add_resource(HelloWorld, "/Hello/<string:name>/<int:age>")	

video_put_arguments = reqparse.RequestParser()
video_put_arguments.add_argument("name",type=str,help="Name of the video is required", required=True)
video_put_arguments.add_argument("likes",type=int,help="Name of the video is required", required=True)
video_put_arguments.add_argument("dislikes",type=int,help="Name of the video is required", required=True)
video_put_arguments.add_argument("followers",type=int,help="Name of the video is required", required=True)

video = {}

def video_id_not_exits(video_id):
	if video_id not in video:
		abort(404,message="Video id is not found...")

class Video(Resource):
	def get(self,video_id):
		video_id_not_exits(video_id)
		return video[video_id]
	def post(self,video_id):
		args = video_put_arguments.parse_args()
		video[video_id] = args
		return video[video_id],201

api.add_resource(Video, "/Video/<int:video_id>")

if __name__ == "__main__":
	app.run(debug=True)
