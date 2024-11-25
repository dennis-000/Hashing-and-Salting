import sqlite3
import bcrypt

# Step 1: Create Database and Users Table
def create_database():
    conn = sqlite3.connect("user_accounts.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password BLOB NOT NULL
        )
    """)
    conn.commit()
    conn.close()
    print("Database and users table created successfully.")

# Add User to Database -- Register
def add_user():
    #if I want to get the user input
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    
    connection = sqlite3.connect("user_accounts.db")
    cursor = connection.cursor()

    # Hash and salt the password
    salt = bcrypt.gensalt()  # Generate a salt
    hashed_password = bcrypt.hashpw(password.encode(), salt)  # Hash the password
    
    print(f"Hashed and salted password for '{username}': {hashed_password}")


    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        connection.commit()
        print(f"User '{username}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"Error: Username '{username}' already exists.")
    connection.close()

# Verify User Login
def verify_user():
    
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    conn = sqlite3.connect("user_accounts.db")
    cursor = conn.cursor()
    
    # Retrieve the stored hashed password for the given username
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    
    if result:
        stored_hashed_password = result[0]  # This will be in bytes
        
        # Correct comparison without encoding the stored password
        if bcrypt.checkpw(password.encode(), stored_hashed_password):
            print("Login successful!")
            return True
        else:
            print("Invalid username or password.")
            return False
    else:
        print("User not found.")
        return False


# --- MAIN PROGRAM ---
if __name__ == "__main__":
    create_database()  # Step 1: Create the database and table

    # Add some users -- Registering the user
    # Just call the function 
    add_user()
    # add_user("opoku", "securepassword123")
    # add_user("antwi", "myp@ssw0rd!")

    # Verify users -- Logging in the user with correct username and password used to register
    verify_user()
    # verify_user("opoku", "securepassword123") 
    # verify_user("antwi", "myp@ssw0rd!")    
