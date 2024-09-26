""" Initialize the Flask application. """
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from config import Config
from .models import db, User  # Import your models

# Initialize login manager
login_manager = LoginManager()

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    
    # Use an absolute path for the SQLite database
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, '../site.db')
    app.config['SECRET_KEY'] = '13bb2a29bc310ad29aee814ab700698936c459511f664d96f077bc9421e47a0c'
    
    # Initialize extensions
    db.init_app(app)  # Initialize the database with the app
    login_manager.init_app(app)  # Initialize the login manager
    Migrate(app, db)  # Initialize migrations for database management

    # Register blueprints
    from .auth.routes import auth  # Assuming auth blueprint exists
    from .game.routes import game  # Assuming game blueprint exists
    app.register_blueprint(auth)
    app.register_blueprint(game)
    
    return app

# Flask-Login user loader callback
@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.query.get(int(user_id))
