from flask import render_template, request, redirect
from flask_login import login_user
from app import app, db
from app.models.user import User

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect('/')
    return render_template("login.html")
