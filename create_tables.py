"""  Script to create the necessary tables in the database. """
from app import create_app, db  # Import the app and db from your app module
import logging

# Enable logging for SQLAlchemy engine to track SQL queries
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

def create_tables():
    """Function to drop and create the necessary tables in the database."""
    app = create_app()  # Create the app
    with app.app_context():
        print("Dropping tables...")
        db.drop_all()  # Drop all existing tables
        print("Tables dropped.")
        print("Creating tables...")
        db.create_all()  # Create all tables based on the models
        print("Tables created.")

if __name__ == "__main__":
    create_tables()
