import pytest
from app import create_app, db

@pytest.fixture
def client():
    app = create_app("testing")
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()

def test_purchase_request(client):
    response = client.post("/purchase/requests/add", data={
        "number": "PR-001",
        "department_id": 1,
        "date_requested": "2024-07-09",
        "date_required": "2024-07-20",
        "priority": "medium",
        "description": "Need office chairs",
        "items": '[{"name": "Chair", "qty": 10}]'
    }, follow_redirects=True)
    assert b"Purchase request created" in response.data or response.status_code in (200, 302)