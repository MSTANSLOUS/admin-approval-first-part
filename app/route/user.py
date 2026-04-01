from flask import Blueprint
from flask import render_template
from flask import request

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/')
def home_page():
    return render_template('index.html')

@user_bp.route('/login_page', methods=['GET', 'POST'])
def login_page():
    name  = request.form.get('user_name')
    email = request.form.get('user_email')

    print(name)
    print(email)

    return render_template('index.html')