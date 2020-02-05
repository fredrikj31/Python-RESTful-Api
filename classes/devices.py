from flask import Flask
from flask_restful import Resource, Api, reqparse

class Device(Resource):
	def get(self):
		# If the key does not exist in the data store, return a 404 error.

		return {'message': 'Device found', 'data': "Hej med dig"}, 200