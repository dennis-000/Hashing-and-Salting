import bcrypt

salt = bcrypt.gensalt()
print(f"Salt: {salt}")

password = "I1am2a3developer4"
hashed_pw = bcrypt.hashpw(password.encode(), salt)

print(f"Hashed Password with Salt: {hashed_pw}")