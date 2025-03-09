from flask import Blueprint, request, jsonify
from pymongo.errors import DuplicateKeyError
from config import User
import datetime
from utilities.password import hash_password, verify_password
from utilities.JWTManagement import create_jwt

import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

loginRegister = Blueprint('loginRegister', __name__)

@loginRegister.route('/login', methods=['POST'])
def login():
    data = request.json
    try:
        user = User.find_one({'email': data['email']})
        if not user:
            return jsonify({'msg': 'User not found'}), 404
        
        if not verify_password(data['password'], user['password']):
            return jsonify({'msg': 'Invalid password'}), 400
        
        User.update_one({'email': data['email']}, {'$set': {'last_login': datetime.datetime.utcnow()}})
        token = create_jwt({'email': user['email'], 'role': user['role']}, 604800)

        return jsonify({'msg': 'Login successful', 'token': token}), 200
    except Exception as e:
        logger.error(f"Login failed: {e}")
        return jsonify({'msg': 'Login failed', 'error': str(e)}), 400


@loginRegister.route('/register', methods=['POST'])
def register():
    
    data = request.get_json()
    try:
        hashed_password = hash_password(data['password'])
    
        registerDev = User.insert_one({
            'username': data['username'],
            'password': hashed_password,
            'email': data['email'],
            'employee_id': data['employee_id'],
            # 'id_card': data['id_card'],
            'role': 'user',
            'appRegistred': []
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