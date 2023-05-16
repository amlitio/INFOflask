from flask import request, redirect
from app import app
from app.models.folder import Folder
from app.models.friend import Friend
from flask_login import login_required, current_user

@app.route("/collaborate", methods=["POST"])
@login_required
def collaborate():
  folder_name = request.form.get("folder_name")
  folder = Folder.query.filter_by(name=folder_name).first()
  if folder:
    friends = Friend.query.filter_by(user=current_user).all()
    # Do something with friends here. For now, we'll just print them.
    print(friends)
  return redirect("/folder/" + folder_name)
