from flask import render_template, request, redirect, url_for
from . import users_bp
from project import db


# Routes
@users_bp.route('/login')
def login():
    return render_template('users/login.html')
