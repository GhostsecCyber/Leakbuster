from flask import Blueprint
from app.leakbuster.resources import *
user = User()
source = Source()

api = Blueprint('api', __name__, url_prefix='/api/v2')

from app.leakbuster.resources.endpoints.users import *
from app.leakbuster.resources.endpoints.leaks import *
