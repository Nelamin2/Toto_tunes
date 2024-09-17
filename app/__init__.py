""" Main application package """
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from config import Config
from .models import db, User
from flask_argon2 import Argon2
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

login_manager = LoginManager()
migrate = Migrate()

def create_app():
    """ Create and configure the app """


    app = Flask(__name__)
    #app configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SECRET_KEY'] = '13bb2a29bc310ad29aee814ab700698936c459511f664d96f077bc9421e47a0c'


    # Initialize extensions
    db.init_app(app)
    #bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)  # Corrected variable name from 'migirate' to 'migrate'

    # Create database tables
    with app.app_context():
        db.create_all()

    # Import and register blueprints
    from .auth.routes import auth  # Blueprint imports
    from .game.routes import game
    app.register_blueprint(auth)
    app.register_blueprint(game)

    return app

# User loader callback for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    """ Load user by ID """
    return User.query.get(int(user_id))
