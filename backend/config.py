from flask import Flask 
from flask_cors import CORS


# load env
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app)


# Database



