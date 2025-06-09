# MASTER TESTING PROTOCOL
**Single Source of Truth for FastAPI MCP Testing Standards**

## 🎯 Testing Philosophy

### Core Principles
1. **Test-Driven Development**: Write tests before implementation
2. **Blueprint → Test Relationship**: Every blueprint must have corresponding tests
3. **Automated Validation**: All tests must be automatable
4. **Performance Gates**: All tests must meet performance targets
5. **FastAPI Focus**: Testing optimized for FastAPI backend patterns

## 🔄 Mandatory Testing Workflow

### For Every New FastAPI Component:

#### Step 1: Create Blueprint
```bash
# Location: backend-mcp/blueprints/[category]/
# Naming: [action]-[layer]-[resource].json
# Must include test requirements in validation section
```

#### Step 2: Generate Code from Blueprint
```bash
# Use smart blueprint system to generate FastAPI code
# Code includes embedded templates and dependencies
```

#### Step 3: Create Test Suite (MANDATORY)
```bash
# Unit Test: tests/unit/[layer]/test_[resource].py
# Integration Test: tests/integration/test_[resource]_api.py
# Load Test: tests/load/test_[resource]_performance.py
# Security Test: tests/security/test_[resource]_security.py
```

#### Step 4: Validate Complete Pipeline
```bash
# Run validation script to ensure blueprint → test relationship
python scripts/validate_smart_blueprint.py [component-name]
```

## 🧪 Test Categories & Requirements

### Unit Tests (`tests/unit/`)
**Purpose**: Test individual functions/classes in isolation
**Performance**: < 100ms per test
**Coverage**: 90%+ for new code
**Structure**: Organized by layer (routes/, services/, models/, tools/)

**Requirements**:
- No external dependencies (use mocks)
- Test edge cases and error conditions
- Include Pydantic model validation tests
- Test business logic in services layer

**Example Structure**:
```python
# tests/unit/services/test_user_service.py
import pytest
from unittest.mock import Mock, AsyncMock
from backend_mcp.services.user_service import UserService
from backend_mcp.models.user_model import UserCreateModel

class TestUserService:
    @pytest.fixture
    def user_service(self):
        return UserService()
    
    @pytest.mark.asyncio
    async def test_create_user_success(self, user_service):
        # Test implementation
        pass
    
    @pytest.mark.asyncio
    async def test_create_user_validation_error(self, user_service):
        # Test implementation
        pass
```

### Integration Tests (`tests/integration/`)
**Purpose**: Test API endpoints and component interactions
**Performance**: < 5 seconds per test
**Coverage**: All API endpoints must have integration tests

**Requirements**:
- Test complete request/response cycle
- Validate HTTP status codes and response formats
- Test authentication and authorization
- Use TestClient for FastAPI testing

**Example Structure**:
```python
# tests/integration/test_user_api.py
import pytest
from fastapi.testclient import TestClient
from backend_mcp.main import app

client = TestClient(app)

class TestUserAPI:
    def test_create_user_endpoint(self):
        response = client.post("/api/v1/users/", json={
            "name": "Test User",
            "email": "test@example.com"
        })
        assert response.status_code == 201
        assert response.json()["name"] == "Test User"
    
    def test_create_user_validation_error(self):
        response = client.post("/api/v1/users/", json={
            "name": "",  # Invalid empty name
            "email": "invalid-email"
        })
        assert response.status_code == 422
```

### Load Tests (`tests/load/`)
**Purpose**: Performance and scalability testing
**Performance**: Measure response times and throughput
**Tools**: Use locust or similar load testing framework

**Requirements**:
- Test API endpoints under load
- Measure response times and error rates
- Test concurrent user scenarios
- Validate performance targets

**Example Structure**:
```python
# tests/load/test_user_load.py
from locust import HttpUser, task, between

class UserLoadTest(HttpUser):
    wait_time = between(1, 3)
    
    @task
    def create_user(self):
        self.client.post("/api/v1/users/", json={
            "name": "Load Test User",
            "email": "loadtest@example.com"
        })
    
    @task(3)
    def get_users(self):
        self.client.get("/api/v1/users/")
```

### Security Tests (`tests/security/`)
**Purpose**: Security vulnerability testing
**Performance**: < 10 seconds per test
**Coverage**: All authenticated endpoints and data validation

**Requirements**:
- Test authentication bypass attempts
- Test input validation and injection attacks
- Test authorization and access controls
- Test rate limiting and abuse prevention
- Test health endpoint security
- Test error monitoring integration

**Example Structure**:
```python
# tests/security/test_user_security.py
import pytest
from fastapi.testclient import TestClient
from backend_mcp.main import app

client = TestClient(app)

class TestUserSecurity:
    def test_unauthorized_access(self):
        response = client.get("/api/v1/users/me")
        assert response.status_code == 401

    def test_rate_limiting(self):
        # Test rate limiting works
        for _ in range(6):  # Exceed 5/minute limit
            response = client.post("/api/v1/users/", json={"email": "test@example.com"})
        assert response.status_code == 429  # Too Many Requests

    def test_health_endpoint_security(self):
        # Health endpoint should not expose sensitive data
        response = client.get("/system/health")
        assert response.status_code == 200
        data = response.json()
        assert "database_password" not in str(data)
        assert "secret_key" not in str(data)

    def test_sql_injection_protection(self):
        response = client.get("/api/v1/users/1'; DROP TABLE users; --")
        assert response.status_code in [400, 404]  # Should not succeed

    def test_xss_protection(self):
        response = client.post("/api/v1/users/", json={
            "name": "<script>alert('xss')</script>",
            "email": "test@example.com"
        })
        # Should either reject or sanitize the input
        assert response.status_code in [400, 422] or \
               "<script>" not in response.json().get("name", "")
```

## 📊 Quality Gates

### Pre-Commit Requirements
- [ ] All unit tests pass
- [ ] Integration tests pass for affected components
- [ ] Generated code passes FastAPI validation
- [ ] Test coverage maintains 90%+
- [ ] Security tests pass for affected endpoints

### Pre-Release Requirements
- [ ] Full test suite passes (unit + integration + load + security)
- [ ] All blueprints have corresponding tests
- [ ] Performance regression tests pass
- [ ] Security vulnerability scan passes
- [ ] API documentation tests pass

## 🚀 Automation Scripts

### Required Scripts:

#### 1. Blueprint Validator
```bash
# scripts/validate_smart_blueprint.py
# Validates blueprint → test relationship
python scripts/validate_smart_blueprint.py --check-all
python scripts/validate_smart_blueprint.py --component user_service
```

#### 2. Test Generator
```bash
# scripts/generate_test_suite.py
# Auto-generates test templates for new components
python scripts/generate_test_suite.py --blueprint create-service-user
python scripts/generate_test_suite.py --layer routes --resource user
```

#### 3. Performance Monitor
```bash
# scripts/performance_monitor.py
# Tracks test performance and API response times
python scripts/performance_monitor.py --benchmark
python scripts/performance_monitor.py --endpoint /api/v1/users
```

#### 4. Coverage Enforcer
```bash
# scripts/enforce_coverage.py
# Ensures coverage requirements are met
python scripts/enforce_coverage.py --min-coverage 90
python scripts/enforce_coverage.py --report
```

#### 5. Security Scanner
```bash
# scripts/security_scanner.py
# Automated security testing
python scripts/security_scanner.py --scan-all
python scripts/security_scanner.py --endpoint /api/v1/users
```

## 📈 Performance Targets

### Test Execution Speed
- **Unit Tests**: < 100ms each, < 30 seconds total
- **Integration Tests**: < 5 seconds each, < 5 minutes total
- **Load Tests**: Variable (based on test scenario)
- **Security Tests**: < 10 seconds each, < 2 minutes total
- **Full Suite**: < 10 minutes total

### API Performance Targets
- **Simple CRUD Operations**: < 200ms response time
- **Complex Business Logic**: < 1 second response time
- **Database Queries**: < 500ms response time
- **Authentication**: < 100ms response time

## 🔧 Configuration Standards

### Test Framework Configurations

#### Pytest Configuration (`tests/config/pytest.ini`)
```ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    --cov=backend_mcp
    --cov-report=html
    --cov-report=term-missing
    --cov-fail-under=90
    -v
markers =
    unit: Unit tests
    integration: Integration tests
    load: Load tests
    security: Security tests
    slow: Slow running tests
```

#### FastAPI Test Configuration

**Database-Agnostic Base Configuration:**
```python
# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from backend_mcp.main import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def authenticated_client():
    # Setup authenticated test client
    pass
```

**Traditional Database Testing:**
```python
# tests/traditional_db_conftest.py
import pytest
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from backend_mcp.database.connection import Base, get_db_session

TEST_DATABASE_URL = "postgresql+asyncpg://test:test@localhost/test_db"

@pytest.fixture(scope="session")
async def test_engine():
    engine = create_async_engine(TEST_DATABASE_URL, echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield engine
    await engine.dispose()

@pytest.fixture
async def test_db_session(test_engine):
    TestSessionLocal = async_sessionmaker(test_engine, expire_on_commit=False)
    async with TestSessionLocal() as session:
        yield session
        await session.rollback()
```

**Supabase Testing:**
```python
# tests/supabase_conftest.py
import pytest
from supabase import create_client
from backend_mcp.database.supabase_client import get_supabase_client

TEST_SUPABASE_URL = "https://test-project.supabase.co"
TEST_SUPABASE_KEY = "test-anon-key"

@pytest.fixture
def test_supabase_client():
    return create_client(TEST_SUPABASE_URL, TEST_SUPABASE_KEY)

@pytest.fixture(autouse=True)
async def cleanup_test_data(test_supabase_client):
    yield
    # Cleanup test data after each test
    test_supabase_client.table('users').delete().neq('id', 'keep').execute()
```

**📚 Complete Database Testing Patterns**: See `.ai-docs/@core/MASTER_DATABASE_PATTERNS.md`

### Output Management
- **All outputs**: `tests/outputs/` (gitignored)
- **Coverage reports**: `tests/outputs/coverage/`
- **Load test results**: `tests/outputs/load/`
- **Security scan results**: `tests/outputs/security/`
- **Logs**: `tests/outputs/logs/`

## 🎯 FastAPI-Specific Testing Patterns

### Testing Pydantic Models
```python
def test_user_model_validation():
    # Test valid data
    user_data = {"name": "John Doe", "email": "john@example.com"}
    user = UserCreateModel(**user_data)
    assert user.name == "John Doe"
    
    # Test invalid data
    with pytest.raises(ValidationError):
        UserCreateModel(name="", email="invalid-email")
```

### Testing Dependency Injection
```python
def test_service_dependency():
    def mock_service():
        return MockUserService()
    
    app.dependency_overrides[UserService] = mock_service
    response = client.post("/api/v1/users/", json=user_data)
    assert response.status_code == 201
```

### Testing Async Endpoints
```python
@pytest.mark.asyncio
async def test_async_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/api/v1/users/", json=user_data)
        assert response.status_code == 201
```

## 🚨 Failure Protocols

### Test Failure Response
1. **Unit Test Failure**: Block commit, fix immediately
2. **Integration Test Failure**: Investigate API contract issues
3. **Load Test Failure**: Investigate performance regression
4. **Security Test Failure**: Immediate security review required

### Blueprint Validation Failure
1. Check blueprint → test relationship integrity
2. Verify file naming conventions
3. Validate blueprint template syntax
4. Update missing tests or blueprints

## 📋 Testing Checklist Template

### For Each New FastAPI Component:
- [ ] Blueprint created with test requirements specified
- [ ] Unit test covers all service methods
- [ ] Integration test covers all API endpoints
- [ ] Load test covers performance scenarios
- [ ] Security test covers authentication/authorization
- [ ] Performance test meets speed targets
- [ ] Blueprint validation script passes
- [ ] Coverage requirements met (90%+)
- [ ] Documentation updated

---

**Authority**: This file is the single source of truth for all testing protocols. All other testing files should reference this master file.

**Last Updated**: 2025-01-07
**Version**: 1.0.0
