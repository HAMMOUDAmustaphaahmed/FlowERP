from functools import wraps
from flask import redirect, url_for, flash
from flask_login import current_user

def admin_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != "admin":
            flash("Admin access required.", "danger")
            return redirect(url_for("main.index"))
        return func(*args, **kwargs)
    return decorated_view