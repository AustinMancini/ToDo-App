from flask import Flask
from flask_sqlalchemy import SQLAlchemy


""" Configuration """

# Instances
db = SQLAlchemy()


# Create Flask Application
def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)

    db.init_app(app)
    register_blueprints(app)
    
    return app

def register_blueprints(app):
    """Register each Blueprint with Flask application instance (app)."""
    from project.tasks import tasks_bp
    from project.users import users_bp

    app.register_blueprint(tasks_bp)
    app.register_blueprint(users_bp)
    