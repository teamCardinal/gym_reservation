import datetime

from gym_reservation import db


class UserSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    session_id = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return f"UserSession('{self.user_id}', '{self.session_id}')"
