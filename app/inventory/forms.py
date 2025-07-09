from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class InventoryForm(FlaskForm):
    name = StringField("Inventory Name", validators=[DataRequired()])
    description = TextAreaField("Description")
    department_id = SelectField("Department", coerce=int)
    submit = SubmitField("Save")

class ProductForm(FlaskForm):
    name = StringField("Product Name", validators=[DataRequired()])
    description = TextAreaField("Description")
    sku = StringField("SKU", validators=[DataRequired()])
    quantity = IntegerField("Quantity", validators=[DataRequired(), NumberRange(min=0)])
    min_stock_alert = IntegerField("Min Stock Alert", validators=[NumberRange(min=0)])
    unit_price = FloatField("Unit Price", validators=[DataRequired()])
    location = StringField("Location")
    inventory_id = SelectField("Inventory", coerce=int)
    submit = SubmitField("Save")