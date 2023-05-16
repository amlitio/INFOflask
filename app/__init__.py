from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

from app.routes import index, login, signup, save, add_friend, collaborate, folder, ask_ai
