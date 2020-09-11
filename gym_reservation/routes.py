from flask import render_template, request, redirect, url_for

from gym_reservation import app, bcrypt, db 
from gym_reservation.forms.register import RegistrationForm
from gym_reservation.models.account import Account
from gym_reservation.models.user import User


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        pass
    else:
        return render_template('home.html')

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

