from flask import Flask
from flask_restful import Resource, Api, reqparse
import os
import markdown

#Importing Classes
from classes import devices


app = Flask(__name__)

api = Api(app)

api.add_resource(devices.Device, '/devices')

@app.route("/")
def index():
	#Default site

	with open("./docs.md", "r") as markdown_file:
		content = markdown_file.read()

		return content

app.run(host='0.0.0.0', port='80', debug=True)