from flask import request, redirect
from app import app, db
from app.models.friend import Friend
from flask_login import login_required, current_user

@app.route("/add-friend", methods=["POST"])
@login_required
def add_friend():
  friend_username = request.form.get("friend_username")
  friend = Friend(name=friend_username, user=current_user)
  db.session.add(friend)
  db.session.commit()
  return redirect("/")
