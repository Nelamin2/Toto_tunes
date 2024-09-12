import sys
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_redis import FlaskRedis
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
redis_store = FlaskRedis()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app(config_filename=None):

    # Add the directory containing 'auth' module to the Python path
    sys.path.append(os.path.join(os.path.dirname(__file__), 'auth'))

    # Register blueprints
    from auth.routes import auth as auth_blueprint
    from game.routes import game as game_blueprint

    app = Flask(__name__)
        
    # Load configurations
    app.config['SECRET_KEY'] = 'thisisasecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
        
    # Initialize extensions with the app
    db.init_app(app)

    migrate.init_app(app, db)
    redis_store.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    login_manager.login_message_category = 'info'

    
    # Register blueprints   

    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(main_blueprint, url_prefix='/main')
    app.register_blueprint(profile_blueprint, url_prefix='/profile')
    app.register_blueprint(game_blueprint, url_prefix='/game')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)