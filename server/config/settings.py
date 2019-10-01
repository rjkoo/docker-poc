import os

DEBUG = True
HELLO = 'Hello, World! - (Find this string in the Main Config)'
SECRET_KEY='CHANGE_THIS_KEY'



# Flask-Seasurf: Cross Site Request Forgery Protection
CSRF_DISABLE = False

# Flask-Mail.
MAIL_DEFAULT_SENDER = 'contact@local.host'
MAIL_SERVER = 'smtp.gmail.com' # Mail server address
MAIL_PORT = 587                # Dependent upon mail server being used
MAIL_USE_TLS = True            # ^
MAIL_USE_SSL = False
MAIL_USERNAME = 'you@gmail.com' # This and line below are overwritten with
                                # instance/settings.py config file
MAIL_PASSWORD = 'supersecurepasswordgoeshere'

# Redis
REDIS_PASSWORD = os.environ['REDIS_PASSWORD']
REDIS_HOST = os.environ['REDIS_HOST']
REDIS_PORT = os.environ['REDIS_PORT']

# Celery
CELERY_BROKER_URL = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/0"
CELERY_RESULT_BACKEND = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/0"
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_REDIS_MAX_CONNECTIONS = 5


# SQLAlchemy
PG_USER = os.environ['PG_USER']
PG_PASSWORD = os.environ['PG_PASSWORD']
PG_HOST = os.environ['PG_HOST']
PG_PORT = os.environ['PG_PORT']
PG_DATABASE = os.environ['PG_HOST']

db_uri = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DATABASE}"
SQLAlCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Seed User data
SEED_ADMIN_EMAIL = 'dev@localhost.com'
SEED_ADMIN_PASSWORD = 'devpassword'
#REMEMBER_COOKIE_DURATION = timedelta(days=90)
