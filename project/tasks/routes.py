from flask import Flask, Blueprint, jsonify, request, render_template, redirect

# Config
tasks_bp = Blueprint('tasks_bp', __name__, template_folder='templates')

# Routes
@tasks_bp.route('/', methods = ['GET'])
def index():
    """Show a user their list of tasks."""
    return render_template('index.html')


