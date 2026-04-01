from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from app.model.user import User

from app.model.user import database

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/')
def home_page():
    return render_template('index.html')


@user_bp.route('/login_page', methods=['GET', 'POST'])
def login_page():
    name  = request.form.get('user_name')
    email = request.form.get('user_email')

    signing_user = User.query.filter_by(user_email=email).first()

    if signing_user:
        print("user exists {}".format(signing_user.user_name))

        if not signing_user.is_active:
            print("user {} not active".format(signing_user.user_name))
            return redirect(url_for('user_bp.home_page'))

        else:
            print("user {} is active".format(signing_user.user_name))
            return redirect(url_for('user_bp.landing_page'))

    else:
        print("user {} does not exist".format(signing_user.user_name))
        new_user = User(user_name=name, user_email=email, is_active=False)
        database.session.add(new_user)
        database.session.commit()
        return redirect(url_for('user_bp.home_page'))


@user_bp.route('/home_page')
def landing_page():
    return render_template('land_page.html')