import sqlite3
from passlib.hash import pbkdf2_sha256

def create_db_and_tables():
    """Create the database and the necessary tables if they do not already exist"""
    conn = sqlite3.connect('app/DB/.DATA.db')
    cursor = conn.cursor()

    # create users table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            email TEXT,
            password_hash TEXT,
            user_type TEXT
        )
        """
    )

    conn.commit()
    conn.close()

def hash_password(password):
    """Hashes the password using the pbkdf2_sha256 algorithm"""
    return pbkdf2_sha256.hash(password)

def verify_password(password, password_hash):
    """Verifies the password against the hash"""
    return pbkdf2_sha256.verify(password, password_hash)

def register_user(first_name, last_name, email, password, user_type):
    """Registers a new user in the database"""
    conn = sqlite3.connect('app/DB/.DATA.db')
    cursor = conn.cursor()

    # Check if email is already taken
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    existing_user = cursor.fetchone()
    if existing_user:
        conn.close()
        return {"error": "Email is already taken"}

    # hash the password
    password_hash = hash_password(password)

    # insert the new user
    cursor.execute(
        """
        INSERT INTO users (first_name, last_name, email, password_hash, user_type)
        VALUES (?, ?, ?, ?, ?)
        """,
        (first_name, last_name, email, password_hash, user_type)
    )

    # commit the transaction
    conn.commit()

    # close the connection
    conn.close()

    return {"success": "User created successfully"}

create_db_and_tables()