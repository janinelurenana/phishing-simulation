from flask import Flask, render_template, request, redirect, url_for, session
from secrets import token_hex

app = Flask(__name__)
app.secret_key = token_hex(32)

# Dummy account for the classroom simulation
DEMO_USERNAME = "student.demo"
DEMO_PASSWORD = "DemoPass123!"

@app.route("/email")
def email():
    return render_template("email.html")
    
@app.route("/")
def home():
    return redirect(url_for("email"))

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def process_login():
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")

    # Store the submitted dummy credentials temporarily
    session["username"] = username
    session["password"] = password

    return redirect(url_for("awareness"))

@app.route("/awareness")
def awareness():
    username = session.get("username", "")
    password = session.get("password", "")

    return render_template(
        "awareness.html",
        username=username,
        password=password
    )

if __name__ == "__main__":
    app.run(debug=True)