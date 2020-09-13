from flask import Blueprint, flash, render_template, redirect, url_for
from flask_login import current_user, login_user 

from gym_reservation import db
from gym_reservation.main.forms import LoginForm, RegistrationForm
from gym_reservation.main.utils import create_user_from_registration_form, login_password_is_valid
from gym_reservation.models.user import User

main = Blueprint("main", __name__)


@main.route("/home", methods=["GET", "POST"])
@main.route('/', methods=['GET', 'POST'])
def home():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if login_password_is_valid(user, form):
            login_user(user)
            return redirect(url_for("account.account", username=current_user.username))
        else:
            flash("Login Unsuccessful. Please check username and password")

    return render_template('home.html', title="Home", form=form)

@main.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = create_user_from_registration_form(form)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in')
        return redirect(url_for("main.home"))

    return render_template("register.html", title="Register", form=form)
