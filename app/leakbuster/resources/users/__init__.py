from app.leakbuster import db
from flask import abort, request, g
from functools import wraps
from app.leakbuster.model import UserMD
from app.leakbuster.schemas.user import ValidationData
from app.leakbuster.utils import is_user_or_is_admin
import sqlalchemy
import uuid
import os


def login_required(roles=[]):
    def wrapper(func):
        @wraps(func)
        def wrap(*args, **kwargs):
                auth = request.authorization
                user = User().get_user_for_auth(auth.username)
                if auth and user.verify_password(auth.password) and user.roles in roles:
                    if user.roles != 'admin':
                        try:
                            is_user_or_is_admin(user, kwargs['id'])
                        except KeyError:
                            pass
                    return func(*args, **kwargs)
                abort(401)
        return wrap
    return wrapper


class User:

    def create_user(self, request):
        ValidationData(request.json)

        user = UserMD(
            name=request.json['name'],
            roles=request.json['roles'],
            callback=request.json['callback'],
            phone=request.json['phone'],
            email=request.json['email'],
            company=request.json['company'],
            cdomain=request.json['cdomain'],
            sites=request.json['sites']
        )
        user.hash_password(request.json['password'])
        try:
            db.session.add(user)
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            abort(500)

        return {
            "Status": "Success",
            "Message": "User registered successfully!",
            "data": user.serialized()
        }

    def get_users(self, request):
        limit = request.args.get('limit')
        offset = request.args.get('offset')
        data = UserMD.query.paginate(offset, limit, False)
        return {"Status": "Success", "data": [x.serialized for x in data.items]}

    def get_user(self, id):
        user = UserMD.query.get_or_404(id, description="User ID not found")
        return user.serialized

    def delete_user(self, request):
        ...

    def update_user(self, request):
        ...

    def get_user_for_auth(self, username):

        try:
            user = UserMD.query.filter_by(name=username).first()
            if user:
                g.user = user
                return user
        except sqlalchemy.exc.IntegrityError:
            abort(500)
        abort(401)

    def create_admin(self):
        try:
            if not UserMD.query.filter_by(name=os.environ.get('ADMIN_NAME', 'Raven')).first():
                user = UserMD(
                    name=os.environ.get('ADMIN_NAME', 'Raven'),
                    roles='admin',
                    callback='callback',
                    phone='11999999999',
                    email='email@admin.com.br',
                    company='GhostSecCyber',
                    cdomain='@GhostSecCyber.com.br',
                    sites='https://GhostSecCyber.com.br'
                )
                user.hash_password(os.environ.get('ADMIN_PASS', 'raven'))
                db.session.add(user)
                db.session.commit()
                return
        except sqlalchemy.exc.OperationalError:
            return
        except sqlalchemy.exc.ProgrammingError:
            return
