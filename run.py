from gym_reservation import create_app, dummy_data

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=443)

    @app.before_first_request
    def create_tables():
        from gym_reservation.models.user import User
        db.create_all()
        # Wipe the DB and uncomment to get your fake data :)
        populate_dummy_database()

    def populate_dummy_database():
        DummyDataGym.populate_gym_data()
        DummyDataGymSession.populate_gym_session_data()
        DummyDataUser.populate_user_data()
        DummyDataUserSession.populate_user_session_data()
