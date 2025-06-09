"""
FastAPI test configuration and fixtures.
"""
import pytest
import asyncio
from typing import Generator, AsyncGenerator
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from backend_mcp.main import app
from backend_mcp.database import get_db, Base
from backend_mcp.models.auth_models import User

# Test database URL (SQLite in memory)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Create test engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

# Create test session
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
def test_db() -> Generator:
    """Create test database tables and clean up after test."""
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


def override_get_db():
    """Override database dependency for testing."""
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


@pytest.fixture(scope="function")
def client(test_db) -> Generator:
    """Create test client with database override."""
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


@pytest.fixture
def sample_user_data():
    """Sample user data for testing."""
    return {
        "email": "test@example.com",
        "name": "Test User",
        "password": "TestPassword123!"
    }


@pytest.fixture
async def authenticated_user(client, sample_user_data):
    """Create and authenticate a test user."""
    # Create user
    response = client.post("/api/v1/auth/register", json=sample_user_data)
    assert response.status_code == 201
    
    # Login user
    login_data = {
        "email": sample_user_data["email"],
        "password": sample_user_data["password"]
    }
    response = client.post("/api/v1/auth/login", json=login_data)
    assert response.status_code == 200
    
    token_data = response.json()
    return {
        "user": token_data["user"],
        "token": token_data["access_token"],
        "headers": {"Authorization": f"Bearer {token_data['access_token']}"}
    }


@pytest.fixture
def auth_headers(authenticated_user):
    """Get authentication headers for requests."""
    return authenticated_user["headers"]


# Performance testing fixtures
@pytest.fixture
def performance_config():
    """Configuration for performance tests."""
    return {
        "max_response_time": 2.0,  # seconds
        "max_memory_usage": 100,   # MB
        "concurrent_users": 10,
        "test_duration": 30        # seconds
    }


# Security testing fixtures
@pytest.fixture
def security_test_data():
    """Test data for security testing."""
    return {
        "sql_injection_payloads": [
            "'; DROP TABLE users; --",
            "1' OR '1'='1",
            "admin'--",
            "' UNION SELECT * FROM users --"
        ],
        "xss_payloads": [
            "<script>alert('xss')</script>",
            "javascript:alert('xss')",
            "<img src=x onerror=alert('xss')>"
        ],
        "invalid_tokens": [
            "invalid_token",
            "Bearer invalid",
            "expired_token_here"
        ]
    }


# Load testing fixtures
@pytest.fixture
def load_test_config():
    """Configuration for load testing."""
    return {
        "users": 50,
        "spawn_rate": 5,
        "run_time": "30s",
        "host": "http://localhost:8000"
    }
