from flask import flash, render_template, request, redirect, url_for
from flask_login import login_user

from gym_reservation import app, bcrypt, db 
from gym_reservation.forms.register import RegistrationForm
from gym_reservation.models.account import Account
from gym_reservation.models.user import User


@app.route('/', methods=['GET', 'POST'])
def home():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for("account"))
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

@app.route("/account", methods=["GET"])
def account():
    account = Account()
    return render_template("account.html", account=account)

