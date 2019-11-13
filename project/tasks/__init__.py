from flask import Blueprint
tasks_bp = Blueprint('tasks_bp', __name__, template_folder='templates')

from . import routes