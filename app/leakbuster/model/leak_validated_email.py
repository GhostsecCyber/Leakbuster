from app.leakbuster import db
from app.leakbuster.model import *


class ValidatedEmailsMD(db.Model, BaseModel):

    __tablename__ = 'validatedEmails'

    valid_email = db.Column(db.Boolean, nullable=False)

    email_id = db.Column(db.String(32), db.ForeignKey('leakEmail.id'))

    @property
    def serialized(self):
        return {
            'id': self.id,
            'valid_email': self.valid_email,
            'mail_id': self.email_id,
            'created': self.created,
            'updated': self.updated
        }
