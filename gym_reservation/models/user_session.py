import datetime

from gym_reservation import db


class UserSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    session_id = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return f"UserSession('{user_id}', '{session_id}')"
