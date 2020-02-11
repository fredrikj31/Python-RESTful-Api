import mysql.connector

class Database:
	def __init__(self):
		self.mydb = mysql.connector.connect(
			host="localhost",
			port="8080",
			user="root",
			passwd=""
		)

		print(self.mydb)