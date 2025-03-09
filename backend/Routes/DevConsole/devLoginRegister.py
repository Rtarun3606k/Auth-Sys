from flask import Blueprint, request, jsonify
from config import DeveloperConsole
import bcrypt
import datetime
from utilities.JWTManagement import create_jwt, verify_jwt
from pymongo.errors import DuplicateKeyError
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to hash a password
def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

# Function to verify a password
def verify_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

devLoginRegister = Blueprint('devLoginRegister', __name__)

@devLoginRegister.route('/login', methods=['POST'])
def login():
    data = request.json
    try:
        user = DeveloperConsole.find_one({'email': data['email']})
        if not user:
            return jsonify({'msg': 'User not found'}), 404
        
        if not verify_password(data['password'], user['password']):
            return jsonify({'msg': 'Invalid password'}), 400
        
        DeveloperConsole.update_one({'email': data['email']}, {'$set': {'last_login': datetime.datetime.utcnow()}})
        token = create_jwt({'email': user['email'], 'role': user['role']}, 604800)

        return jsonify({'msg': 'Login successful', 'token': token}), 200
    except Exception as e:
        logger.error(f"Login failed: {e}")
        return jsonify({'msg': 'Login failed', 'error': str(e)}), 400

@devLoginRegister.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    try:
        hashed_password = hash_password(data['password'])
    
        registerDev = DeveloperConsole.insert_one({
            'username': data['username'],
            'password': hashed_password,
            'email': data['email'],
            'employee_id': data['employee_id'],
            # 'id_card': data['id_card'],
            'role': 'developer',
            
        })
        
        if not registerDev:
            return jsonify({'msg': 'User registration failed'}), 400
        
        return jsonify({'msg': 'User registered successfully'}), 200
    except DuplicateKeyError as e:
        logger.error(f"User registration failed: {e}")
        return jsonify({'msg': 'User registration failed', 'error': 'Email or Employee ID already exists'}), 400
    except Exception as e:
        
        logger.error(f"User registration failed: {e}")
        return jsonify({'msg': 'User registration failed', 'error': str(e)}), 400