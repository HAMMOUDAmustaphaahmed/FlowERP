from app import db
from .base import BaseModel

class Inventory(BaseModel):
    __tablename__ = 'inventories'

    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False)
    products = db.relationship('Product', backref='inventory', lazy=True)
    custom_columns = db.Column(db.JSON)  # For custom attributes