from flask import abort, request, g
from functools import wraps
from app.leakbuster.model import UserMD
from app.leakbuster.utils import is_user_or_is_admin
from app.leakbuster.crypt import encrypt
import sqlalchemy
import os
import uuid


def login_required(roles=[]):
    def wrapper(func):
        @wraps(func)
        def wrap(*args, **kwargs):
                auth = request.authorization
                user = User().get_user_for_auth(auth.username)
                if auth and user.verify_password(auth.password) and user.roles in roles:
                    if user.roles != 'admin' and user.roles != 'script':
                        try:
                            is_user_or_is_admin(user, kwargs['id'])
                        except KeyError:
                            pass
                    return func(*args, **kwargs)
                else:
                    abort(401)
        return wrap
    return wrapper


class User:

    def create_user(self, request):

        try:

            user = UserMD(
                name=request.json['name'],
                roles=request.json['roles'],
                phone=request.json['phone'],
                email=request.json['email'],
                company=request.json['company'],
                cdomain=request.json['cdomain'],
                site=request.json['site']
            )
            user.hash_password(request.json['password'])

            user.commit()
        except sqlalchemy.exc.IntegrityError as e:
            abort(500)
        except KeyError:
            abort(400, "Missing roles parameter")
        return {
            "Status": "Success",
            "Message": "User registered successfully!",
            "data": user.serialized
        }

    def get_users(self, request):
        limit = request.args.get('limit')
        offset = request.args.get('offset')
        data = UserMD.query.paginate(offset, limit, False)
        return {"Status": "Success", "data": [x.serialized for x in data.items]}

    def get_user(self, id):
        user = UserMD.query.get_or_404(id, description="User ID not found")
        return {'Status': 'Success', 'data': user.serialized}

    def delete_user(self, id):
        user = UserMD.query.get_or_404(id, description="User ID not found")
        user.delete()
        return {
            "Status": "Success",
            "Message": "User Successfully deleted"
        }

    def update_user(self, request, id):

        user = UserMD.query.get_or_404(id, description="User ID not found")
        user.name = request.json['name']
        user.phone = request.json['phone']
        user.email = request.json['email']
        user.company = request.json['company']
        user.cdomain = request.json['cdomain']
        user.site = request.json['site']
        user.hash_password(request.json['password'])

        try:
            user.commit()
        except sqlalchemy.exc.IntegrityError:
            abort(500, "Something went wrong, verify user data and try again")
        return {
            "Status": "Success",
            "Message": "User updated successfully",
            "data": user.serialized
        }

    def get_user_for_auth(self, username):

        try:
            user = UserMD.query.filter_by(name=encrypt(username)).first()
            if user:
                user.read()
                g.user = user
                return user
        except sqlalchemy.exc.IntegrityError:
            abort(500)
        abort(401)

    def create_admin(self):
        try:
            if not UserMD.query.filter_by(name=encrypt(os.environ.get('ADMIN_USER', 'admin'))).first():
                user = UserMD(
                    id=uuid.uuid4().hex,
                    name=os.environ.get('ADMIN_USER', 'admin'),
                    roles='admin',
                    phone='11999999999',
                    email='email@admin.com.br',
                    company='GhostSecCyber',
                    cdomain='@GhostSecCyber.com.br',
                    site='https://GhostSecCyber.com.br'
                )
                user.hash_password(os.environ.get('ADMIN_PASS'))
                user.commit()
                return user
        except sqlalchemy.exc.OperationalError:
            return
        except sqlalchemy.exc.ProgrammingError:
            return

    def create_script_user(self):
        try:
            if not UserMD.query.filter_by(roles=encrypt('script')).first():
                user = UserMD(
                    id=uuid.uuid4().hex,
                    name=os.environ.get('SCRIPT_USER', 'script'),
                    roles='script',
                    phone='99999999999',
                    email='leakbuster_script@leakbuster_script.com.br',
                    company='leakbuster_script',
                    cdomain='@leakbuster_script.com.br',
                    site='https://leakbuster_script.com.br'
                )
                user.hash_password(os.environ.get('SCRIPT_PASS'))
                user.commit()
                return user
        except sqlalchemy.exc.OperationalError:
            return
        except sqlalchemy.exc.ProgrammingError:
            return
