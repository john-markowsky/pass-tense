import pytest
import sqlite3
from passlib.hash import pbkdf2_sha256
from app.DB.database import register_user, verify_password, create_db_and_tables

# define test cases for create_db_and_tables
def test_create_db_and_tables():
    create_db_and_tables()
    conn = sqlite3.connect('app/DB/.DATA.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    assert ('users',) in tables

# define test cases for egister_user
def test_register_user():
    # register a new user
    result = register_user('John', 'Doe', 'john.doe12@example.com', 'password', 'user')

    # check if the user was created successfully
    assert result == {"success": "User created successfully"}

    # try to register the same user again
    result = register_user('John', 'Doe', 'john.doe@example.com', 'password', 'user')

    # check if an error was returned
    assert result == {"error": "Email is already taken"}

# define test cases for verify_password
def test_verify_password():
    # hash the password
    password_hash = pbkdf2_sha256.hash('password')

    # verify the password
    assert verify_password('password', password_hash) is True
    assert verify_password('wrong_password', password_hash) is False
