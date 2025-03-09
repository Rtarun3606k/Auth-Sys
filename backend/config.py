from flask import Flask 
from flask_cors import CORS

from DataBase.dataBase import db


# load env
from dotenv import load_dotenv
load_dotenv()




#database registrations 
DeveloperConsole = db.developerConsole 
User = db.user
Admin = db.admin


app = Flask(__name__)
CORS(app)


# Database



