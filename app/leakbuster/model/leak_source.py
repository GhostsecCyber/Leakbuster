from app.leakbuster import db
from app.leakbuster.model import *


class LeakSourceMD(db.Model):

    __tablename__ = 'leakSource'

    id = db.Column(db.String(32), primary_key=True)
    url = db.Column(db.String(200), unique=True)
    date = db.Column(db.String(200))
    description = db.Column(db.String(400))
    author = db.Column(db.String(200))

    general = db.relationship('LeakGeneralMD')
    leak_emails = db.relationship('LeakEmailMD')
    leak_password = db.relationship('LeakPasswordMD')

    @property
    def serialized(self):
        return {
            'id': self.id,
            'url': self.url,
            'date': self.date,
            'description': self.description,
            'author': self.author,
            'general': self.general,
            'leak_emails': self.leak_emails,
            'leak_password': self.leak_password

        }
