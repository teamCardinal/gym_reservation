from gym_reservation import bcrypt
from gym_reservation.models.user import User
from gym_reservation.models.gym_session import GymSession


class RouteHelpers():
    def login_password_is_valid(self, user, form):
        valid_password = False

        if user and bcrypt.check_password_hash(user.password, form.password.data):
           valid_password = True

        return valid_password

    def create_user_from_registration_form(self, form):
        user = User(
                username=form.username.data,
                email=form.email.data,
                gym=form.gym.data,
                membership_id=form.membership_id.data,
                password=form.password.data)
        password = user.hash_password(form.password.data)

        return user

    def convert_user_sessions_to_gym_sessions(self, user_sessions):
        gym_sessions = []
        for user_session in user_sessions:
            gym_session = GymSession.query.filter_by(id=user_session.session_id).first()
            gym_sessions.append(gym_session)

        return gym_sessions
