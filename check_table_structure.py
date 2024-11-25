import sqlite3

def check_table_structure():
    conn = sqlite3.connect("user_accounts.db")
    cursor = conn.cursor()

    # Fetch the table schema
    cursor.execute("PRAGMA table_info(users)")
    columns = cursor.fetchall()
    print("Table Structure:")
    for column in columns:
        print(column)

    conn.close()

check_table_structure()
