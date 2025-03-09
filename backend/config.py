from flask import Flask 
from flask_cors import CORS

from DataBase.dataBase import db,developerConsole,user,admin


# load env
from dotenv import load_dotenv
load_dotenv()




#database registrations 
DeveloperConsole = developerConsole
User = user
Admin = admin



app = Flask(__name__)
CORS(app)


# Database



