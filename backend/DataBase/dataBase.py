from pymongo import MongoClient
import datetime

client = MongoClient('localhost', 27017)

db = client['auth-sys']



developerConsole = db['developer-console']

user = db['user']   

admin = db['admin']

