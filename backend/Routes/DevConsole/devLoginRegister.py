from flask import Blueprint, request, jsonify

from config import DeveloperConsole

import bcrypt

# Function to hash a password

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
    DeveloperConsole.insert_one({
        'username': data['username'],

    })


@devLoginRegister.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = hash_password(data['password'])
    
    DeveloperConsole.insert_one({
        'username': data['username'],
        'password': hashed_password,
        'email': data['email'],
        'employee_id': data['employee_id'],
        # 'id_card': data['id_card'],
    })
    
    return jsonify({'msg': 'User registered successfully'})