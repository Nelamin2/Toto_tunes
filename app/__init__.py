""" main application package """
from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from config import Config
from .models import  db, User

# db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # Specify the route for login page
login_manager.login_message_category = 'info'  # Flash message category

def create_app(config_class=Config):
    """ Create and configure the app """
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate = Migrate(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    # Test hashing
    test_password = "testpassword"
    hashed = bcrypt.generate_password_hash(test_password).decode('utf-8')
    print("Hashed Password:", hashed)

    # Test checking
    is_correct = bcrypt.check_password_hash(hashed, test_password)
    print("Password Match:", is_correct)  # Should return True


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
