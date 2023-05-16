from flask import request, redirect
from app import app, db
from app.models.folder import Folder
from app.models.information import Information
from flask_login import login_required

@app.route("/save", methods=["POST"])
@login_required
def save():
  information = request.form.get("information")
  folder_name = request.form.get("folder")
  folder = Folder.query.filter_by(name=folder_name).first()
  if folder:
    information = Information(content=information, folder=folder)
    db.session.add(information)
    db.session.commit()
  return redirect("/")
