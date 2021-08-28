import os
from flask_testing import TestCase
from app.leakbuster import app, db
from app.leakbuster.model import UserMD
from app.leakbuster.resources.users import User
import base64
import uuid


def add_testing_update_user():
    user = UserMD(
        id=uuid.uuid4().hex,
        name='test',
        roles='user',
        phone='test',
        email='test@mail.com',
        company='test',
        cdomain='@test.com',
        site='http://test.com'
    )
    user.hash_password('test')
    db.session.add(user)
    db.session.commit()

    return user.id


def add_testing_user():
    User().create_admin()


def default_header():
    username = os.environ.get('ADMIN_USER', 'buster')
    password = os.environ.get('ADMIN_PASS', 'buster')
    return {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {(base64.b64encode(f"{username}:{password}".encode("utf-8"))).decode("utf-8")}'
    }


def wrong_header():
    return {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {(base64.b64encode("test:test".encode("utf-8"))).decode("utf-8")}'
    }


class ProjectTest(TestCase):
    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def create_app(self):
        return app
