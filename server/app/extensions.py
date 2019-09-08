from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_seasurf import SeaSurf

db = SQLAlchemy()
mail = Mail()
csrf = SeaSurf()

