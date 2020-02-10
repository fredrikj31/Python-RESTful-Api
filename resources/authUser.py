import flask
from flask_restful import reqparse, Resource

class AuthUser(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()

	def post(self):
		data = self.reqparse.parse_args()
		data['key'] == request.headers['key']
		if data['key'] == "6z5s10RbwlTwExZ1":
			print("Success")
			return 200
		else:
			return 400