from app.leakbuster.resources.endpoints import api, email, login_required
from flask import request, jsonify
from app.leakbuster.schemas.validator import validate_request
from app.leakbuster.schemas.leak.email import ValidationData


@api.route('/leak/email/', methods=['GET'])
@login_required(roles=["admin", "script"])
def get_leak_emails():
    return jsonify(email.get_mails(request))


@api.route('/leak/email/', methods=['POST'])
@login_required(roles=["admin", "script"])
@validate_request(ValidationData)
def register_leak_emails():
    return jsonify(email.create_mail(request))


@api.route('/leak/email/<string:id>', methods=['GET'])
@login_required(roles=["user", "admin", "script"])
def get_leak_email(id):
    return jsonify(email.get_mail(id))


@api.route('/leak/email/<string:id>', methods=['PUT'])
@login_required(roles=["admin"])
@validate_request(ValidationData)
def update_leak_email(id):
    return jsonify(email.update_mail(request, id))


@api.route('/leak/email/<string:id>', methods=['DELETE'])
@login_required(roles=["admin"])
def delete_leak_email(id):
    return jsonify(email.delete_mail(id))
