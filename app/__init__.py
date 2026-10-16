from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        from app import routes
        from app.models import Kid, Task, Reward
        db.create_all()

        app.register_blueprint(routes.bp)

    return app
