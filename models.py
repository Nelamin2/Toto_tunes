from . import db
from flask_login import UserMixin
from datetime import datetime

# User model for authentication
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    scores = db.relationship('Score', backref='user', lazy=True)
    
    
    children = db.relationship('ChildProfile', backref='parent', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class BabyProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Category model to organize images into groups
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    images = db.relationship('Image', backref='category', lazy=True)

    def __repr__(self):
        return f"Category('{self.name}')"


# Image model to store images and corresponding audio
class Image(db.Model):
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
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)  # The score for correct matches
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Score('{self.user.username}', '{self.score}')"

