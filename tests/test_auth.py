import pytest
from app import create_app, db
from app.models.user import User

@pytest.fixture
def client():
    app = create_app("testing")
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()

def test_signup_and_login(client):
    # Sign up a new user
    response = client.post("/signup", data={
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpassword",
        "confirm_password": "testpassword"
    }, follow_redirects=True)
    assert b"Account created" in response.data

    # Login with new user
    response = client.post("/login", data={
        "username": "testuser",
        "password": "testpassword"
    }, follow_redirects=True)
    assert b"Dashboard" in response.data