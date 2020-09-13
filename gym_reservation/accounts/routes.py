from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required, logout_user

from gym_reservation import db
from gym_reservation.accounts.utils import convert_user_sessions_to_gym_sessions
from gym_reservation.models.gym_session import GymSession
from gym_reservation.models.user_session import UserSession

accounts = Blueprint("account", __name__)


@accounts.route("/account/<username>", methods=["GET"])
@login_required
def account(username):
    if username == current_user.username:
        return render_template("account.html", title="Account")
    else:
        return redirect(url_for("main.home"))

@accounts.route("/account/<username>/sessions", methods=["GET"])
@login_required
def user_sessions(username):
    if username == current_user.username:
        user_sessions = current_user.sessions
        gym_sessions = convert_user_sessions_to_gym_sessions(user_sessions)
        return render_template("user_sessions.html", title="MySessions", sessions=gym_sessions)
    else:
        return redirect(url_for("main.home"))

@accounts.route("/account/<username>/cancel-session/<id>")
def cancel_session(username, id):
    UserSession.query\
    .filter_by(user_id=current_user.id)\
    .filter_by(session_id=id)\
    .delete()

    db.session.commit()

    return redirect(url_for("account.user_sessions", username=current_user.username))

@accounts.route("/account/<username>/logout")
def logout(username):
    logout_user()
    return redirect(url_for("main.home"))
