# Utility functions for inventory blueprint

def get_low_stock_products():
    from app.models.product import Product
    return Product.query.filter(Product.quantity <= Product.min_stock_alert).all()

def get_inventory_products(inventory_id):
    from app.models.product import Product
    return Product.query.filter_by(inventory_id=inventory_id).all()