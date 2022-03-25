from app.leakbuster import db
from app.leakbuster.model import *


class LeakPasswordMD(db.Model, BaseModel):

    __tablename__ = 'leakPassword'

    leak_password = db.Column(db.String(3072))

    leak_id = db.Column(db.String(32), db.ForeignKey('leakSource.id'))
    email_id = db.Column(db.String(32), db.ForeignKey('leakEmail.id'))

    @property
    def serialized(self):
        self.read()
        return {
            'id': self.id,
            'password': self.leak_password,
            'leak_id': self.leak_id,
            'email_id': self.email_id,
            'created': self.created,
            'updated': self.updated
        }


class PasswordWordlist(db.Model, BaseModel):

    __tablename__ = "passwordWordlist"

    leak_password = db.Column(db.String(3072))

    @property
    def serialized(self):
        self.read()
        return self.leak_password
