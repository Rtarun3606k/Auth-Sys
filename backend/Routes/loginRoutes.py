from flask import Blueprint, request, jsonify


loginRegister = Blueprint('loginRegister', __name__)

@loginRegister.route('/login', methods=['POST'])
def login():
    return jsonify({'msg': 'Login'})