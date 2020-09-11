from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "a4ee17a1c54ab04ae3a0950b8f86b5bf"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "home"

@app.before_first_request
def create_tables():
    from gym_reservation.models.user import User
    db.create_all()

from gym_reservation import routes
from gym_reservation.models.user import User
from gym_reservation.models.user_session import UserSession
from gym_reservation.models.gym import Gym
from gym_reservation.models.gym_session import GymSession

