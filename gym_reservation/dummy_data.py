import datetime
import random

from gym_reservation.models.gym import Gym
from gym_reservation.models.gym_session import GymSession
from gym_reservation.models.user import User
from gym_reservation.models.user_session import UserSession
from gym_reservation import db


def populate_dummy_database():
    DummyDataGym.populate_gym_data()
    DummyDataGymSession.populate_gym_session_data()
    DummyDataUser.populate_user_data()
    DummyDataUserSession.populate_user_session_data()


class DummyDataGym:

    dummy_gym_1 = Gym("SomeTimes Fitness", "100 Universal City Plaza, Universal City, CA 91608", "123-456-7891",
                      "gym1@fakemail.com")
    dummy_gym_2 = Gym("0 Hour Fitness", "1600 Pennsylvania Avenue NW, Washington, DC 20500", "123-456-7892",
                      "gym2@fakemail.com")
    dummy_gym_3 = Gym("Asteroid Fitness", "11 W 53rd St, New York, NY 10019", "123-456-7893",
                      "gym3@fakemail.com")
    dummy_gym_4 = Gym("Mold's Gym", "719 Wisconsin St, Cawker City, KS 67430", "123-456-7894",
                      "gym4@fakemail.com")
    dummy_gym_5 = Gym("NYC Fitness", "702 SW 8th St, Bentonville, AR 72712", "123-456-7895",
                      "gym5@fakemail.com")

    dummy_gyms = [dummy_gym_1, dummy_gym_2, dummy_gym_3, dummy_gym_4, dummy_gym_5]

    @staticmethod
    def populate_gym_data():

        for a_gym in DummyDataGym.dummy_gyms:
            db.session.add(a_gym)
            db.session.commit()


class DummyDataGymSession:

    @staticmethod
    def generate_random_session():
        activities = ["weight room", "cardio equipment", "indoor track", "yoga studio"]
        date_pair = (DummyDataGymSession.generate_random_date(), DummyDataGymSession.generate_random_date())

        time_start = min(date_pair)
        time_end = max(date_pair)
        gym_id = random.randrange(1, 6)
        capacity = random.randrange(1, 100)
        spots_remaining = random.randrange(0, capacity + 1)
        activity = activities[random.randrange(0, len(activities))] 

        return GymSession(time_start, time_end, gym_id, capacity, spots_remaining, activity)

    @staticmethod
    def generate_random_date():
        year = random.randrange(2020, 2078)
        month = random.randrange(1, 13)
        day = random.randrange(1, 28)
        hour = random.randrange(0, 24)
        minute = random.randrange(0, 60, 15)

        date = datetime.datetime(year, month, day, hour, minute)

        return date

    # dummy_gym_session_1 = GymSession(datetime.datetime(2020, 9, 13, 7), datetime.datetime(2020, 9, 13, 8),
    #                                  1, 15, 6, "weight room")
    # dummy_gym_session_2 = GymSession(datetime.datetime(2020, 9, 13, 12), datetime.datetime(2020, 9, 13, 13),
    #                                  2, 20, 16, "cardio equipment")
    # dummy_gym_session_3 = GymSession(datetime.datetime(2020, 9, 13, 18, 30), datetime.datetime(2020, 9, 13, 19, 30),
    #                                  3, 10, 4, "indoor track")
    # dummy_gym_session_4 = GymSession(datetime.datetime(2020, 9, 13, 8, 30), datetime.datetime(2020, 9, 13, 9, 30),
    #                                  4, 6, 3, "yoga studio")
    # dummy_gym_session_5 = GymSession(datetime.datetime(2020, 9, 13, 16, 30), datetime.datetime(2020, 9, 13, 17, 30),
    #                                  5, 10, 5, "weight room")

    # dummy_gym_sessions = [dummy_gym_session_1, dummy_gym_session_2, dummy_gym_session_3, dummy_gym_session_4,
    #                       dummy_gym_session_5]

    @staticmethod
    def populate_gym_session_data():
        for i in range(10, 100):
            session = DummyDataGymSession.generate_random_session()
            db.session.add(session)
            print(session)
        
        db.session.commit()

        # for a_gym_session in DummyDataGymSession.dummy_gym_sessions:
        #     db.session.add(a_gym_session)
        #     db.session.commit()


class DummyDataUser:
    dummy_user_1 = User("joeflex", "joe@fakemail.com",  "ilovebears")
    dummy_user_2 = User("nancymuscle", "nancy@fakemail.com", "ilovecats")
    dummy_user_3 = User("steveripped", "steve@fakemail.com", "iloverhinos")
    dummy_user_4 = User("jilljacked", "jill@fakemail.com", "iloveorcas")
    dummy_user_5 = User("sambench600", "sam@fakemail.com", "ilovesloths")

    dummy_users = [dummy_user_1, dummy_user_2, dummy_user_3, dummy_user_4, dummy_user_5]

    @staticmethod
    def populate_user_data():

        for a_user in DummyDataUser.dummy_users:
            a_user.hash_password(a_user.password)
            db.session.add(a_user)
            db.session.commit()


class DummyDataUserSession:
    dummy_user_session_1 = UserSession(1, 4)
    dummy_user_session_2 = UserSession(2, 3)
    dummy_user_session_3 = UserSession(3, 5)
    dummy_user_session_4 = UserSession(4, 2)
    dummy_user_session_5 = UserSession(5, 1)

    dummy_user_sessions = [dummy_user_session_1, dummy_user_session_2, dummy_user_session_3, dummy_user_session_4,
                           dummy_user_session_5]

    @staticmethod
    def populate_user_session_data():

        for a_user_session in DummyDataUserSession.dummy_user_sessions:
            db.session.add(a_user_session)
            db.session.commit()
