# Instance specific configuration for FlowERP.
# This file should NOT be committed to version control with real secrets.

SECRET_KEY = "instance-specific-secret-key"
SQLALCHEMY_DATABASE_URI = "mysql://user:password@localhost/flowerp"
MAIL_USERNAME = "your-email@example.com"
MAIL_PASSWORD = "your-email-password"
JWT_SECRET_KEY = "instance-specific-jwt-secret"