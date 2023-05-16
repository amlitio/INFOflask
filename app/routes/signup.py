from flask import render_template, request, redirect
from app import app, db
from app.models.user import User
from werkzeug.security import generate_password_hash

@app.route("/signup", methods=["GET", "POST"])
def signup():
  if request.method == 'POST':
    username = request.form.get('username')
    password = generate_password_hash(request.form.get('password')) 
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return redirect('/login')
  return render_template("signup.html")
