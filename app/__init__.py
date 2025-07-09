import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_jwt_extended import JWTManager
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
mail = Mail()
jwt = JWTManager()
csrf = CSRFProtect()

def create_app(config_name=None):
    app = Flask(__name__, instance_relative_config=True)
    config_name = config_name or os.environ.get("FLASK_ENV", "default")
    app.config.from_object(f"config.{config_name.capitalize()}Config")
    app.config.from_pyfile("config.py", silent=True)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    mail.init_app(app)
    jwt.init_app(app)
    csrf.init_app(app)

    # Import and register blueprints
    from .auth import auth_bp
    from .main import main_bp
    from .admin import admin_bp
    from .inventory import inventory_bp
    from .purchase import purchase_bp
    from .department import department_bp
    from .api import api_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(inventory_bp)
    app.register_blueprint(purchase_bp)
    app.register_blueprint(department_bp)
    app.register_blueprint(api_bp, url_prefix="/api")

    return app