""" This file is used to run the application"""
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Default Flask port is 5000
