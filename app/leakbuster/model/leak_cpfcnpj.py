from app.leakbuster import db
from app.leakbuster.model import *


class LeakCPFCNPJ(db.Model):

    __tablename__ = 'leakCPFCNPJ'

    id = db.Column(db.String(32), primary_key=True)
    CPF_CNPJ = db.Column(db.String(100), nullable=False)

    leak_id = db.Column(db.String(32), db.ForeignKey('leakSource.id'))

    @property
    def serialized(self):
        return {
            'id': self.id,
            'cpf_cnpj': self.warning_type,
            'leak_id': self.leak_id
        }
