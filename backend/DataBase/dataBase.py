from pymongo import MongoClient,ASCENDING
import datetime

client = MongoClient('localhost', 27017)

db = client['auth-sys']



developerConsole = db['developer-console']

user = db['user']   

admin = db['admin']


developerConsole.create_index([('email', ASCENDING)], unique=True)
developerConsole.create_index([('employee_id', ASCENDING)], unique=True)

user.create_index([('email', ASCENDING)], unique=True)
user.create_index([('user_id', ASCENDING)], unique=True)

admin.create_index([('email', ASCENDING)], unique=True)
admin.create_index([('employee_id', ASCENDING)], unique=True)