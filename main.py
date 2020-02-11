from flask import Flask
from flask_restful import Resource, Api, reqparse
import os
import markdown

#Classes
from resources.devices import Device

app = Flask(__name__)

api = Api(app)

apikey = "6z5s10RbwlTwExZ1"

@app.route("/")
def index():
	#Default site
	with open("./docs.md", "r") as markdown_file:
		content = markdown_file.read()

		return markdown.markdown(content, extensions=['fenced_code', 'tables', 'nl2br'])


api.add_resource(Device, '/devices')

app.run(host='127.0.0.1', port='5000', debug=True)