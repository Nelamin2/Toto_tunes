from . import db
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

# User model for authentication
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    
    # Relationship with ChildProfile (was BabyProfile)
    children = db.relationship('BabyProfile', backref='parent', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Child profile model (previously BabyProfile)
class BabyProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    
    # Reference to the parent user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # Relationship to the Score model
    scores = db.relationship('Score', backref='child', lazy=True)

    def __repr__(self):
        return f"ChildProfile('{self.username}', '{self.age}', '{self.gender}')"

# Category model to organize images into groups
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    
    # Relationship to images
    images = db.relationship('Image', backref='category', lazy=True)

    def __repr__(self):
        return f"Category('{self.name}')"

# Image model to store images and corresponding audio
class Element(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_file = db.Column(db.String(100), nullable=False)  # Path to image file
    audio_file = db.Column(db.String(100), nullable=False)  # Path to audio file
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    
    # Timestamp for when the image was added
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Image('{self.image_file}', '{self.audio_file}', '{self.category.name}')"

# Model to track user scores or progress
class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    # Foreign key linking to ChildProfile
    child_id = db.Column(db.Integer, db.ForeignKey('child_profile.id'), nullable=False)
    
    score = db.Column(db.Integer, nullable=False)  # The score for correct matches
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Score('{self.child.username}', '{self.score}', '{self.timestamp}')"


