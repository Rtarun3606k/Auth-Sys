from flask import Blueprint, request, jsonify
from config import User
import logging
from utilities.JWTManagement import middleWare
from utilities.password import hash_password

userRoutes = Blueprint('userRoutes', __name__)
logger = logging.getLogger(__name__)


@userRoutes.route('/users', methods=['GET'])
def get_users():
    try:
        authToken = request.headers.get('Authorization')
        if not authToken:
            return jsonify({'msg': 'Authorization header missing'}), 401
        payload = middleWare(authToken)
        if payload['role'] != 'admin':
            return jsonify({'msg': 'Unauthorized'}), 401
        users = list(User.find())
        for user in users:
            user['email'] = str(user['email'])
        return jsonify(users), 200
    except Exception as e:
        logger.error(f"Fetching users failed: {e}")
        return jsonify({'msg': 'Fetching users failed', 'error': str(e)}), 400

@userRoutes.route('/user', methods=['GET'])
def get_user():
    try:
        authToken = request.headers.get('Authorization')
        if not authToken:
            return jsonify({'msg': 'Authorization header missing'}), 401
        payload = middleWare(authToken)
       
        user = User.find_one({'email': payload['email']})
        if user:
            user['_id'] = str(user['_id'])
            return jsonify(user), 200
        return jsonify({'msg': 'User not found'}), 404
    except Exception as e:
        logger.error(f"Fetching user failed: {e}")
        return jsonify({'msg': 'Fetching user failed', 'error': str(e)}), 400

@userRoutes.route('/user', methods=['PUT'])
def update_user():
    data = request.get_json()
    try:
        authToken = request.headers.get('Authorization')
        if not authToken:
            return jsonify({'msg': 'Authorization header missing'}), 401
        payload = middleWare(authToken)
        if payload['role'] != 'user'  or payload['role'] != 'admin':
            return jsonify({'msg': 'Unauthorized'}), 401
        if 'password' in data:
            data['password'] = hash_password(data['password'])
        update_result = User.update_one({'_id': payload['_id']}, {'$set': data})
        if update_result.modified_count == 0:
            return jsonify({'msg': 'User update failed'}), 400
        return jsonify({'msg': 'User updated successfully'}), 200
    except Exception as e:
        logger.error(f"Updating user failed: {e}")
        return jsonify({'msg': 'Updating user failed', 'error': str(e)}), 400

@userRoutes.route('/user', methods=['DELETE'])
def delete_user():
    try:
        authToken = request.headers.get('Authorization')
        if not authToken:
            return jsonify({'msg': 'Authorization header missing'}), 401
        payload = middleWare(authToken)
        if payload['role'] != 'admin' or payload['role'] != 'user':
            return jsonify({'msg': 'Unauthorized'}), 401
        user_email = payload['email']
        delete_result = User.delete_one({'email': user_email})
        if delete_result.deleted_count == 0:
            return jsonify({'msg': 'User deletion failed'}), 400
        return jsonify({'msg': 'User deleted successfully'}), 200
    except Exception as e:
        logger.error(f"Deleting user failed: {e}")
        return jsonify({'msg': 'Deleting user failed', 'error': str(e)}), 400
