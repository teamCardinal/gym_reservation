from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

from gym_reservation.models.user import User


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


class RegistrationForm(FlaskForm):
    username = StringField(
            "Username", 
            validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField(
            "Email",
            validators=[DataRequired(), Email()])

    password = PasswordField(
            "Password",
            validators=[DataRequired(), Length(min=8)])

    confirm_password = PasswordField(
            "Confirm Password",
            validators=[DataRequired(), EqualTo("password")])

    submit = SubmitField("Sign Up")


    def validate_username(self, username):

        user = User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError("That username is taken. Please choose a different one.")

    def validate_email(self, email):

        user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError("That email is taken. Please use a different one.")
