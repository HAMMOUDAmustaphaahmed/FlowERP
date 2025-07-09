from flask import Blueprint

department_bp = Blueprint("department", __name__, template_folder="templates", static_folder="static")

from . import routes