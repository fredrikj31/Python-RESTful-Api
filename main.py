from flask import Flask
from flask_restful import Resource, Api, reqparse
import os
import markdown

#Classes
from resources import authUser

app = Flask(__name__)

api = Api(app)

apikey = "6z5s10RbwlTwExZ1"

parser = reqparse.RequestParser()
parser.add_argument('apiKey', location='headers')

class Device(Resource):
	
	def get(self):
		if checkAuth() == True:
			return {'message': 'Device found', 'data': "Hej med dig"}, 200
		else:
			return {'message': 'Unauthorized'}, 400

def checkAuth():
	args = parser.parse_args()

	if args['apiKey'] == "6z5s10RbwlTwExZ1":
		return True
	else:
		return False

"""@app.route("/")
def index():
	#Default site

	with open("./docs.md", "r") as markdown_file:
		content = markdown_file.read()

		return content"""


api.add_resource(Device, '/devices')

app.run(host='127.0.0.1', port='5000', debug=True)