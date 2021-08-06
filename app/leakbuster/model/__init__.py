from app.leakbuster import db
from werkzeug.security import generate_password_hash, check_password_hash
import uuid


class UserMD(db.Model):

    __tablename__ = 'leakbuster_user'

    id = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    roles = db.Column(db.String(5), nullable=False)
    phone = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    callback = db.Column(db.String(100), unique=True, nullable=False)
    company = db.Column(db.String(300), nullable=False)
    cdomain = db.Column(db.String(300), unique=True, nullable=False)
    site = db.Column(db.String(300), unique=True, nullable=False)

    @property
    def serialized(self):
        return {
            'id': self.id,
            'username': self.name,
            'role': self.roles,
            'callback': self.callback,
            'phone': self.phone,
            'email': self.email,
            'company': self.company,
            'cdomain': self.cdomain,
            'site': self.site
        }

    def hash_password(self, password):
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)


class LeakSourceMD(db.Model):

    __tablename__ = 'leakbuster_leakSource'

    id = db.Column(db.String(32), primary_key=True, default=uuid.uuid4().hex)
    url = db.Column(db.String(200), unique=True)
    date = db.Column(db.String(200))
    descri = db.Column(db.String(400))
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
            'descri': self.descri,
            'author': self.author,
            'general': self.general,
            'leak_emails': self.leak_emails,
            'leak_password': self.leak_password

        }


class LeakGeneralMD(db.Model):

    __tablename__ = 'leakbuster_leakGeneral'

    id = db.Column(db.String(32), primary_key=True, default=uuid.uuid4().hex)
    leaks = db.Column(db.String(100))

    leak_id = db.Column(db.String(32), db.ForeignKey('leakbuster_leakSource.id'))

    @property
    def serialized(self):
        return {
            'id': self.id,
            'leaks': self.leaks,
            'leak_id': self.leak_id
        }


class LeakEmailMD(db.Model):

    __tablename__ = 'leakbuster_leakEmail'

    id = db.Column(db.String(32), primary_key=True, default=uuid.uuid4().hex)
    email = db.Column(db.String(500))

    leak_id = db.Column(db.String(32), db.ForeignKey('leakbuster_leakSource.id'))
    leak_password = db.relationship('LeakPasswordMD')

    @property
    def serialized(self):
        return {
            'id': self.id,
            'email': self.email,
            'leak_id': self.leak_id,
            'leak_password': self.leak_password
        }


class LeakPasswordMD(db.Model):

    __tablename__ = 'leakbuster_leakPassword'

    id = db.Column(db.String(32), primary_key=True, default=uuid.uuid4().hex)
    password = db.Column(db.String(600))

    leak_id = db.Column(db.String(32), db.ForeignKey('leakbuster_leakSource.id'))
    email_id = db.Column(db.String(32), db.ForeignKey('leakbuster_leakEmail.id'))

    @property
    def serialized(self):
        return {
            'id': self.id,
            'password': self.password,
            'leak_id': self.leak_id,
            'email_id': self.email_id
        }


class LeakWarningMD(db.Model):

    __tablename__ = 'leakbuster_leakWarning'

    id = db.Column(db.String(32), primary_key=True, default=uuid.uuid4().hex)
    warning_type = db.Column(db.String(6), nullable=False)
    comp_domain = db.Column(db.String(300), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(500))

    leak_id = db.Column(db.String(32), db.ForeignKey('leakbuster_leakSource.id'))

    @property
    def serialized(self):
        return {
            'id': self.id,
            'warning_type': self.warning_type,
            'comp_domain': self.comp_domain,
            'password': self.password,
            'email': self.email,
            'leak_id': self.leak_id
        }


class ValidatedEmailsMD(db.Model):

    __tablename__ = 'leakbuster_validatedEmails'

    id = db.Column(db.String(32), primary_key=True, default=uuid.uuid4().hex)
    valid_email = db.Column(db.Boolean, nullable=False)

    email_id = db.Column(db.String(32), db.ForeignKey('leakbuster_leakEmail.id'))

    @property
    def serialized(self):
        return {
            'id': self.id,
            'valid_email': self.valid_email,
            'mail_id': self.email_id
        }


class LeakCPFCNPJ(db.Model):

    __tablename__ = 'leakbuster_leakCPFCNPJ'

    id = db.Column(db.String(32), primary_key=True, default=uuid.uuid4().hex)
    CPF_CNPJ = db.Column(db.String(100), nullable=False)

    leak_id = db.Column(db.String(32), db.ForeignKey('leakbuster_leakSource.id'))

    @property
    def serialized(self):
        return {
            'id': self.id,
            'cpf_cnpj': self.warning_type,
            'leak_id': self.leak_id
        }
