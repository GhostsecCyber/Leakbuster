from app.leakbuster import db
from app.leakbuster.model import *


class LeakSourceMD(db.Model, BaseModel):

    __tablename__ = 'leakSource'

    url = db.Column(db.String(3072), unique=True)
    date = db.Column(db.String(3072))
    description = db.Column(db.String(3072))
    author = db.Column(db.String(3072))

    general = db.relationship('LeakGeneralMD')
    leak_emails = db.relationship('LeakEmailMD')
    leak_password = db.relationship('LeakPasswordMD')

    @property
    def serialized(self):
        self.read()
        return {
            'id': self.id,
            'url': self.url,
            'date': self.date,
            'description': self.description,
            'author': self.author,
            'general': [x.serialized for x in self.general],
            'leak_emails': [x.serialized for x in self.leak_emails],
            'leak_password': [x.serialized for x in self.leak_password],
            'created': self.created,
            'updated': self.updated

        }
