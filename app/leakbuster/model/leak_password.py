from app.leakbuster import db
from app.leakbuster.model import *


class LeakPasswordMD(db.Model):

    __tablename__ = 'leakPassword'

    id = db.Column(db.String(32), primary_key=True)
    password = db.Column(db.String(600))

    leak_id = db.Column(db.String(32), db.ForeignKey('leakSource.id'))
    email_id = db.Column(db.String(32), db.ForeignKey('leakEmail.id'))

    @property
    def serialized(self):
        return {
            'id': self.id,
            'password': self.password,
            'leak_id': self.leak_id,
            'email_id': self.email_id
        }
