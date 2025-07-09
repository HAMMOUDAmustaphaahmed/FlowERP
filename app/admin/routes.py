from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from . import admin_bp

def admin_required(func):
    from functools import wraps
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != "admin":
            flash("Admin access required.", "danger")
            return redirect(url_for("main.index"))
        return func(*args, **kwargs)
    return decorated_view

@admin_bp.route("/admin/dashboard")
@login_required
@admin_required
def dashboard():
    return render_template("admin/dashboard.html")

@admin_bp.route("/admin/users")
@login_required
@admin_required
def users():
    # Add logic to retrieve users
    return render_template("admin/users.html")

@admin_bp.route("/admin/companies")
@login_required
@admin_required
def companies():
    # Add logic to retrieve companies
    return render_template("admin/companies.html")

@admin_bp.route("/admin/departments")
@login_required
@admin_required
def departments():
    # Add logic to retrieve departments
    return render_template("admin/departments.html")

@admin_bp.route("/admin/system-settings", methods=["GET", "POST"])
@login_required
@admin_required
def system_settings():
    # Add logic for system settings
    return render_template("admin/system_settings.html")