import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_redis import FlaskRedis
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from models import User
from app.auth.routes import auth as auth_blueprint
from app.game.routes import game as game_blueprint

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
redis_store = FlaskRedis()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Load configurations
    app.config['SECRET_KEY'] = 'thisisasecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['REDIS_URL'] = 'redis://localhost:6379/0'
    app.config['BCRYPT_LOG_ROUNDS'] = 12
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SESSION_PERMANENT'] = True
    app.config['SESSION_USE_SIGNER'] = True
    app.config['SESSION_KEY_PREFIX'] = 'session'
    app.config['SESSION_COOKIE_NAME'] = 'session'
    app.config['SESSION_COOKIE_DOMAIN'] = None
    app.config['SESSION_COOKIE_PATH'] = '/'
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['SESSION_COOKIE_SECURE'] = False
    app.config['SESSION_COOKIE_SAMESITE'] = None
    app.config['SESSION_REFRESH_EACH_REQUEST'] = True

    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)
    redis_store.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'  # Adjust this to match your actual login view
    login_manager.login_message_category = 'info'

    # Register blueprints with the app
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(game_blueprint, url_prefix='/game')

    return app
