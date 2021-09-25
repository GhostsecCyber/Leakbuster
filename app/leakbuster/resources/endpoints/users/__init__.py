from app.leakbuster.resources.endpoints import api, user, login_required
from flask import request, jsonify
from app.leakbuster.schemas.validator import validate_request
from app.leakbuster.schemas.user import ValidationData


@api.route('/user/', methods=['GET'])
@login_required(roles=["admin"])
def get_users():
    return jsonify(user.get_users(request))


@api.route('/user/<string:id>', methods=['GET'])
@login_required(roles=["admin", "user"])
def get_user(id):
    return jsonify(user.get_user(id))


@api.route('/user/', methods=['POST'])
@login_required(roles=["admin"])
@validate_request(ValidationData)
def create_user():
    return jsonify(user.create_user(request))


@api.route('/user/<string:id>', methods=['PUT'])
@login_required(roles=["admin", "user"])
@validate_request(ValidationData)
def update_user(id):
    return jsonify(user.update_user(request, id))


@api.route('/user/<string:id>', methods=['DELETE'])
@login_required(roles=["admin"])
def delete_user(id):
    return jsonify(user.delete_user(id))
