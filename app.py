from flask import Flask, redirect, render_template, url_for
from forms.register import RegistrationForm
app = Flask(__name__)

app.config["SECRET_KEY"] = "a4ee17a1c54ab04ae3a0950b8f86b5bf"

@app.route('/')
def hello_world():
    return "Hello, Team Cardinal!"

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for("home"))
    return render_template("register.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
