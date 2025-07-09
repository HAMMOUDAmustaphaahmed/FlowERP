# Utility functions for API blueprint

def serialize_model_list(model_list, fields):
    """
    Serialize a list of SQLAlchemy model instances to dicts with selected fields.
    """
    return [{field: getattr(obj, field) for field in fields} for obj in model_list]