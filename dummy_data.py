from gym_reservation import db

class DummyDataGym:

    dummy_gym_1 = Gym("SomeTimes Fitness", "100 Universal City Plaza, Universal City, CA 91608", "123-456-7890", "gym1@fakemail.com")
    dummy_gym_2 = Gym("SomeTimes Fitness", "1600 Pennsylvania Avenue NW, Washington, DC 20500", "123-456-7890", "gym2@fakemail.com")
    dummy_gym_3 = Gym("SomeTimes Fitness", "11 W 53rd St, New York, NY 10019", "123-456-7890", "gym3@fakemail.com")
    dummy_gym_4 = Gym("SomeTimes Fitness", "719 Wisconsin St, Cawker City, KS 67430", "123-456-7890", "gym4@fakemail.com")
    dummy_gym_5 = Gym("SomeTimes Fitness","702 SW 8th St, Bentonville, AR 72712", "123-456-7890", "gym5@fakemail.com")

class DummyDataGymSession:
    dummy_gym_session_1 = GymSession()
    dummy_gym_session_2 = GymSession()
    dummy_gym_session_3 = GymSession()
    dummy_gym_session_4 = GymSession()
    dummy_gym_session_5 = GymSession()

class DummyDataUser:
    dummy_user_1 = User("joeflex", "joe@fakemail.com", "SomeTimes Fitness", "001", "ilovebears")
    dummy_user_2 = User("nancymuscle", "nancy@fakemail.com", "SomeTimes Fitness", "002", "ilovecats")
    dummy_user_3 = User("steveripped", "steve@fakemail.com", "SomeTimes Fitness", "003", "iloverhinos")
    dummy_user_4 = User("jilljacked", "jill@fakemail.com", "SomeTimes Fitness", "004", "iloveorcas")
    dummy_user_5 = User("sambench600", "sam@fakemail.com", "SomeTimes Fitness", "005", "ilovesloths")

class DummyDataUserSession:
    dummy_user_session_1 = UserSession(001,)
    dummy_user_session_2 = UserSession(002,)
    dummy_user_session_3 = UserSession(003,)
    dummy_user_session_4 = UserSession(004,)
    dummy_user_session_5 = UserSession(005,)


