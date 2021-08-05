from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.leakbuster.utils import config_APP, register_error_handlers
from flasgger import Swagger
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
config_APP(app)
db = SQLAlchemy(app)
Migrate(app, db)

from app.leakbuster.resources.api import *
from app.leakbuster.resources.frontend import *

Swagger(app, template_file='apidocs.yaml')


def create_app():
    app.register_blueprint(api)
    # app.register_blueprint(frontend)

    register_error_handlers(app)
    User().create_admin()

    return app
