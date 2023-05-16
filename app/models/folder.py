from app import db

class Folder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    informations = db.relationship('Information', backref='folder', lazy='dynamic')
