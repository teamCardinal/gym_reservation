from flask_login import UserMixin

from gym_reservation import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    gym = db.Column(db.String(20), nullable=False)
    membership_id = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    sessions = db.relationship("UserSession")

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.gym}', '{self.membership_id}')"

    def add_session(self, session):
        self.sessions.append(session)

    def remove_session(self, session):
        self.sessions.remove(session)

