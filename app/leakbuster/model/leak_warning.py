from app.leakbuster import db
from app.leakbuster.model import *


class LeakWarningMD(db.Model, BaseModel):

    __tablename__ = 'leakWarning'

    warning_type = db.Column(db.String(3072), nullable=False)
    comp_domain = db.Column(db.String(3072), nullable=False)
    leak_password = db.Column(db.String(3072), nullable=False)
    email = db.Column(db.String(3072))

    leak_id = db.Column(db.String(32), db.ForeignKey('leakSource.id'))

    @property
    def serialized(self):
        self.read()
        return {
            'id': self.id,
            'warning_type': self.warning_type,
            'comp_domain': self.comp_domain,
            'password': self.leak_password,
            'email': self.email,
            'leak_id': self.leak_id,
            'created': self.created,
            'updated': self.updated
        }
