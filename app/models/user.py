from app import db
from .base import BaseModel
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(BaseModel, UserMixin):
    __tablename__ = 'users'

    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    password_hash = db.Column(db.String(128), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    role = db.Column(db.String(32), default='user')  # admin, user, etc.
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    last_login_at = db.Column(db.DateTime)
    failed_logins = db.Column(db.Integer, default=0)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)