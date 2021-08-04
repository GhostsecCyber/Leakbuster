from flask import Blueprint
from app.leakbuster.resources import *
user = User()

api = Blueprint('api', __name__, url_prefix='/api/v2')

from app.leakbuster.resources.api.users import *
