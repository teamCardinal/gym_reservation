from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from gym_reservation.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = "main.home"

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from gym_reservation.accounts.routes import accounts
    from gym_reservation.main.routes import main 
    from gym_reservation.sessions.routes import sessions 
    app.register_blueprint(accounts)
    app.register_blueprint(main)
    app.register_blueprint(sessions)

    return app
