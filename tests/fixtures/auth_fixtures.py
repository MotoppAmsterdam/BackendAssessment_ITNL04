import pytest
from fastapi.testclient import TestClient

from db import models
from db.database import get_db
from auth.oauth2 import get_current_user

@pytest.fixture
def test_user(db_session):
    user = models.DbUser(
        username="testuser",
        email="test@example.com",
        password="fakehashed"
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user

@pytest.fixture
def override_get_current_user(test_user):
    def _override():
        return test_user
    return _override

@pytest.fixture
def authorized_client(db_session, override_get_current_user):
    from main import app
    app.dependency_overrides[get_db] = lambda: db_session
    app.dependency_overrides[get_current_user] = override_get_current_user
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()

@pytest.fixture
def unauthorized_client(db_session):
    from main import app
    app.dependency_overrides[get_db] = lambda: db_session
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()
