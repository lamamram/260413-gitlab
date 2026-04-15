import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.database import Base
from selenium import webdriver

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
        # Delete all employees and users before each test to ensure clean state
        from app.models.employee import Employee
        from app.models.user import User

        try:
            db.query(Employee).delete()
            db.query(User).delete()
            db.commit()
        except Exception:
            # If tables don't exist yet, just pass
            db.rollback()
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
def selenium():
    options = webdriver.FirefoxOptions()
    # pas besoin de GUI => un conteneur docker n'a pas de serveur X11
    options.add_argument("--headless")
    # appeler le serveur selenium
    return webdriver.Remote(
        command_executor="http://selenium-server:4444/wd/hub",
        options=options
    )