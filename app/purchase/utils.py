# Utility functions for purchase blueprint

def get_pending_requests():
    from app.models.purchase import PurchaseRequest
    return PurchaseRequest.query.filter_by(status='en attente').all()

def get_accepted_quotations():
    from app.models.purchase import Quotation
    return Quotation.query.filter_by(status='accepted').all()

def get_paid_invoices():
    from app.models.purchase import Invoice
    return Invoice.query.filter_by(paid=True).all()