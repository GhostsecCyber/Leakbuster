from app.leakbuster.resources.endpoints import api, general, login_required
from flask import request, jsonify
from app.leakbuster.schemas.validator import validate_request
from app.leakbuster.schemas.leak.general import ValidationData


@api.route('/leak/general/', methods=['GET'])
@login_required(roles=["admin"])
def get_leak_generals():
    return jsonify(general.get_generals(request))


@api.route('/leak/general/', methods=['POST'])
@login_required(roles=["admin", "script"])
@validate_request(ValidationData)
def register_leak_generals():
    return jsonify(general.create_general(request))


@api.route('/leak/general/<string:id>', methods=['GET'])
@login_required(roles=["user", "admin"])
def get_leak_general(id):
    return jsonify(general.get_general(id))


@api.route('/leak/general/<string:id>', methods=['DELETE'])
@login_required(roles=["admin"])
def delete_leak_general(id):
    return jsonify(general.delete_general(id))
