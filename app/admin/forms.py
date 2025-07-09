from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired, Email

class CompanyForm(FlaskForm):
    name = StringField("Company Name", validators=[DataRequired()])
    address = StringField("Address")
    email = StringField("Email", validators=[Email()])
    phone = StringField("Phone")
    fiscal_id = StringField("Fiscal ID")
    registration_number = StringField("Registration Number")
    website = StringField("Website")
    submit = SubmitField("Save")

class DepartmentForm(FlaskForm):
    name = StringField("Department Name", validators=[DataRequired()])
    description = StringField("Description")
    company_id = SelectField("Company", coerce=int)
    submit = SubmitField("Save")

class UserForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[Email()])
    role = SelectField("Role", choices=[("admin", "Admin"), ("user", "User")])
    is_active = BooleanField("Active")
    submit = SubmitField("Save")