from gym_reservation.models.gym import Gym
from gym_reservation.models.gym_session import GymSession


def convert_user_sessions_to_gym_sessions(user_sessions):
    gym_sessions = []

    for user_session in user_sessions:
        gym_session = GymSession.query.filter_by(id=user_session.session_id).first().__dict__
        gym_session["name"] = Gym.query.filter_by(id=gym_session["gym_id"]).first().name
        gym_sessions.append(gym_session)

    return gym_sessions
