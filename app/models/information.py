from app import db

class Information(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    folder_id = db.Column(db.Integer, db.ForeignKey('folder.id'))
