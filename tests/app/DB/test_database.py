import random
import string
import pytest
import sqlite3
from passlib.hash import pbkdf2_sha256
from app.DB.database import register_user, verify_password, create_db_and_tables

#Create random email to check for DB uniqueness
def generate_random_email():
    """Generates a random email address"""
    random_string = ''.join(random.choices(string.ascii_lowercase, k=10))
    domain = random.choice(['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com'])
    return f"{random_string}@{domain}"


# define test cases for create_db_and_tables
def test_create_db_and_tables():
    create_db_and_tables()
    conn = sqlite3.connect('app/DB/.DATA.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    assert ('users',) in tables

# define test cases for register_user
def test_register_user():
    # generate a random email address
    email = generate_random_email()

    # register a new user
    result = register_user('John', 'Doe', email, 'password', 'user')

    # check if the user was created successfully
    assert result == {"success": "User created successfully"}

    # try to register the same user again
    result = register_user('John', 'Doe', email, 'password', 'user')

    # check if an error was returned
    assert result == {"error": "Email is already taken"}

# define test cases for verify_password
def test_verify_password():
    # hash the password
    password_hash = pbkdf2_sha256.hash('password')

    # verify the password
    assert verify_password('password', password_hash) is True
    assert verify_password('wrong_password', password_hash) is False
