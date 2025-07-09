from flask import Blueprint

auth_bp = Blueprint("auth", __name__, template_folder="templates", static_folder="static")

from . import routes

from .models.user import User  # Assurez-vous que le chemin est correct

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
