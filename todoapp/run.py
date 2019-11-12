from flask import Flask


def create_app(config_filename):
    app = Flask(__name__)

    app.config.from_object(config_filename)

    from tasks.add_task_routes import tasks_bp
    app.register_blueprint(tasks_bp)

    return app


if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)
