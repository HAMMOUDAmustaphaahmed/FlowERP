from app import db
from .base import BaseModel

class Department(BaseModel):
    __tablename__ = 'departments'

    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)
    users = db.relationship('User', backref='department', lazy=True)
    inventories = db.relationship('Inventory', backref='department', lazy=True)