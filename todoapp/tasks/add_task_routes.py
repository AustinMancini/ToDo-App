from flask import Flask, Blueprint, jsonify, request, render_template, redirect

# Setup ToDo landing page Blueprint
tasks_bp = Blueprint('tasks_bp', __name__)

# Routes
@tasks_bp.route('/add_task', methods = ['GET'])
def add_task():
    """Add an item to the ToDo list."""
    if request.method == 'GET':
        return render_template('index.html')


