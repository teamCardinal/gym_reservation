from gym_reservation import db


class Gym(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    parent_gym = db.Column(db.String(20), nullable=False)
    location_X = db.Column(db.Float, nullable=False)
    location_Y = db.Column(db.Float, nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"Gym('{self.name}', '{self.parent_gym}', '{self.address}', '{self.phone}', '{self.email}')"
