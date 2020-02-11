from resources.database import Database

myDB = Database("localhost", "root", "", "api")

print(myDB.getDevices())