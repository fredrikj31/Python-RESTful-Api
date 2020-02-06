from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_httpauth import HTTPBasicAuth
import os
import markdown

app = Flask(__name__)

api = Api(app)

auth = HTTPBasicAuth()

USER_DATA = {
    "admin": "SecretPassword"
}

@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password

class Device(Resource):
	@auth.login_required
	def get(self):
		# If the key does not exist in the data store, return a 404 error.

		return {'message': 'Device found', 'data': "Hej med dig"}, 200

@app.route("/")
def index():
	#Default site

	with open("./docs.md", "r") as markdown_file:
		content = markdown_file.read()

		return content


api.add_resource(Device, '/devices')

app.run(host='127.0.0.1', port='5000', debug=True)