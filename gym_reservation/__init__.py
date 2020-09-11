from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "a4ee17a1c54ab04ae3a0950b8f86b5bf"

from gym_reservation import routes

