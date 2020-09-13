from gym_reservation import bcrypt
from gym_reservation.models.user import User 


def login_password_is_valid(user, form):
    valid_password = False

    if user and bcrypt.check_password_hash(user.password, form.password.data):
        valid_password = True

    return valid_password

def create_user_from_registration_form(form):
    user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data)

    password = user.hash_password(form.password.data)

    return user
