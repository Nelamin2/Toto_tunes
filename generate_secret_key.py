""" Generate a secure random key for Flask app """
import secrets

# Generate a secure random key
secret_key = secrets.token_hex(32)
print(secret_key)
