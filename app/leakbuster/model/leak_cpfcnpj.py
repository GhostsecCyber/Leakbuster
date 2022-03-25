from app.leakbuster import db
from app.leakbuster.model import *


class LeakCPFCNPJ(db.Model, BaseModel):

    __tablename__ = 'leakCPFCNPJ'

    CPF_CNPJ = db.Column(db.String(3072), nullable=False)

    leak_id = db.Column(db.String(32), db.ForeignKey('leakSource.id'))

    @property
    def serialized(self):
        self.read()
        return {
            'id': self.id,
            'cpf_cnpj': self.warning_type,
            'leak_id': self.leak_id,
            'created': self.created,
            'updated': self.updated
        }
