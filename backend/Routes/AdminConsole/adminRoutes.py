from flask import Blueprint, request, jsonify
from config import Admin,User,DeveloperConsole,Application
import logging
from utilities.JWTManagement import middleWare
from utilities.password import hash_password
from bson.json_util import dumps

adminRoutes = Blueprint('adminRoutes', __name__)
logger = logging.getLogger(__name__)

@adminRoutes.route('/admins', methods=['GET'])
def get_admins():
    try:
        authToken = request.headers.get('Authorization')
        if not authToken:
            return jsonify({'msg': 'Authorization header missing'}), 401
        payload = middleWare(authToken)
        if payload['role'] != 'admin':
            return jsonify({'msg': 'Unauthorized'}), 401
        admins = list(Admin.find())
        return jsonify({'admins': dumps(admins)}), 200
    except Exception as e:
        logger.error(f"Fetching admins failed: {e}")
        return jsonify({'msg': 'Fetching admins failed', 'error': str(e)}), 400
    
@adminRoutes.route('/adminUpdate', methods=['PATCH'])
def update_admin():
    data = request.get_json()
    try:
        authToken = request.headers.get('Authorization')
        if not authToken:
            return jsonify({'msg': 'Authorization header missing'}), 401
        payload = middleWare(authToken)
        if payload['role'] != 'admin':
            return jsonify({'msg': 'Unauthorized'}), 401
        if 'password' in data:
            data['password'] = hash_password(data['password'])
        update_result = Admin.update_one({'email': payload['email']}, {'$set': data})
        if update_result.modified_count == 0:
            return jsonify({'msg': 'Admin update failed'}), 400
        return jsonify({'msg': 'Admin updated successfully'}), 200
    except Exception as e:
        logger.error(f"Admin update failed: {e}")
        return jsonify({'msg': 'Admin update failed', 'error': str(e)}), 400
    

@adminRoutes.route('/adminDelete', methods=['DELETE'])
def delete_admin():
    try:
        authToken = request.headers.get('Authorization')
        if not authToken:
            return jsonify({'msg': 'Authorization header missing'}), 401
        payload = middleWare(authToken)
        if payload['role'] != 'admin':
            return jsonify({'msg': 'Unauthorized'}), 401
        delete_result = Admin.delete_one({'email': payload['email']})
        if delete_result.deleted_count == 0:
            return jsonify({'msg': 'Admin deletion failed'}), 400
        return jsonify({'msg': 'Admin deleted successfully'}), 200
    except Exception as e:
        logger.error(f"Admin deletion failed: {e}")
        return jsonify({'msg': 'Admin deletion failed', 'error': str(e)}), 400
    
@adminRoutes.route('/developers', methods=['GET'])
def get_developers():
    try:
        authToken = request.headers.get('Authorization')
        if not authToken:
            return jsonify({'msg': 'Authorization header missing'}), 401
        payload = middleWare(authToken)
        if payload['role'] != 'admin':
            return jsonify({'msg': 'Unauthorized'}), 401
        developers = list(DeveloperConsole.find())
        return jsonify({'developers': dumps(developers)}), 200
    except Exception as e:
        logger.error(f"Fetching developers failed: {e}")
        return jsonify({'msg': 'Fetching developers failed', 'error': str(e)}), 400
    
@adminRoutes.route('/developerUpdate', methods=['PATCH'])
def update_developer():
    data = request.get_json()
    try:
        authToken = request.headers.get('Authorization')
        if not authToken:
            return jsonify({'msg': 'Authorization header missing'}), 401
        payload = middleWare(authToken)
        if payload['role'] != 'admin':
            return jsonify({'msg': 'Unauthorized'}), 401
        if 'password' in data:
            data['password'] = hash_password(data['password'])
        update_result = DeveloperConsole.update_one({'email': payload['email']}, {'$set': data})
        if update_result.modified_count == 0:
            return jsonify({'msg': 'Developer update failed'}), 400
        return jsonify({'msg': 'Developer updated successfully'}), 200
    except Exception as e:
        logger.error(f"Developer update failed: {e}")
        return jsonify({'msg': 'Developer update failed', 'error': str(e)}), 400
    

@adminRoutes.route('/developerDelete', methods=['DELETE'])
def delete_developer():
    try:
        authToken = request.headers.get('Authorization')
        if not authToken:
            return jsonify({'msg': 'Authorization header missing'}), 401
        payload = middleWare(authToken)
        if payload['role'] != 'admin':
            return jsonify({'msg': 'Unauthorized'}), 401
        delete_result = DeveloperConsole.delete_one({'email': payload['email']})
        if delete_result.deleted_count == 0:
            return jsonify({'msg': 'Developer deletion failed'}), 400
        return jsonify({'msg': 'Developer deleted successfully'}), 200
    except Exception as e:
        logger.error(f"Developer deletion failed: {e}")
        return jsonify({'msg': 'Developer deletion failed', 'error': str(e)}), 400
    
@adminRoutes.route('/users', methods=['GET'])
def get_users():
    try:
        authToken = request.headers.get('Authorization')
        if not authToken:
            return jsonify({'msg': 'Authorization header missing'}), 401
        payload = middleWare(authToken)
        if payload['role'] != 'admin':
            return jsonify({'msg': 'Unauthorized'}), 401
        users = list(User.find())
        return jsonify({'users': dumps(users)}), 200
    except Exception as e:
        logger.error(f"Fetching users failed: {e}")
        return jsonify({'msg': 'Fetching users failed', 'error': str(e)}), 400
    

@adminRoutes.route('/userUpdate', methods=['PATCH'])
def update_user():
    data = request.get_json()
    try:
        authToken = request.headers.get('Authorization')
        if not authToken:
            return jsonify({'msg': 'Authorization header missing'}), 401
        payload = middleWare(authToken)
        if payload['role'] != 'admin':
            return jsonify({'msg': 'Unauthorized'}), 401
        if 'password' in data:
            data['password'] = hash_password(data['password'])
        update_result = User.update_one({'email': payload['email']}, {'$set': data})
        if update_result.modified_count == 0:
            return jsonify({'msg': 'User update failed'}), 400
        return jsonify({'msg': 'User updated successfully'}), 200
    except Exception as e:
        logger.error(f"User update failed: {e}")
        return jsonify({'msg': 'User update failed', 'error': str(e)}), 400
    
@adminRoutes.route('/userDelete', methods=['DELETE'])
def delete_user():
    try:
        authToken = request.headers.get('Authorization')
        if not authToken:
            return jsonify({'msg': 'Authorization header missing'}), 401
        payload = middleWare(authToken)
        if payload['role'] != 'admin':
            return jsonify({'msg': 'Unauthorized'}), 401
        delete_result = User.delete_one({'email': payload['email']})
        if delete_result.deleted_count == 0:
            return jsonify({'msg': 'User deletion failed'}), 400
        return jsonify({'msg': 'User deleted successfully'}), 200
    except Exception as e:
        logger.error(f"User deletion failed: {e}")
        return jsonify({'msg': 'User deletion failed', 'error': str(e)}), 400
    

@adminRoutes.route('/applications', methods=['GET'])
def get_applications():
    try:
        authToken = request.headers.get('Authorization')
        if not authToken:
            return jsonify({'msg': 'Authorization header missing'}), 401
        payload = middleWare(authToken)
        if payload['role'] != 'admin':
            return jsonify({'msg': 'Unauthorized'}), 401
        applications = list(Application.find())
        return jsonify({'applications': dumps(applications)}), 200
    except Exception as e:
        logger.error(f"Fetching applications failed: {e}")
        return jsonify({'msg': 'Fetching applications failed', 'error': str(e)}), 400
    
@adminRoutes.route('/applicationUpdate', methods=['PATCH'])
def update_application():
    data = request.get_json()
    try:
        authToken = request.headers.get('Authorization')
        if not authToken:
            return jsonify({'msg': 'Authorization header missing'}), 401
        payload = middleWare(authToken)
        if payload['role'] != 'admin':
            return jsonify({'msg': 'Unauthorized'}), 401
        update_result = Application.update_one({'_id': data['_id']}, {'$set': data})
        if update_result.modified_count == 0:
            return jsonify({'msg': 'Application update failed'}), 400
        return jsonify({'msg': 'Application updated successfully'}), 200
    except Exception as e:
        logger.error(f"Application update failed: {e}")
        return jsonify({'msg': 'Application update failed', 'error': str(e)}), 400
    

@adminRoutes.route('/applicationDelete', methods=['DELETE'])
def delete_application():
    data = request.get_json()
    try:
        authToken = request.headers.get('Authorization')
        if not authToken:
            return jsonify({'msg': 'Authorization header missing'}), 401
        payload = middleWare(authToken)
        if payload['role'] != 'admin':
            return jsonify({'msg': 'Unauthorized'}), 401
        delete_result = Application.delete_one({'_id': data['_id']})
        if delete_result.deleted_count == 0:
            return jsonify({'msg': 'Application deletion failed'}), 400
        return jsonify({'msg': 'Application deleted successfully'}), 200
    except Exception as e:
        logger.error(f"Application deletion failed: {e}")
        return jsonify({'msg': 'Application deletion failed', 'error': str(e)}), 400
    

@adminRoutes.route('/applicationApprove', methods=['PATCH'])
def approve_application():
    data = request.get_json()
    try:
        authToken = request.headers.get('Authorization')
        if not authToken:
            return jsonify({'msg': 'Authorization header missing'}), 401
        payload = middleWare(authToken)
        if payload['role'] != 'admin':
            return jsonify({'msg': 'Unauthorized'}), 401
        update_result = Application.update_one({'_id': data['_id']}, {'$set': {'approved': True}})
        if update_result.modified_count == 0:
            return jsonify({'msg': 'Application approval failed'}), 400
        return jsonify({'msg': 'Application approved successfully'}), 200
    except Exception as e:
        logger.error(f"Application approval failed: {e}")
        return jsonify({'msg': 'Application approval failed', 'error': str(e)}), 400
    
@adminRoutes.route('/applicationReject', methods=['PATCH'])
def reject_application():
    data = request.get_json()
    try:
        authToken = request.headers.get('Authorization')
        if not authToken:
            return jsonify({'msg': 'Authorization header missing'}), 401
        payload = middleWare(authToken)
        if payload['role'] != 'admin':
            return jsonify({'msg': 'Unauthorized'}), 401
        update_result = Application.update_one({'_id': data['_id']}, {'$set': {'approved': False}})
        if update_result.modified_count == 0:
            return jsonify({'msg': 'Application rejection failed'}), 400
        return jsonify({'msg': 'Application rejected successfully'}), 200
    except Exception as e:
        logger.error(f"Application rejection failed: {e}")
        return jsonify({'msg': 'Application rejection failed', 'error': str(e)}), 400
    


 