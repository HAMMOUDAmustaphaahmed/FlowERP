from flask import jsonify, request, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import api_bp
from app.models.user import User
from app.models.company import Company
from app.models.department import Department
from app.models.inventory import Inventory
from app.models.product import Product
from app.models.purchase import PurchaseRequest, Quotation, Invoice, DeliveryNote
from app import db

# Example: Get current user's info
@api_bp.route("/me", methods=["GET"])
@jwt_required()
def get_me():
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)
    return jsonify({
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "role": user.role,
        "company_id": user.company_id,
        "department_id": user.department_id,
    })

@api_bp.route("/companies", methods=["GET"])
@jwt_required()
def get_companies():
    companies = Company.query.all()
    return jsonify([{
        "id": c.id,
        "name": c.name,
        "email": c.email,
        "address": c.address,
        "phone": c.phone
    } for c in companies])

@api_bp.route("/departments", methods=["GET"])
@jwt_required()
def get_departments():
    departments = Department.query.all()
    return jsonify([{
        "id": d.id,
        "name": d.name,
        "description": d.description,
        "company_id": d.company_id
    } for d in departments])

@api_bp.route("/inventories", methods=["GET"])
@jwt_required()
def get_inventories():
    inventories = Inventory.query.all()
    return jsonify([{
        "id": inv.id,
        "name": inv.name,
        "description": inv.description,
        "department_id": inv.department_id
    } for inv in inventories])

@api_bp.route("/products", methods=["GET"])
@jwt_required()
def get_products():
    products = Product.query.all()
    return jsonify([{
        "id": p.id,
        "name": p.name,
        "sku": p.sku,
        "quantity": p.quantity,
        "unit_price": p.unit_price,
        "inventory_id": p.inventory_id
    } for p in products])

@api_bp.route("/purchase/requests", methods=["GET"])
@jwt_required()
def get_purchase_requests():
    requests = PurchaseRequest.query.all()
    return jsonify([{
        "id": r.id,
        "number": r.number,
        "status": r.status,
        "department_id": r.department_id,
        "user_id": r.user_id
    } for r in requests])

# Add other API endpoints as needed, following this pattern.