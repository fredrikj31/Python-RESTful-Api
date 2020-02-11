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

class Devices(Resource):
	def get(self):
		if auth.checkAuth() == False:
			return {'message': 'Unauthorized'}, 400
		else:
			return {'message': 'Success', 'data': myDatabase.getDevices()}, 200
			