import os

from sqlalchemy import exc

from gym_reservation import create_app, db, dummy_data

app = create_app()

@app.before_first_request
def create_tables():
    from gym_reservation.models.user import User
    db.create_all()

    try:
        dummy_data.populate_dummy_database()
    except exc.IntegrityError:
        db.session.rollback()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='127.0.0.1', port=port)
