# Utility functions for admin blueprint

def get_all_companies():
    from app.models.company import Company
    return Company.query.all()

def get_all_users():
    from app.models.user import User
    return User.query.all()

def get_all_departments():
    from app.models.department import Department
    return Department.query.all()