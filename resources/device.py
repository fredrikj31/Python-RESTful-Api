from flask import Flask
from flask_restful import Resource, Api, reqparse
import os
import markdown

#Database
from resources.database import Database
myDatabase = Database("localhost", "root", "", "api")

#Auth
from resources.auth import AuthUser
auth = AuthUser()

class Device(Resource):
	def get(self):
		if auth.checkAuth() == False:
			return {'message': 'Unauthorized'}, 400
		else:
			parser = reqparse.RequestParser()
			parser.add_argument('id', required=True)
			args = parser.parse_args()
			print(args['id'])

			return {'message': 'Success', 'data': myDatabase.getDevice(args['id'])}, 200
			

	def post(self):
		if auth.checkAuth() == False:
			return {'message': 'Unauthorized'}, 400
		else:
			parser = reqparse.RequestParser()
			parser.add_argument('deviceName', required=True)
			parser.add_argument('deviceType', required=True)
			args = parser.parse_args()

			result = myDatabase.createDevice(args['deviceName'], args['deviceType'])
			if result == True:
				return {'message': 'Success', 'data': 'Device Created'}, 200
			else:
				return {'message': 'System Error'}, 500

	def delete(self):
		if auth.checkAuth() == False:
			return {'message': 'Unauthorized'}, 400
		else:
			print("Hey")