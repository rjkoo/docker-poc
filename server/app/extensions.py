from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_seasurf import SeaSurf
from flask_login import LoginManager
db = SQLAlchemy()
mail = Mail()
csrf = SeaSurf()
login_manager = LoginManager()

