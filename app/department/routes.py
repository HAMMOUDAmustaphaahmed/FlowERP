from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from . import department_bp
from .forms import DepartmentForm
from app.models.department import Department
from app import db

@department_bp.route("/departments")
@login_required
def list_departments():
    departments = Department.query.all()
    return render_template("department/departments.html", departments=departments)

@department_bp.route("/departments/add", methods=["GET", "POST"])
@login_required
def add_department():
    form = DepartmentForm()
    if form.validate_on_submit():
        department = Department(
            name=form.name.data,
            description=form.description.data,
            company_id=form.company_id.data
        )
        db.session.add(department)
        db.session.commit()
        flash("Department created successfully.", "success")
        return redirect(url_for("department.list_departments"))
    return render_template("department/add_department.html", form=form)

@department_bp.route("/departments/edit/<int:department_id>", methods=["GET", "POST"])
@login_required
def edit_department(department_id):
    department = Department.query.get_or_404(department_id)
    form = DepartmentForm(obj=department)
    if form.validate_on_submit():
        form.populate_obj(department)
        db.session.commit()
        flash("Department updated successfully.", "success")
        return redirect(url_for("department.list_departments"))
    return render_template("department/edit_department.html", form=form, department=department)