from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class DepartmentForm(FlaskForm):
    name = StringField("Department Name", validators=[DataRequired()])
    description = TextAreaField("Description")
    company_id = SelectField("Company", coerce=int)
    submit = SubmitField("Save")