from app.models.user import User
from app.models.company import Company

def test_user_password():
    user = User(username="u", email="e", is_active=True)
    user.set_password("mypassword")
    assert user.check_password("mypassword")
    assert not user.check_password("wrongpassword")

def test_company_creation():
    company = Company(name="Test Inc", address="123 Test St", email="test@inc.com")
    assert company.name == "Test Inc"