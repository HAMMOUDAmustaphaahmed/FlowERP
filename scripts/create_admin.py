"""
Script to create an admin user.
"""
from app import create_app, db
from app.models.user import User

app = create_app()

with app.app_context():
    username = input("Admin username: ")
    email = input("Admin email: ")
    password = input("Admin password: ")

    admin = User(username=username, email=email, role='admin', is_active=True)
    admin.set_password(password)
    db.session.add(admin)
    db.session.commit()
    print(f"Admin user {username} created.")