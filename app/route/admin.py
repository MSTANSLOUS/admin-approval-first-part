from flask import Blueprint
from flask import render_template

from app.model.user import User
from app.model.user import database

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route('/admin')
def admin():
    all_users = User.query.all()
    return render_template("admin_approval_side.html", users=all_users)