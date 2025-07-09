from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from . import inventory_bp
from .forms import InventoryForm, ProductForm
from app.models.inventory import Inventory
from app.models.product import Product
from app import db

@inventory_bp.route("/inventory/dashboard")
@login_required
def dashboard():
    inventories = Inventory.query.all()
    return render_template("inventory/dashboard.html", inventories=inventories)

@inventory_bp.route("/inventory/inventories")
@login_required
def inventories():
    inventories = Inventory.query.all()
    return render_template("inventory/inventories.html", inventories=inventories)

@inventory_bp.route("/inventory/products")
@login_required
def products():
    products = Product.query.all()
    return render_template("inventory/products.html", products=products)

@inventory_bp.route("/inventory/product/<int:product_id>")
@login_required
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template("inventory/product_detail.html", product=product)

@inventory_bp.route("/inventory/add-product", methods=["GET", "POST"])
@login_required
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(
            name=form.name.data,
            description=form.description.data,
            sku=form.sku.data,
            quantity=form.quantity.data,
            min_stock_alert=form.min_stock_alert.data,
            unit_price=form.unit_price.data,
            location=form.location.data,
            inventory_id=form.inventory_id.data
        )
        db.session.add(product)
        db.session.commit()
        flash("Product added successfully.", "success")
        return redirect(url_for("inventory.products"))
    return render_template("inventory/add_product.html", form=form)

@inventory_bp.route("/inventory/edit-product/<int:product_id>", methods=["GET", "POST"])
@login_required
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)
    form = ProductForm(obj=product)
    if form.validate_on_submit():
        form.populate_obj(product)
        db.session.commit()
        flash("Product updated successfully.", "success")
        return redirect(url_for("inventory.product_detail", product_id=product.id))
    return render_template("inventory/edit_product.html", form=form, product=product)

@inventory_bp.route("/inventory/history")
@login_required
def history():
    # Placeholder for inventory history logic
    return render_template("inventory/history.html")