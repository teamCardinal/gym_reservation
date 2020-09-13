from gym_reservation.models.gym_session import GymSession


def convert_user_sessions_to_gym_sessions(user_sessions):
    gym_sessions = []
    for user_session in user_sessions:
        gym_session = GymSession.query.filter_by(id=user_session.session_id).first()
        gym_sessions.append(gym_session)

    return gym_sessions
