from app.DB.models import User, UserCreate

def test_user_model():
    user = User(id=1, first_name="John", last_name="Doe", email="johndoe@example.com", user_type="admin")
    assert user.id == 1
    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.email == "johndoe@example.com"
    assert user.user_type == "admin"
    assert user.dict() == {"id": 1, "first_name": "John", "last_name": "Doe", "email": "johndoe@example.com", "user_type": "admin"}

def test_user_create_model():
    user_create = UserCreate(first_name="John", last_name="Doe", email="johndoe@example.com", user_type="admin", password="password", confirm_password="password")
    assert user_create.first_name == "John"
    assert user_create.last_name == "Doe"
    assert user_create.email == "johndoe@example.com"
    assert user_create.user_type == "admin"
    assert user_create.password == "password"
    assert user_create.confirm_password == "password"
    assert user_create.dict() == {"first_name": "John", "last_name": "Doe", "email": "johndoe@example.com", "user_type": "admin", "password": "password", "confirm_password": "password"}
