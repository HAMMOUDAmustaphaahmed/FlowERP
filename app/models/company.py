from app import db
from .base import BaseModel

class Company(BaseModel):
    __tablename__ = 'companies'

    name = db.Column(db.String(255), nullable=False, unique=True)
    address = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    phone = db.Column(db.String(30))
    fiscal_id = db.Column(db.String(64))
    registration_number = db.Column(db.String(64))
    website = db.Column(db.String(128))
    users = db.relationship('User', backref='company', lazy=True)
    departments = db.relationship('Department', backref='company', lazy=True)