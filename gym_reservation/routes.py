from flask import flash, render_template, request, redirect, url_for
from flask_login import current_user, login_required, login_user, logout_user

from gym_reservation import app, bcrypt, db
from gym_reservation.forms.register import RegistrationForm
from gym_reservation.forms.login import LoginForm
from gym_reservation.models.user import User
from gym_reservation.models.gym import Gym
from gym_reservation.models.gym_session import GymSession

@app.route('/', methods=['GET', 'POST'])
def home():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for("account", username=current_user.username))
        else:
            flash("Login Unsuccessful. Please check username and password")

    return render_template('home.html', form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(
                username=form.username.data,
                email=form.email.data,
                gym=form.gym.data,
                membership_id=form.membership_id.data,
                password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in')
        return redirect(url_for("home"))
    return render_template("register.html", form=form)


@app.route("/sessions", methods=["GET", "POST"])
def display_list():
    gym = Gym()
    gym_session = GymSession()
    return render_template("sessions.html", gym=gym, gym_session=gym_session)


@app.route("/account/<username>", methods=["GET"])
@login_required
def account(username):
    if username == current_user.username:
        return render_template("account.html")
    else:
        return redirect(url_for("home"))


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))
