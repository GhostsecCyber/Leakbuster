from app.leakbuster.resources.endpoints import api, wordlist, login_required
from flask import request, jsonify
from app.leakbuster.schemas.validator import validate_request
from app.leakbuster.schemas.leak.wordlist import ValidationData


@api.route('/wordlist/', methods=['GET'])
@login_required(roles=["admin"])
def get_wordlist():
    return jsonify(wordlist.get_wordlists(request))


@api.route('/wordlist/', methods=['POST'])
@login_required(roles=["admin", "script"])
@validate_request(ValidationData)
def register_wordlist():
    return jsonify(wordlist.add_wordlist(request))
