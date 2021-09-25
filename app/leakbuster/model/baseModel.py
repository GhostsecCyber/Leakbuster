from datetime import datetime
from app.leakbuster import db
import uuid


def generate_uuid():
    return uuid.uuid4().hex


class BaseModel:
    id = db.Column(db.String(32), primary_key=True, default=generate_uuid())
    created = db.Column(db.DateTime, default=datetime.now)
    updated = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
