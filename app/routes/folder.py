from flask import render_template
from app import app
from app.models.folder import Folder
from app.models.friend import Friend
from flask_login import login_required, current_user

@app.route("/folder/<folder_name>")
@login_required
def folder(folder_name):
  folder = Folder.query.filter_by(name=folder_name).first()
  if folder:
    information = folder.informations
    friends = Friend.query.filter_by(user=current_user).all()
    return render_template("folder.html", information=information, friends=friends)
  return redirect("/")
