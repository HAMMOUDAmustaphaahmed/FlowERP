from flask import Blueprint

purchase_bp = Blueprint("purchase", __name__, template_folder="templates", static_folder="static")

from . import routes