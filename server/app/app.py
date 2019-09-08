from flask import Flask
from app.blueprints.page import page
from app.blueprints.contact import contact
from app.extensions import (
    db,
    mail,
    csrf
)


def create_app(settings_override=None):
    """
    Create a flask app using the app factory pattern

    :return A flask app instance.
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    if settings_override:
        app.config.update(settings_override)

    # Register App components via blueprints
    app.register_blueprint(page)
    app.register_blueprint(contact)

    # Initialize Extensions
    extensions(app)


    @app.route('/hello')
    def index():
        """
        Render a Hello World response.
        For test purposes only; Remove this route and function when you begin
        development.

        :return Flask response
        """

        return app.config['HELLO']

    return app

def extensions(app):
    """
    Register extenstions on the application instance

    :param app: Flask Application instance
    :return: None
    """

    mail.init_app(app)
    db.init_app(app)
    csrf.init_app(app)

    return None
