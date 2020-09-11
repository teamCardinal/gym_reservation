from flask import render_template, request, redirect, url_for

from gym_reservation import app
from gym_reservation.forms.register import RegistrationForm
from gym_reservation.models.account import Account


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
        return redirect(url_for("home"))
    return render_template("register.html", form=form)

@app.route("/account", methods=["GET"])
def account():
    account = Account()
    return render_template("account.html", account=account)

