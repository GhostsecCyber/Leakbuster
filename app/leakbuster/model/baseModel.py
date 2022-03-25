from datetime import datetime
from app.leakbuster import db
from app.leakbuster.crypt import encrypt, decrypt
from sqlalchemy.orm.collections import InstrumentedList
import uuid


def generate_uuid():
    return uuid.uuid4().hex


blacklist = ['id', '_sa_instance_state', 'password', 'created', 'updated', 'leak_id', 'email_id']


class BaseModel:
    id = db.Column(db.String(32), primary_key=True, default=generate_uuid())
    created = db.Column(db.DateTime, default=datetime.now)
    updated = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def commit(self):
        db.session.close_all()
        for k, v in self.__dict__.items():
            if k not in blacklist:
                if isinstance(v, InstrumentedList) and v != []:
                    for item in v:
                        for x, y in item.__dict__.items():
                            if x not in blacklist:
                                item.__setattr__(x, encrypt(y))
                else:
                    self.__setattr__(k, encrypt(v))
        db.session.add(self)
        db.session.commit()
        return

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def read(self):
        for k, v in self.__dict__.items():
            if k not in blacklist:
                self.__setattr__(k, decrypt(v))
