import flask
from flask_restful import Resource, Api, reqparse

class AuthUser:
	def checkAuth(self):
		parser = reqparse.RequestParser()
		parser.add_argument('apiKey', location='headers')
		args = parser.parse_args()

		if args['apiKey'] == "6z5s10RbwlTwExZ1":
			return True
		else:
			return False