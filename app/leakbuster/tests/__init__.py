import os
from flask_testing import TestCase
from app.leakbuster import app, db
from app.leakbuster.model import UserMD, LeakSourceMD, LeakEmailMD, LeakPasswordMD, LeakGeneralMD
from app.leakbuster.resources.users import User
from app.leakbuster.crypt import encrypt, decrypt
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
    user.commit()

    return user.id


def add_testing_update_leak_source():
    leak_source = LeakSourceMD(
        id=uuid.uuid4().hex,
        url='http://unit_test.com',
        description='unit_test',
        date='unit_test',
        author='unit_test'
    )
    leak_source.commit()

    return leak_source.id


def add_testing_update_leak_email():
    leak_id = add_testing_update_leak_source()
    leak_email = LeakEmailMD(
        email='unit_test_mail@mail.com',
        leak_id=leak_id
    )

    password_leak = LeakPasswordMD(
        leak_id=leak_id,
        leak_password="test"
    )
    leak_email.leak_password.append(password_leak)
    leak_email.commit()

    return leak_email.id, leak_id


def add_testing_general_leak():
    leak_id = add_testing_update_leak_source()

    with open(f"{os.getcwd()}\\leakbuster\\downloads\\text.txt", 'wt') as arq:
        arq.write('test')
    arq.close()

    general = LeakGeneralMD(
        leaks=f"{os.getcwd()}\\leakbuster\\downloads\\text.txt",
        leak_id=leak_id
    )

    general.commit()

    return general.id


def add_testing_user():
    User().create_admin()
    User().create_script_user()


def default_header():
    username = os.environ.get('ADMIN_USER', 'admin')
    password = os.environ.get('ADMIN_PASS', 'admin')
    return {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {(base64.b64encode(f"{username}:{password}".encode("utf-8"))).decode("utf-8")}'
    }


def script_user_header():
    username = os.environ.get('SCRIPT_USER', 'script')
    password = os.environ.get('SCRIPT_PASS', 'script')
    return {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {(base64.b64encode(f"{username}:{password}".encode("utf-8"))).decode("utf-8")}'
    }


def default_user_header():
    return {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {(base64.b64encode("test:test".encode("utf-8"))).decode("utf-8")}'
    }


def wrong_header():
    return {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {(base64.b64encode("USERNAME:PASSWORD".encode("utf-8"))).decode("utf-8")}'
    }


class ProjectTest(TestCase):
    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def create_app(self):
        return app
