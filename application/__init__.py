import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_admin import Admin
from config import config

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s [in %(pathname)s %(lineno)s]')
db = SQLAlchemy()
admin_flask = Admin(name="code_snippets")
moment = Moment()


def create_app(config_name):
    app = Flask(__name__)
    app.logger.info(f"current config is {config[config_name]}")
    app.config.from_object(config[config_name])

    db.init_app(app)
    admin_flask.init_app(app)
    moment.init_app(app)

    with app.app_context():
        db.create_all()

        from .main import main_bp
        app.register_blueprint(main_bp)

        from .admin import admin_bp
        app.register_blueprint(admin_bp)

        from .api_v1 import api_v1_bp
        app.register_blueprint(api_v1_bp)

    return app
