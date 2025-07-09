# Utility functions for department blueprint

def get_departments_by_company(company_id):
    from app.models.department import Department
    return Department.query.filter_by(company_id=company_id).all()