from app import db
from .base import BaseModel

class PurchaseRequest(BaseModel):
    __tablename__ = 'purchase_requests'

    number = db.Column(db.String(32), unique=True, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date_requested = db.Column(db.DateTime, nullable=False)
    date_required = db.Column(db.DateTime)
    priority = db.Column(db.String(16))
    description = db.Column(db.Text)
    items = db.Column(db.JSON)
    status = db.Column(db.String(32), default='en attente')

class Quotation(BaseModel):
    __tablename__ = 'quotations'

    number = db.Column(db.String(32), unique=True, nullable=False)
    supplier_name = db.Column(db.String(128), nullable=False)
    supplier_email = db.Column(db.String(128))
    supplier_phone = db.Column(db.String(32))
    items = db.Column(db.JSON)
    total_amount = db.Column(db.Float)
    payment_terms = db.Column(db.String(128))
    delivery_time = db.Column(db.String(64))
    status = db.Column(db.String(32), default='en attente')

class Invoice(BaseModel):
    __tablename__ = 'invoices'

    number = db.Column(db.String(32), unique=True, nullable=False)
    quotation_id = db.Column(db.Integer, db.ForeignKey('quotations.id'))
    status = db.Column(db.String(32), default='en attente')
    due_date = db.Column(db.DateTime)
    paid = db.Column(db.Boolean, default=False)
    reminders_sent = db.Column(db.Integer, default=0)

class DeliveryNote(BaseModel):
    __tablename__ = 'delivery_notes'

    number = db.Column(db.String(32), unique=True, nullable=False)
    purchase_request_id = db.Column(db.Integer, db.ForeignKey('purchase_requests.id'))
    received = db.Column(db.Boolean, default=False)
    date_received = db.Column(db.DateTime)
    validated_by = db.Column(db.Integer, db.ForeignKey('users.id'))