import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app
from app.models.database import get_db, Base
import uuid
import time

# Create test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="session")
def setup_database():
    """Create database tables once per test session"""
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(autouse=True)
def cleanup_database():
    """Clean up database before each test"""
    db = TestingSessionLocal()
    try:
        # Delete all users before each test to ensure clean state
        from app.models.user import User

        db.query(User).delete()
        db.commit()
        yield
    finally:
        db.close()


@pytest.fixture(scope="function")
def db_session():
    """Create a fresh database session for each test"""
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def test_client():
    """Override the get_db dependency with test session"""

    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()


def generate_unique_email():
    """Generate a unique email for testing"""
    timestamp = str(int(time.time() * 1000))
    return f"test_{uuid.uuid4().hex[:8]}_{timestamp}@example.com"


def test_read_root(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_create_user(test_client):
    user_data = {"name": "Test User", "email": generate_unique_email(), "age": 25}
    response = test_client.post("/users/", json=user_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == user_data["name"]
    assert data["email"] == user_data["email"]
    assert data["age"] == user_data["age"]
    assert "id" in data


def test_read_users(test_client):
    # Create a user first
    user_data = {"name": "Test User 2", "email": generate_unique_email(), "age": 30}
    test_client.post("/users/", json=user_data)

    # Get users
    response = test_client.get("/users/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_read_user(test_client):
    # Create a user first
    user_data = {"name": "Test User 3", "email": generate_unique_email(), "age": 35}
    create_response = test_client.post("/users/", json=user_data)
    user_id = create_response.json()["id"]

    # Get user by ID
    response = test_client.get(f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
    assert data["name"] == user_data["name"]


def test_update_user(test_client):
    # Create a user first
    user_data = {"name": "Test User 4", "email": generate_unique_email(), "age": 40}
    create_response = test_client.post("/users/", json=user_data)
    user_id = create_response.json()["id"]

    # Update user
    update_data = {"name": "Updated User", "email": generate_unique_email(), "age": 45}
    response = test_client.put(f"/users/{user_id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == update_data["name"]
    assert data["age"] == update_data["age"]


@pytest.mark.skip(reason="Delete user test is currently skipped")
def test_delete_user(test_client):
    # Create a user first
    user_data = {"name": "Test User 5", "email": generate_unique_email(), "age": 50}
    create_response = test_client.post("/users/", json=user_data)
    user_id = create_response.json()["id"]

    # Delete user
    response = test_client.delete(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "User deleted successfully"}

    # Verify user is deleted
    get_response = test_client.get(f"/users/{user_id}")
    assert get_response.status_code == 404
