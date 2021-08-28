from app.leakbuster import db
from app.leakbuster.model import *


class LeakGeneralMD(db.Model):

    __tablename__ = 'leakGeneral'

    id = db.Column(db.String(32), primary_key=True)
    leaks = db.Column(db.String(100))

    leak_id = db.Column(db.String(32), db.ForeignKey('leakSource.id'))

    @property
    def serialized(self):
        return {
            'id': self.id,
            'leaks': self.leaks,
            'leak_id': self.leak_id
        }
