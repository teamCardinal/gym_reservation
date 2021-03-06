from datetime import datetime

from gym_reservation import db


class GymSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time_start = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    time_end = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    gym_id = db.Column(db.Integer, db.ForeignKey("gym.id"), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    spots_remaining = db.Column(db.Integer, nullable=False)
    activity = db.Column(db.String, nullable=False)


    def __repr__(self):
        return f"GymSession('{self.time_start}', '{self.time_end}', '{self.gym_id}', '{self.capacity}', '{self.spots_remaining}', '{self.activity}')"

    def __init__(self, time_start, time_end, gym_id, capacity, spots_remaining, activity ):
        self.time_start = time_start
        self.time_end = time_end
        self.gym_id = gym_id
        self.capacity = capacity
        self.spots_remaining = spots_remaining
        self.activity = activity
