from app.leakbuster.resources.endpoints import api, source, login_required
from flask import request, jsonify


@api.route('/leak/source/', methods=['GET'])
@login_required(roles=["admin", "script"])
def get_leak_sources():
    return jsonify(source.get_leaks(request))


@api.route('/leak/source/', methods=['POST'])
@login_required(roles=["admin", "script"])
def register_leak_sources():
    return jsonify(source.create_leak(request))


@api.route('/leak/source/<string:id>', methods=['GET'])
@login_required(roles=["admin", "script"])
def get_leak_source(id):
    return jsonify(source.get_leak(id))


@api.route('/leak/source/<string:id>', methods=['PUT'])
@login_required(roles=["admin"])
def update_leak_source(id):
    return jsonify(source.update_leak(request, id))


@api.route('/leak/source/<string:id>', methods=['DELETE'])
@login_required(roles=["admin"])
def delete_leak_source(id):
    return jsonify(source.delete_leak(id))
