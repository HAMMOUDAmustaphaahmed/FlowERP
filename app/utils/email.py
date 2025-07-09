from flask_mail import Message
from flask import current_app
from app import mail

def send_email(subject, recipients, text_body, html_body=None):
    msg = Message(subject, recipients=recipients, body=text_body, html=html_body)
    mail.send(msg)

def send_reset_email(user):
    token = user.get_reset_token()
    send_email(
        "Password Reset Request",
        [user.email],
        f"To reset your password, visit the following link: {current_app.url_for('auth.reset_password', token=token, _external=True)}",
        html_body=f"<p>To reset your password, visit the following link: <a href='{current_app.url_for('auth.reset_password', token=token, _external=True)}'>Reset Password</a></p>"
    )