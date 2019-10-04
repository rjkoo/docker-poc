from flask import Flask
from celery import Celery
from app.blueprints.page import page
from app.blueprints.contact import contact
from app.blueprints.user import user
from app.blueprints.plan_of_work import plans

# models
from app.blueprints.user.models import User
from app.blueprints.plan_of_work.models import ( 
        PlanOfWork,
        CriticalIssue
)


from app.extensions import (
    db,
    mail,
    csrf,
    login_manager
)

CELERY_TASK_LIST = [
    'app.blueprints.contact.tasks',
    'app.blueprints.user.tasks'
]

def create_celery_app(app=None):
    """
    Create a new Celery object and tie together the celery config to the app's
    config. Wrap all tasks in the context of the application.

    :param app: Flask app
    :return Celery app
    """

    app = app or create_app()

    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'],
                    include=CELERY_TASK_LIST)
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery


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
    app.register_blueprint(user)
    app.register_blueprint(plans)
    extensions(app)
    authentication(app, User)


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
    login_manager.init_app(app)

    return None


def authentication(app, user_model):
    """
    Initialize the Flask-login extension(mutates the app passed int).

    :param app: Flask application extention
    :param user_model: Model that contains the authentication information
    :type user_model: SQLAlchemy model
    :return: None
    """


    # user_loader - sets the callback for reloading a user from the session.
    # Take a user ID and return a user object, or None if the user doesn't exist
    @login_manager.user_loader
    def load_user(uid):
        return user_model.query.get(uid)

    @login_manager.token_loader
    def load_token(token):
        duration = app.config['REMEMBER_COOKIE_DURATION'].total_seconds()
        serializer = URLSafeTimedSerializer(app.secret_key)

        data = serializer.loads(token, max_age=duration)
        user_uid = data[0]

        return user_model.query.get(user_uid)


"""
    @login_manager.token_loader
    def load_token(token):
        duration = app.config['REMEMBER_COOKIE_DURATION'].total_seconds()
        serializer = URLSafeTimedSerializer(app.secret_key)

        data = serializer.loads(token, max_age=duration)
        user_uid = data[0]

        return user_model.query.get(user_uid)
"""
