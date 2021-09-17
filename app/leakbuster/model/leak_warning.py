from app.leakbuster import db
from app.leakbuster.model import *


class LeakWarningMD(db.Model, BaseModel):

    __tablename__ = 'leakWarning'

    warning_type = db.Column(db.String(6), nullable=False)
    comp_domain = db.Column(db.String(300), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(500))

    leak_id = db.Column(db.String(32), db.ForeignKey('leakSource.id'))

    @property
    def serialized(self):
        return {
            'id': self.id,
            'warning_type': self.warning_type,
            'comp_domain': self.comp_domain,
            'password': self.password,
            'email': self.email,
            'leak_id': self.leak_id,
            'created': self.created,
            'updated': self.updated
        }
