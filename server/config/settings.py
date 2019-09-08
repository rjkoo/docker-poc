import os

DEBUG = True
HELLO = 'Hello, World! - (Find this string in the Main Config)'
SECRET_KEY='CHANGE_THIS_KEY'

# Get Environment Variables
PGUSER = os.environ['PGUSER']
PGPASSWORD = os.environ['PGPASSWORD']
PGHOST = os.environ['PGHOST']
PGPORT = os.environ['PGPORT']
PGDATABASE = os.environ['PGHOST']

PGURI = "postgresql://%s:%s@%s:%s/%s" %(PGUSER,
                                          PGPASSWORD,PGHOST,PGPORT,PGDATABASE)


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
MAIL_PASSWORD = 'awesomepassword'

# Celery.
RPASSWORD = os.environ['RPASSWORD']
REDIS_HOST = os.environ['REDIS_HOST']
REDIS_PORT = os.environ['REDIS_PORT']
broker_url_string = "redis://:%s@%s:%s/0" %(RPASSWORD, 
                                               REDIS_HOST,
                                               REDIS_PORT)
CELERY_BROKER_URL = 'redis://:devpassword@redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://:devpassword@redis:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_REDIS_MAX_CONNECTIONS = 5
