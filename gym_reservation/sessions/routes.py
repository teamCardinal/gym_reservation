from datetime import datetime
from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user
from sqlalchemy.orm import load_only

from gym_reservation import db
from gym_reservation.models.gym import Gym
from gym_reservation.models.gym_session import GymSession
from gym_reservation.models.user_session import UserSession

sessions = Blueprint("sessions", __name__)


@sessions.route("/sessions", methods=["GET", "POST"])
def gym_sessions():
    gyms = Gym.query.all()

    user_sessions = db.session\
    .query(UserSession)\
    .filter(UserSession.user_id == current_user.id)\
    .all()

    registered_session_ids = [s.session_id for s in user_sessions]

    gyms_and_sessions = db.session\
    .query(GymSession)\
    .filter(~GymSession.id.in_(registered_session_ids))\
    .filter(GymSession.time_start >= datetime.now())\
    .filter(GymSession.spots_remaining > 0)\
    .join(Gym)

    return render_template("sessions.html", title="Sessions", sessions=gyms_and_sessions, gyms=gyms)

@sessions.route("/sessions/register-session/<id>")
def register_session(id):
    session = UserSession.query.filter_by(session_id=id).first()

    if not session:
        session = UserSession(user_id=current_user.id, session_id=id)
    else:
        session.user_id = current_user.id

    db.session.add(session)

    gym_session = GymSession.query.filter_by(id=id).first()

    if gym_session.spots_remaining >= 1:
        gym_session.spots_remaining -= 1

    db.session.commit()

    return redirect(url_for("sessions.gym_sessions"))
