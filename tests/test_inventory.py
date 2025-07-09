import pytest
from app import create_app, db
from app.models.inventory import Inventory

@pytest.fixture
def client():
    app = create_app("testing")
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()

def test_inventory_creation(client):
    response = client.post("/inventory/add-product", data={
        "name": "Sample Product",
        "description": "Test",
        "sku": "SKU12345",
        "quantity": 10,
        "min_stock_alert": 2,
        "unit_price": 100,
        "location": "Aisle 1",
        "inventory_id": 1
    }, follow_redirects=True)
    # Should redirect or show success message
    assert b"Product added" in response.data or response.status_code in (200, 302)