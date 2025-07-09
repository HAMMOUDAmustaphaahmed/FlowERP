from flask import render_template, redirect, url_for, flash, request, session, current_app
from flask_login import login_user, logout_user, current_user, login_required
from . import auth_bp
from .forms import LoginForm, SignupForm, ForgotPasswordForm, ResetPasswordForm
from app.models.user import User
from app import db
from app.utils.email import send_reset_email

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            user.failed_logins = 0
            db.session.commit()
            return redirect(url_for("main.dashboard"))
        else:
            if user:
                user.failed_logins += 1
                db.session.commit()
            flash("Invalid username or password.", "danger")
    return render_template("auth/login.html", form=form)

@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data, 
            email=form.email.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            is_active=True
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Account created, please log in.", "success")
        return redirect(url_for("auth.login"))
    return render_template("auth/signup.html", form=form)

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "success")
    return redirect(url_for("auth.login"))

@auth_bp.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    form = ForgotPasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_reset_email(user)
            flash("Password reset instructions sent to your email.", "info")
        else:
            flash("No account found with that email.", "danger")
    return render_template("auth/forgot_password.html", form=form)

@auth_bp.route("/reset-password/<token>", methods=["GET", "POST"])
def reset_password(token):
    user = User.verify_reset_token(token)
    if not user:
        flash("This reset link is invalid or has expired.", "danger")
        return redirect(url_for("auth.forgot_password"))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash("Your password has been updated.", "success")
        return redirect(url_for("auth.login"))
    return render_template("auth/reset_password.html", form=form)