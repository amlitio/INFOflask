from app import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)  # New field
    password = db.Column(db.String(128))
    folders = db.relationship('Folder', backref='user', lazy='dynamic')  # New relationship

    def check_password(self, password):
        return check_password_hash(self.password, password)
