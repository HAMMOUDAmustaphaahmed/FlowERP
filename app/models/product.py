from app import db
from .base import BaseModel

class Product(BaseModel):
    __tablename__ = 'products'

    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text)
    sku = db.Column(db.String(64), unique=True, nullable=False)
    quantity = db.Column(db.Integer, default=0)
    min_stock_alert = db.Column(db.Integer, default=0)
    unit_price = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(128))
    image = db.Column(db.String(256))
    inventory_id = db.Column(db.Integer, db.ForeignKey('inventories.id'), nullable=False)
    custom_data = db.Column(db.JSON)