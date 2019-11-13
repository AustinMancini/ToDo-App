from flask import render_template

from . import tasks_bp


# Routes
@tasks_bp.route('/')
def index():
    return render_template('tasks/index.html')

