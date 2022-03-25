from app.leakbuster import db
from app.leakbuster.model import *
import os


class LeakGeneralMD(db.Model, BaseModel):

    __tablename__ = 'leakGeneral'

    leaks = db.Column(db.String(3072))

    leak_id = db.Column(db.String(32), db.ForeignKey('leakSource.id'))

    @property
    def serialized(self):
        self.read()
        return {
            'id': self.id,
            'leaks': self.leaks,
            'leak_id': self.leak_id,
            'created': self.created,
            'updated': self.updated
        }

    def delete(self):
        self.read()
        os.remove(f"{self.leaks}")
        super(LeakGeneralMD, self).delete()
