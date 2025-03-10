from flask import Blueprint, request, jsonify
from config import DeveloperConsole,Admin
import bcrypt
import datetime
from utilities.JWTManagement import create_jwt, verify_jwt
from pymongo.errors import DuplicateKeyError
import logging
from utilities.password import hash_password,verify_password

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


adminLoginRegister = Blueprint('adminLoginRegister', __name__)

@adminLoginRegister.route('/login', methods=['POST'])
def login():
    data = request.json
    try:
        user = Admin.find_one({'email': data['email']})
        if not user:
            return jsonify({'msg': 'User not found'}), 404
        
        if not verify_password(data['password'], user['password']):
            return jsonify({'msg': 'Invalid password'}), 400
        
        Admin.update_one({'email': data['email']}, {'$set': {'last_login': datetime.datetime.utcnow()}})
        token = create_jwt({'email': user['email'], 'role': user['role']}, 604800)

        return jsonify({'msg': 'Login successful', 'token': token}), 200
    except Exception as e:
        logger.error(f"Login failed: {e}")
        return jsonify({'msg': 'Login failed', 'error': str(e)}), 400

@adminLoginRegister.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    try:
        hashed_password = hash_password(data['password'])
    
        registerDev = Admin.insert_one({
            'username': data['username'],
            'password': hashed_password,
            'email': data['email'],
            'employee_id': data['employee_id'],
            # 'id_card': data['id_card'],
            'role': 'admin',
            
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