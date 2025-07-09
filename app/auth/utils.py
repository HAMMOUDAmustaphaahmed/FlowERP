from itsdangerous import URLSafeTimedSerializer
from flask import current_app, url_for
from app.utils.email import send_email

def generate_reset_token(user):
    s = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])
    return s.dumps(user.id, salt="reset-password")

def verify_reset_token(token, expiration=3600):
    s = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])
    try:
        user_id = s.loads(token, salt="reset-password", max_age=expiration)
    except Exception:
        return None
    from app.models.user import User
    return User.query.get(user_id)