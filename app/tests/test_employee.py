import pytest
from fastapi.testclient import TestClient
from main import app
from app.models.database import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.database import Base
import uuid
import time

# Create test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


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


@pytest.fixture
def employee_factory():
    """Factory fixture to create Employee instances"""
    from app.models.employee import Employee

    def create_employee(seniority=0):
        employee = Employee()
        employee.seniority = seniority
        return employee

    return create_employee


# TESTS UNITAIRES


def test_get_seniority_default_value(employee_factory):
    """Test get_seniority returns default seniority value"""
    employee = employee_factory()
    result = employee.get_seniority()

    assert result == 0


def test_get_seniority_custom_value(employee_factory):
    """Test get_seniority returns custom seniority value"""
    employee = employee_factory(seniority=5)
    result = employee.get_seniority()

    assert result == 5


def test_get_seniority_zero_value(employee_factory):
    """Test get_seniority returns zero when seniority is set to zero"""
    employee = employee_factory(seniority=0)
    result = employee.get_seniority()

    assert result == 0


def test_get_seniority_negative_value(employee_factory):
    """Test get_seniority handles negative seniority values"""
    employee = employee_factory(seniority=-1)
    result = employee.get_seniority()

    assert result == -1


def test_get_seniority_edge_case(employee_factory):
    """Test get_seniority with maximum reasonable seniority value"""
    employee = employee_factory(seniority=50)
    result = employee.get_seniority()

    assert result == 50


# TESTS D'INTEGRATION - Route GET /employees/list


def test_list_employees_empty(test_client, setup_database):
    """Test GET /employees/list returns empty list when no employees exist"""
    # Arrange - database is empty (cleaned by cleanup_database fixture)

    # Act
    response = test_client.get("/employees/list")

    # Assert
    assert response.status_code == 200
    assert response.json() == []


def test_list_employees_single_employee(test_client, setup_database, db_session):
    """Test GET /employees/list returns single employee"""
    # Arrange - Create a user and an employee
    from app.models.user import User
    from app.models.employee import Employee

    user = User(name="Test User", email=generate_unique_email(), age=30)
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)

    employee = Employee(full_name="John Doe", seniority=5, user_id=user.id)
    db_session.add(employee)
    db_session.commit()

    # Act
    response = test_client.get("/employees/list")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["full_name"] == "John Doe"
    assert data[0]["seniority"] == 5
    assert data[0]["user_id"] == user.id


def test_list_employees_multiple_employees(test_client, setup_database, db_session):
    """Test GET /employees/list returns multiple employees"""
    # Arrange - Create multiple users and employees
    from app.models.user import User
    from app.models.employee import Employee

    users_data = [
        {"name": "User 1", "email": generate_unique_email(), "age": 25},
        {"name": "User 2", "email": generate_unique_email(), "age": 30},
        {"name": "User 3", "email": generate_unique_email(), "age": 35},
    ]

    for user_data in users_data:
        user = User(**user_data)
        db_session.add(user)
    db_session.commit()

    users = db_session.query(User).all()

    employees_data = [
        {"full_name": "John Doe", "seniority": 5, "user_id": users[0].id},
        {"full_name": "Jane Smith", "seniority": 3, "user_id": users[1].id},
        {"full_name": "Bob Johnson", "seniority": 10, "user_id": users[2].id},
    ]

    for emp_data in employees_data:
        employee = Employee(**emp_data)
        db_session.add(employee)
    db_session.commit()

    # Act
    response = test_client.get("/employees/list")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 3
    assert {emp["full_name"] for emp in data} == {
        "John Doe",
        "Jane Smith",
        "Bob Johnson",
    }


def test_list_employees_with_pagination_skip(test_client, setup_database, db_session):
    """Test GET /employees/list with skip parameter"""
    # Arrange - Create multiple employees
    from app.models.user import User
    from app.models.employee import Employee

    for i in range(5):
        user = User(name=f"User {i}", email=generate_unique_email(), age=20 + i)
        db_session.add(user)
    db_session.commit()

    users = db_session.query(User).all()

    for i, user in enumerate(users):
        employee = Employee(full_name=f"Employee {i}", seniority=i, user_id=user.id)
        db_session.add(employee)
    db_session.commit()

    # Act
    response = test_client.get("/employees/list?skip=2")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 3


def test_list_employees_with_pagination_limit(test_client, setup_database, db_session):
    """Test GET /employees/list with limit parameter"""
    # Arrange - Create multiple employees
    from app.models.user import User
    from app.models.employee import Employee

    for i in range(5):
        user = User(name=f"User {i}", email=generate_unique_email(), age=20 + i)
        db_session.add(user)
    db_session.commit()

    users = db_session.query(User).all()

    for i, user in enumerate(users):
        employee = Employee(full_name=f"Employee {i}", seniority=i, user_id=user.id)
        db_session.add(employee)
    db_session.commit()

    # Act
    response = test_client.get("/employees/list?limit=2")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2


def test_employee_id(test_client, setup_database, db_session):
    """Test GET /employees/:id returns employee object with correct ID"""
    # Arrange - Create a user and an employee
    from app.models.user import User
    from app.models.employee import Employee

    user = User(name="Test User", email=generate_unique_email(), age=30)
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)

    employee = Employee(full_name="John Doe", seniority=5, user_id=user.id)
    db_session.add(employee)
    db_session.commit()
    db_session.refresh(employee)

    # Act
    response = test_client.get(f"/employees/{employee.id}")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert data["id"] == employee.id
