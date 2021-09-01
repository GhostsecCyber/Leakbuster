from app.leakbuster import db
from app.leakbuster.model import *
from werkzeug.security import generate_password_hash, check_password_hash


class UserMD(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    roles = db.Column(db.String(6), nullable=False)
    phone = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    company = db.Column(db.String(300), nullable=False)
    cdomain = db.Column(db.String(300), unique=True, nullable=False)
    site = db.Column(db.String(300), unique=True, nullable=False)

    @property
    def serialized(self):
        return {
            'id': self.id,
            'username': self.name,
            'role': self.roles,
            'phone': self.phone,
            'email': self.email,
            'company': self.company,
            'cdomain': self.cdomain,
            'site': self.site
        }

    def hash_password(self, password):
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)