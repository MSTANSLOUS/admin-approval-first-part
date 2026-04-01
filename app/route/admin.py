from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for

from app.model.user import User
from app.model.user import database

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route('/admin')
def admin():
    all_users = User.query.all()
    return render_template("admin_approval_side.html", users=all_users)

@admin_bp.route('/admin/active_deactivate/<int:user_id>', methods=['GET', 'POST'])
def active_deactivate(user_id):
    user = User.query.get(user_id)
    if not user.is_active:
        user.is_active = True
        database.session.commit()
        return redirect(url_for('admin_bp.admin'))
    else:
        user.is_active = False
        database.session.commit()
        return redirect(url_for('admin_bp.admin'))