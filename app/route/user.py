from flask import Blueprint
from flask import render_template

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/')
def home_page():
    return render_template('index.html')