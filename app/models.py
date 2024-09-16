""" Models for the application"""
from datetime import datetime
from flask_login import UserMixin
#from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
#from flask_bcrypt import Bcrypt
#initilize db object
from flask_argon2 import Argon2

#create an instance of the PasswordHasher
#ph = PasswordHasher()
db = SQLAlchemy()
argon2= Argon2()

class User(db.Model, UserMixin):
    """User model for authentication.

    Args:
        db (object): db object from app/__init__.py
        UserMixin (object): UserMixin object from flask_login

    Returns:
        object: User object with email, password_hash, and children attributes
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)  # Keep password_hash to match the database column
    children = db.relationship('ChildProfile', backref='parent', lazy=True)
    def __repr__(self):
        return f"User('{self.email}')"

    def set_password(self, password):
        """Hashes the password and stores it using Argon2."""  
        self.password_hash = argon2.generate_password_hash(password)

    def check_password(self, password):
        """Checks if the provided password matches the stored hash using Argon2."""
        return argon2.check_password_hash(self.password_hash, password)

# Child profile model
class ChildProfile(db.Model):
    """ Child profile model
    args:
        db (object): db object from app/__init__.py
        Returns:
        object: ChildProfile object"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    scores = db.relationship('Score', backref='child', lazy=True)

    def __repr__(self):
        return f"ChildProfile('{self.username}', '{self.age}', '{self.gender}')"

# Category model
class Category(db.Model):
    """ Category model

    Args:
        db (object): db object from app/__init__.py

    Returns:
        object: Category object with name, icon, and elements
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    icon = db.Column(db.String(100), nullable=False)
    elements = db.relationship('Element', backref='category', lazy=True)

    def __repr__(self):
        return f"Category('{self.name}')"

# Element model
class Element(db.Model):
    """ Element model
    
    Args:
        db (object): db object from app/__init__.py
        Returns:  element object with image_file, audio_file, category_id, and date_added"""
    id = db.Column(db.Integer, primary_key=True)
    image_file = db.Column(db.String(100), nullable=False)
    audio_file = db.Column(db.String(100), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        """ Return element object as string"""
        return f"Element('{self.image_file}', '{self.audio_file}', '{self.category.name}')"

# Score model
class Score(db.Model):
    """ Score model
    Args:
        db (object): db object from app/__init__.py
        Returns:    Score object with child_id, score, and timestamp"""
    id = db.Column(db.Integer, primary_key=True)
    child_id = db.Column(db.Integer, db.ForeignKey('child_profile.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Score('{self.child.username}', '{self.score}', '{self.timestamp}')"
