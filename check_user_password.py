import sqlite3

conn = sqlite3.connect("user_accounts.db")
cursor = conn.cursor()

# Query the database to see the stored password hashes
cursor.execute("SELECT username, password FROM users")
rows = cursor.fetchall()

# Print out the usernames and hashed passwords
for row in rows:
    print(f"Username: {row[0]}, Password: {row[1]}")

conn.close()
