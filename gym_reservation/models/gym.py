from gym_reservation import db


class Gym(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    sessions = db.relationship("GymSession")

    def __repr__(self):
        return f"Gym('{self.name}', '{self.address}', '{self.phone}', '{self.email}')"

    def __init__(self, name, address, phone, email):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
