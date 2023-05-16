from flask import Flask
from flask_login import LoginManager
from app.models.SQLAlchemy import db
from app.models import User  # assuming User is your user model

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from app.routes import index, login, signup, save, add_friend, collaborate, folder, ask_ai
