from datetime import datetime

from gym_reservation import db
from gym_reservation.models.gym import Gym
from gym_reservation.models.gym_session import GymSession


def convert_user_sessions_to_gym_sessions(user_sessions):
    gym_sessions = []

    registered_session_ids = [s.session_id for s in user_sessions]

    gyms_and_sessions = db.session\
    .query(GymSession)\
    .filter(GymSession.time_start >= datetime.now())\
    .join(Gym)

    for user_session in user_sessions:
        gym_session = db.session\
        .query(GymSession)\
        .filter_by(id=user_session.session_id)\
        .filter(GymSession.time_end >= datetime.now())\
        .first()

        if gym_session:
            gym_session = gym_session.__dict__
            gym_session["name"] = Gym.query.filter_by(id=gym_session["gym_id"]).first().name

        gym_sessions.append(gym_session)

    gym_sessions = sorted(gym_sessions, key=lambda k: k["time_start"])

    return gym_sessions
