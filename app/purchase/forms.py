from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, SelectField, FloatField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Optional

class PurchaseRequestForm(FlaskForm):
    number = StringField("Request Number", validators=[DataRequired()])
    department_id = SelectField("Department", coerce=int)
    date_requested = DateField("Date Requested", validators=[DataRequired()])
    date_required = DateField("Date Required", validators=[Optional()])
    priority = SelectField("Priority", choices=[("low", "Low"), ("medium", "Medium"), ("high", "High")])
    description = TextAreaField("Description")
    items = TextAreaField("Items (JSON format)")
    submit = SubmitField("Submit")

class QuotationForm(FlaskForm):
    number = StringField("Quotation Number", validators=[DataRequired()])
    supplier_name = StringField("Supplier Name", validators=[DataRequired()])
    supplier_email = StringField("Supplier Email")
    supplier_phone = StringField("Supplier Phone")
    items = TextAreaField("Items (JSON format)")
    total_amount = FloatField("Total Amount")
    payment_terms = StringField("Payment Terms")
    delivery_time = StringField("Delivery Time")
    status = SelectField("Status", choices=[("en attente", "En attente"), ("accepted", "Accepted"), ("rejected", "Rejected")])
    submit = SubmitField("Submit")

class InvoiceForm(FlaskForm):
    number = StringField("Invoice Number", validators=[DataRequired()])
    quotation_id = SelectField("Quotation", coerce=int)
    status = SelectField("Status", choices=[("en attente", "En attente"), ("paid", "Paid")])
    due_date = DateField("Due Date")
    paid = SelectField("Paid", choices=[("no", "No"), ("yes", "Yes")])
    submit = SubmitField("Submit")

class DeliveryNoteForm(FlaskForm):
    number = StringField("Delivery Note Number", validators=[DataRequired()])
    purchase_request_id = SelectField("Purchase Request", coerce=int)
    received = SelectField("Received", choices=[("no", "No"), ("yes", "Yes")])
    date_received = DateField("Date Received", validators=[Optional()])
    validated_by = SelectField("Validated By", coerce=int)
    submit = SubmitField("Submit")