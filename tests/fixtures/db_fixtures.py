import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.database import get_db, Base

# Test database in memory
TEST_DB_URL = "sqlite:///:memory:"
test_engine = create_engine(TEST_DB_URL, connect_args={"check_same_thread": False}).connect()
testing_session_local = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

# Dependency override
def override_get_db():
    db = testing_session_local()
    try:
        yield db
    finally:
        db.close()

# Create database prior to any test
@pytest.fixture(scope="function", autouse=True)
def setup_database():
    from main import app
#    app.dependency_overrides[get_db] = override_get_db
    Base.metadata.create_all(bind=test_engine)
    print(f"\nSetting up")
    yield
    print(f"\nTearing down")
    Base.metadata.drop_all(bind=test_engine)

@pytest.fixture
def db_session():
    session = testing_session_local()
    try:
        yield session
    finally:
        session.close()
