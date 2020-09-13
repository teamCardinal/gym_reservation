from gym_reservation import create_app, dummy_data

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

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
