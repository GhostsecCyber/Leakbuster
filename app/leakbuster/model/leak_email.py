from app.leakbuster import db
from app.leakbuster.model import *


class LeakEmailMD(db.Model, BaseModel):

    __tablename__ = 'leakEmail'

    email = db.Column(db.String(500))

    leak_id = db.Column(db.String(32), db.ForeignKey('leakSource.id'))
    leak_password = db.relationship('LeakPasswordMD')

    @property
    def serialized(self):
        return {
            'id': self.id,
            'email': self.email,
            'leak_id': self.leak_id,
            'leak_password': self.leak_password,
            'created': self.created,
            'updated': self.updated
        }
