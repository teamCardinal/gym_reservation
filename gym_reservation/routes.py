from flask import flash, render_template, redirect, url_for
from flask_login import current_user, login_required, login_user, logout_user

from gym_reservation import app, db
from gym_reservation.forms.register import RegistrationForm
from gym_reservation.forms.login import LoginForm
from gym_reservation.helpers.route_helpers import RouteHelpers
from gym_reservation.models.user import User
from gym_reservation.models.gym import Gym
from gym_reservation.models.gym_session import GymSession
from gym_reservation.models.user_session import UserSession

route_helpers = RouteHelpers()

@app.route("/home", methods=["GET", "POST"])
@app.route('/', methods=['GET', 'POST'])
def home():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if route_helpers.login_password_is_valid(user, form):
            login_user(user)
            return redirect(url_for("account", username=current_user.username))
        else:
            flash("Login Unsuccessful. Please check username and password")

    return render_template('home.html', title="Home - Login", form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = route_helpers.create_user_from_registration_form(form)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in')
        return redirect(url_for("home"))

    return render_template("register.html", title="Register", form=form)

@app.route("/sessions", methods=["GET", "POST"])
def gym_sessions():
    sessions = GymSession.query.all()
    gyms_and_sessions = db.session.query(GymSession).join(Gym)
    return render_template("sessions.html", title="Sessions", sessions=gyms_and_sessions)

@app.route("/register_session/<id>")
def register_session(id):
    session = GymSession.query.filter_by(id=id).first()
    print(session)
    db.session.add(session)
    db.session.commit()
    return redirect(url_for("gym_sessions"))

@app.route("/cancel_session/<id>")
def cancel_session(id):
    db.session.query(UserSession).filter(session_id=id).delete()
    session.commit()

    return redirect(url_for("user_sessions"))

@app.route("/account/<username>", methods=["GET"])
@login_required
def account(username):
    if username == current_user.username:
        return render_template("account.html", title="Account")
    else:
        return redirect(url_for("home"))

@app.route("/account/<username>/sessions", methods=["GET"])
@login_required
def user_sessions(username):
    if username == current_user.username:
        user_sessions = current_user.sessions
        print(user_sessions)
        gym_sessions = route_helpers.convert_user_sessions_to_gym_sessions(user_sessions)
        return render_template("user_sessions.html", title="MySessions", sessions=gym_sessions)
    else:
        return redirect(url_for("home"))

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))
