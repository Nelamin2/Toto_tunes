from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
test_password = "testpassword"
hashed = bcrypt.generate_password_hash(test_password).decode('utf-8')
print("Hashed Password:", hashed)

is_correct = bcrypt.check_password_hash(hashed, test_password)
print("Password Match:", is_correct)  # Should return True