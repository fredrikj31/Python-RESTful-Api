import mysql.connector
import json

class Database:
	def __init__(self, hostname, username, password, database):
		self.hostname = hostname
		self.username = username
		self.password = password
		self.database = database

		try:
			self.mydb = mysql.connector.connect(
				host=self.hostname,
				user=self.username,
				passwd=self.password,
				database=self.database
			)

			self.mycursor = self.mydb.cursor()

		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print("Something is wrong with your user name or password")
			elif err.errno == errorcode.ER_BAD_DB_ERROR:
				print("Database does not exist")
			else:
				print(err)


	def getDevices(self):
		self.mycursor.execute("SELECT * FROM `devices`")

		myresult = self.mycursor.fetchall()

		deviceList = []

		deviceInfo = {}

		for x in myresult:
			(Id, DeviceName, DeviceType, Added) = x
			deviceInfo.update({'Id': Id})
			deviceInfo.update({'Device Name': DeviceName})
			deviceInfo.update({'Device Type': DeviceType})
			deviceInfo.update({'Added': Added})

			deviceList.append(deviceInfo)
			deviceInfo = {}


		return deviceList

	def getDevice(self, Id):
		self.mycursor.execute("SELECT * FROM `devices` WHERE `Id`='{}'".format(Id))

		print("Row affected: {}".format(self.mycursor.rowcount))

		if self.mycursor.rowcount == 1:
			myresult = self.mycursor.fetchone()
			deviceInfo = {}
			(Id, DeviceName, DeviceType, Added) = myresult
			deviceInfo.update({'Id': Id})
			deviceInfo.update({'Device Name': DeviceName})
			deviceInfo.update({'Device Type': DeviceType})
			deviceInfo.update({'Added': Added})

			return deviceInfo
		else:
			return "Could not find any device with that Id"