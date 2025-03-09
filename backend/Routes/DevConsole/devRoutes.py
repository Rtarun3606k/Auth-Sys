from flask import Blueprint, request, jsonify
from config import DeveloperConsole,Application
from utilities.JWTManagement import create_jwt, verify_jwt, middleWare
from utilities.searilization import serialize_doc,generate_api_keys
from pymongo.errors import DuplicateKeyError

devRoutes = Blueprint('devRoutes', __name__)

@devRoutes.route('/getDev', methods=['GET'])
def getDev():
    try:
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'msg': 'Authorization header missing'}), 401
        
        # Assuming the token is in the format "Bearer <token>"
        auth_token = auth_header.split(" ")[1]
        payload = middleWare(auth_token)
        
        if payload['role'] != 'developer':
            return jsonify({'msg': 'Unauthorized'}), 401
        
        print(payload,payload['email'])
        
        dev = DeveloperConsole.find_one({'email': payload['email']})
        if not dev:
            return jsonify({'msg': 'Developer not found'}), 404
        dev = serialize_doc(dev)
        return jsonify({'DevData': dev, 'msg': 'Data found successfully'}), 200
    except Exception as e:
        return jsonify({'msg': 'Error', 'error': str(e)}), 400
    
@devRoutes.route('/updateDev', methods=['PUT'])
def updateDev():
    try:
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'msg': 'Authorization header missing'}), 401
        
        # Assuming the token is in the format "Bearer <token>"
        auth_token = auth_header.split(" ")[1]
        payload = middleWare(auth_token)
        
        if payload['role'] != 'developer':
            return jsonify({'msg': 'Unauthorized'}), 401
        
        data = request.json
        updateDev = DeveloperConsole.update_one({'email': payload['email']}, {'$set': data})
        
        if not updateDev:
            return jsonify({'msg': 'Update failed'}), 400
        
        return jsonify({'msg': 'Update successful'}), 200
    except Exception as e:
        return jsonify({'msg': 'Error', 'error': str(e)}), 400
    
@devRoutes.route('/deleteDev', methods=['DELETE'])
def deleteDev():
    try:
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'msg': 'Authorization header missing'}), 401
        
        # Assuming the token is in the format "Bearer <token>"
        auth_token = auth_header.split(" ")[1]
        payload = middleWare(auth_token)
        
        if payload['role'] != 'developer':
            return jsonify({'msg': 'Unauthorized'}), 401
        
        deleteDev = DeveloperConsole.delete_one({'email': payload['email']})
        
        if not deleteDev:
            return jsonify({'msg': 'Delete failed'}), 400
        
        return jsonify({'msg': 'Delete successful'}), 200
    except Exception as e:
        return jsonify({'msg': 'Error', 'error': str(e)}), 400
    


@devRoutes.route('/getAllDevs', methods=['GET'])
def getAllDevs():
    try:
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'msg': 'Authorization header missing'}), 401
        
        # Assuming the token is in the format "Bearer <token>"
        auth_token = auth_header.split(" ")[1]
        payload = middleWare(auth_token)
        
        if payload['role'] != 'developer':
            return jsonify({'msg': 'Unauthorized'}), 401
        
        devs = DeveloperConsole.find({'role': 'developer'})
        if not devs:
            return jsonify({'msg': 'No developers found'}), 404
        
        return jsonify({'DevsData': devs, 'msg': 'Data found successfully'}), 200
    except Exception as e:
        return jsonify({'msg': 'Error', 'error': str(e)}),401
    



@devRoutes.route('/createApp', methods=['POST'])
def createApp():
    try:
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'msg': 'Authorization header missing'}), 401
        
        # Assuming the token is in the format "Bearer <token>"
        auth_token = auth_header.split(" ")[1]
        payload = middleWare(auth_token)
        
        if payload['role'] != 'developer':
            return jsonify({'msg': 'Unauthorized'}), 401
        
        data = request.json
        app_data = data.get('appData')
        if not app_data:
            return jsonify({'msg': 'App data missing'}), 400
        
        if not app_data.get('appname') or not app_data.get('redirectionURL') or not app_data.get('errorURL'):
            return jsonify({'msg': 'App data incomplete'}), 400
        
        # Generate unique API keys
        api_keys = generate_api_keys(app_data['appname'])
        app_data.update(api_keys)
        
        # Find the developer document
        print(app_data)
        developer = DeveloperConsole.find_one({'email': payload['email']})
        if not developer:
            return jsonify({'msg': 'Developer not found'}), 404
        
        # Add developer's _id to the app data
        app_data['developer_id'] = developer['_id']
        
        # Insert the new app data into the Application collection
        app_result = Application.insert_one(app_data)
        app_id = app_result.inserted_id
        
        # Ensure 'apps' field is an array and push the new app ID
        update_result = DeveloperConsole.update_one(
            {'email': payload['email']},
            {'$push': {'apps': app_id}}
        )
        
        if update_result.modified_count == 0:
            return jsonify({'msg': 'App creation failed'}), 400
        
        return jsonify({'msg': 'App created successfully', 'app_id': str(app_id), **api_keys}), 200
    
    except DuplicateKeyError as e:
        return jsonify({'msg': 'App creation failed', 'error': 'App already exists', 'details': str(e)}), 400

    except Exception as e:
        return jsonify({'msg': 'Error', 'error': str(e)}), 400