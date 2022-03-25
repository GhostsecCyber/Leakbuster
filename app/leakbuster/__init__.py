from flask import Flask, send_from_directory
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


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'img/Leaker.ico')


@app.after_request
def close_sessions(request):
    db.session.close_all()
    return request


from app.leakbuster.resources.endpoints import *
from app.leakbuster.resources.frontend import *

Swagger(app, template_file='apidocs.yaml')


def create_app():
    app.register_blueprint(api)
    # app.register_blueprint(frontend)

    register_error_handlers(app)
    User().create_admin()
    User().create_script_user()

    return app
