from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from . import main_bp

@main_bp.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))
    return render_template("index.html")

@main_bp.route("/dashboard")
@login_required
def dashboard():
    # Optionally, pass summary data to the dashboard
    return render_template("main/dashboard.html")

@main_bp.route("/profile")
@login_required
def profile():
    return render_template("main/profile.html")

@main_bp.route("/settings", methods=["GET", "POST"])
@login_required
def settings():
    # Add logic for managing user settings
    return render_template("main/settings.html")