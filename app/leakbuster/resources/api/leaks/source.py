from app.leakbuster.resources.api import api, source, login_required
from flask import request, jsonify


@api.route('/leak/source', methods=['GET'])
@login_required(roles=["admin", "script"])
def get_leak_sources():
    return jsonify(source.get_leaks(request))


@api.route('/leak/source', methods=['POST'])
@login_required(roles=["admin", "script"])
def register_leak_sources():
    return jsonify(source.create_leak(request))
