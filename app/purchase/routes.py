from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from . import purchase_bp
from .forms import PurchaseRequestForm, QuotationForm, InvoiceForm, DeliveryNoteForm
from app.models.purchase import PurchaseRequest, Quotation, Invoice, DeliveryNote
from app import db

@purchase_bp.route("/purchase/requests")
@login_required
def requests_list():
    requests = PurchaseRequest.query.all()
    return render_template("purchase/requests.html", requests=requests)

@purchase_bp.route("/purchase/requests/add", methods=["GET", "POST"])
@login_required
def add_request():
    form = PurchaseRequestForm()
    if form.validate_on_submit():
        purchase_request = PurchaseRequest(
            number=form.number.data,
            department_id=form.department_id.data,
            user_id=current_user.id,
            date_requested=form.date_requested.data,
            date_required=form.date_required.data,
            priority=form.priority.data,
            description=form.description.data,
            items=form.items.data,
            status="en attente"
        )
        db.session.add(purchase_request)
        db.session.commit()
        flash("Purchase request created.", "success")
        return redirect(url_for("purchase.requests_list"))
    return render_template("purchase/add_request.html", form=form)

@purchase_bp.route("/purchase/quotations")
@login_required
def quotations():
    quotations = Quotation.query.all()
    return render_template("purchase/quotations.html", quotations=quotations)

@purchase_bp.route("/purchase/invoices")
@login_required
def invoices():
    invoices = Invoice.query.all()
    return render_template("purchase/invoices.html", invoices=invoices)

@purchase_bp.route("/purchase/delivery-notes")
@login_required
def delivery_notes():
    notes = DeliveryNote.query.all()
    return render_template("purchase/delivery_notes.html", notes=notes)