from flask import Blueprint, render_template

# Config
users_bp = Blueprint('users_bp', __name__, template_folder='template')


# Routes
@users_bp.route('/login')
def login():
    return render_template('login.html')