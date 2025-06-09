# MASTER CONVENTIONS
**Single Source of Truth for FastAPI MCP Project Conventions**

## 🎯 Core Philosophy
- **AI-First Development**: Optimized for AI code generation and understanding
- **Smart Blueprint Strategy**: Embedded templates in blueprints (no separate code examples)
- **FastAPI Backend Focus**: Pure backend MCP server architecture
- **Single Source of Truth**: All conventions centralized in this file

## 📁 Project Structure

### Root Directory Structure
```
FastAPI-MCP/
├── .ai-docs/                   # 🤖 AI Documentation & Context
│   ├── @core/                  # Master authoritative files
│   │   ├── MASTER_CONVENTIONS.md      # 🔥 THIS FILE - All conventions
│   │   ├── MASTER_TESTING.md          # 🔥 All testing protocols
│   │   └── MASTER_ARCHITECTURE.md     # 🔥 All architecture patterns
│   ├── @conventions/           # Quick reference files (reference @core)
│   ├── @context/              # Detailed context files
│   ├── @prompts/              # Task-specific AI prompts
│   └── chat-summaries/        # AI conversation records
├── backend-mcp/               # FastAPI MCP Server
│   ├── blueprints/            # Smart blueprints with embedded templates
│   ├── server/                # MCP server implementation
│   ├── tools/                 # MCP tools
│   ├── models/                # Data models
│   ├── services/              # Business logic
│   ├── routes/                # API endpoints
│   ├── middleware/            # Custom middleware
│   ├── database/              # Database configuration
│   ├── config/                # Configuration files
│   └── main.py               # FastAPI application entry point
├── tests/                     # All testing infrastructure
│   ├── unit/                  # Service/model unit tests
│   ├── integration/           # API endpoint tests
│   ├── load/                  # Performance tests
│   └── security/              # Security tests
├── scripts/                   # Automation and validation scripts
├── docs/                      # Human documentation
└── requirements.txt           # Python dependencies
```

## 🏗️ Backend Architecture Layers

### 1. Routes Layer (`backend-mcp/routes/`)
**Purpose**: HTTP endpoint definitions and request/response handling
**Naming**: `{resource}_routes.py` (e.g., `user_routes.py`, `auth_routes.py`)
**Responsibilities**:
- Request validation
- Response formatting
- HTTP status codes
- Route grouping with APIRouter

### 2. Services Layer (`backend-mcp/services/`)
**Purpose**: Business logic and orchestration
**Naming**: `{resource}_service.py` (e.g., `user_service.py`, `auth_service.py`)
**Responsibilities**:
- Business rule enforcement
- Data transformation
- External service integration
- Error handling

### 3. Models Layer (`backend-mcp/models/`)
**Purpose**: Data structures and database models
**Naming**: `{resource}_model.py` (e.g., `user_model.py`, `auth_model.py`)
**Responsibilities**:
- Pydantic models for validation
- SQLAlchemy models for database
- Data serialization/deserialization

### 4. MCP Tools Layer (`backend-mcp/tools/`)
**Purpose**: MCP-specific tool implementations
**Naming**: `{tool_name}_tool.py` (e.g., `code_generator_tool.py`)
**Responsibilities**:
- MCP tool interface implementation
- Tool-specific business logic
- Integration with FastAPI services

### 5. Database Layer (`backend-mcp/database/`)
**Purpose**: Data persistence and database integration
**Naming**: See `.ai-docs/@core/MASTER_DATABASE_PATTERNS.md` for complete patterns
**Responsibilities**:
- Database connection management
- Repository pattern implementation
- Data model definitions
- Migration and schema management

**Database Strategy Selection:**
- **Traditional Database**: Use for complex queries, full control, enterprise requirements
- **Supabase Integration**: Use for rapid development, built-in auth, real-time features
- **📚 Complete Patterns**: See `.ai-docs/@core/MASTER_DATABASE_PATTERNS.md`

## ⚙️ Configuration Management (MANDATORY)

### Production-Ready Settings Pattern
```python
# backend-mcp/config/settings.py
from pydantic import BaseSettings, Field
from typing import List, Optional
import os

class Settings(BaseSettings):
    # Application
    app_name: str = "FastAPI MCP Server"
    app_version: str = "1.0.0"
    environment: str = Field(default="development", regex="^(development|staging|production)$")
    debug: bool = Field(default=False)

    # Database (Traditional)
    database_url: Optional[str] = None
    database_pool_size: int = 20
    database_max_overflow: int = 0
    database_echo: bool = False

    # Database (Supabase)
    supabase_url: Optional[str] = None
    supabase_anon_key: Optional[str] = None
    supabase_service_key: Optional[str] = None

    # Security
    secret_key: str = Field(..., min_length=32)
    cors_origins: List[str] = ["http://localhost:3000"]
    allowed_hosts: List[str] = ["*"]

    # Monitoring & Logging
    log_level: str = Field(default="INFO", regex="^(DEBUG|INFO|WARNING|ERROR|CRITICAL)$")
    sentry_dsn: Optional[str] = None
    enable_metrics: bool = True

    # Rate Limiting
    enable_rate_limiting: bool = True
    rate_limit_requests: int = 100
    rate_limit_window: int = 60  # seconds

    # Feature Flags
    enable_swagger_ui: bool = True
    enable_redoc: bool = True

    class Config:
        env_file = ".env"
        case_sensitive = False

    @property
    def is_production(self) -> bool:
        return self.environment == "production"

    @property
    def is_development(self) -> bool:
        return self.environment == "development"

# Global settings instance
settings = Settings()
```

### Environment File Template (.env)
```bash
# Application
APP_NAME="FastAPI MCP Server"
APP_VERSION="1.0.0"
ENVIRONMENT="development"  # development|staging|production
DEBUG=true

# Database (Choose one approach)
# Traditional Database
DATABASE_URL="postgresql+asyncpg://user:pass@localhost/db"
DATABASE_POOL_SIZE=20

# OR Supabase
SUPABASE_URL="https://your-project.supabase.co"
SUPABASE_ANON_KEY="your-anon-key"
SUPABASE_SERVICE_KEY="your-service-key"

# Security
SECRET_KEY="your-super-secret-key-min-32-chars"
CORS_ORIGINS=["http://localhost:3000","https://yourdomain.com"]

# Monitoring
LOG_LEVEL="INFO"
SENTRY_DSN="https://your-sentry-dsn"
ENABLE_METRICS=true

# Rate Limiting
ENABLE_RATE_LIMITING=true
RATE_LIMIT_REQUESTS=100
RATE_LIMIT_WINDOW=60
```

## 📝 Naming Conventions

### File Naming
- **Python files**: `snake_case.py`
- **Directories**: `snake_case/`
- **Configuration files**: `snake_case.yaml`, `snake_case.json`
- **Documentation**: `UPPER_CASE.md` for master files, `@lower-case.md` for AI files

### Code Naming
- **Classes**: `PascalCase` (e.g., `UserService`, `AuthModel`)
- **Functions/Methods**: `snake_case` (e.g., `get_user`, `validate_token`)
- **Variables**: `snake_case` (e.g., `user_id`, `auth_token`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `MAX_RETRY_ATTEMPTS`)
- **API Endpoints**: `kebab-case` (e.g., `/api/v1/user-profile`)

### Blueprint Naming
- **Format**: `{action}-{layer}-{resource}.json`
- **Examples**: 
  - `create-route-user.json`
  - `update-service-auth.json`
  - `delete-model-product.json`

## 🔧 Smart Blueprint System

### Blueprint Structure
```json
{
  "name": "create-route-user",
  "description": "Creates a FastAPI route for user management",
  "category": "routes",
  "template": {
    "embedded_code": "# Jinja2 template code here",
    "dependencies": ["fastapi", "pydantic"],
    "imports": ["from fastapi import APIRouter"]
  },
  "parameters": {
    "resource_name": "string",
    "methods": "array",
    "auth_required": "boolean"
  },
  "validation": {
    "required_files": ["models/{resource}_model.py"],
    "test_requirements": ["unit", "integration"]
  }
}
```

### Blueprint Categories
- **`routes/`**: API endpoint blueprints
- **`services/`**: Business logic blueprints
- **`models/`**: Data model blueprints
- **`tools/`**: MCP tool blueprints
- **`middleware/`**: Custom middleware blueprints
- **`database/`**: Database configuration blueprints
- **`system/`**: Health checks and system monitoring blueprints

## 🚀 FastAPI Patterns

### Standard Route Pattern
```python
from fastapi import APIRouter, Depends, HTTPException
from ..services.{resource}_service import {Resource}Service
from ..models.{resource}_model import {Resource}Model

router = APIRouter(prefix="/api/v1/{resource}", tags=["{resource}"])

@router.post("/", response_model={Resource}Model)
async def create_{resource}(
    {resource}_data: {Resource}CreateModel,
    service: {Resource}Service = Depends()
):
    try:
        return await service.create_{resource}({resource}_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
```

### Standard Service Pattern
```python
from typing import List, Optional
from ..models.{resource}_model import {Resource}Model
from ..database.connection import get_db_session

class {Resource}Service:
    async def create_{resource}(self, {resource}_data: {Resource}CreateModel) -> {Resource}Model:
        # Business logic implementation
        pass
    
    async def get_{resource}(self, {resource}_id: int) -> Optional[{Resource}Model]:
        # Retrieval logic implementation
        pass
```

### Standard Model Pattern
```python
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class {Resource}BaseModel(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)

class {Resource}CreateModel({Resource}BaseModel):
    pass

class {Resource}Model({Resource}BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
```

## 🏥 System Health and Monitoring Patterns

### Health Check Endpoint (MANDATORY)
```python
from fastapi import APIRouter, Depends, HTTPException, status
from datetime import datetime
from typing import Dict, Any

router = APIRouter(prefix="/system", tags=["system"])

@router.get("/health", response_model=Dict[str, Any])
async def health_check():
    """
    Health check endpoint for load balancers and monitoring systems.
    REQUIRED for production deployment.
    """
    health_status = {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "version": settings.app_version,
        "environment": settings.environment
    }

    # Database health check
    try:
        # Traditional: async with get_db_session() as db: await db.execute("SELECT 1")
        # Supabase: supabase.table('health_check').select("count", count="exact").execute()
        health_status["database"] = "healthy"
    except Exception as e:
        health_status["database"] = "unhealthy"
        health_status["status"] = "degraded"

    return health_status

@router.get("/ready")
async def readiness_check():
    """Readiness check for Kubernetes deployments."""
    return {"status": "ready", "timestamp": datetime.utcnow().isoformat()}
```

### Structured Logging Pattern (MANDATORY)
```python
# backend-mcp/utils/logging.py
import structlog
import logging
import sys

def configure_logging(log_level: str = "INFO", environment: str = "development"):
    """Configure structured logging for production readiness."""
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=getattr(logging, log_level.upper())
    )

    structlog.configure(
        processors=[
            structlog.stdlib.add_log_level,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.JSONRenderer() if environment == "production"
            else structlog.dev.ConsoleRenderer()
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )

# Usage in services
logger = structlog.get_logger()

async def create_user(self, user_data: UserCreateModel) -> UserModel:
    logger.info("user_creation_started", user_email=user_data.email)
    try:
        user = await self.repository.create(user_data)
        logger.info("user_creation_completed", user_id=user.id)
        return user
    except Exception as e:
        logger.error("user_creation_failed", error=str(e))
        raise
```

## 🔒 Security Conventions

### Authentication Pattern
```python
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from ..services.auth_service import AuthService

security = HTTPBearer()

async def get_current_user(
    token: str = Depends(security),
    auth_service: AuthService = Depends()
):
    user = await auth_service.verify_token(token.credentials)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )
    return user
```

### Input Validation
- Use Pydantic models for all request/response validation
- Implement field-level validation with `Field()` constraints
- Use custom validators for complex business rules
- Sanitize all user inputs

### Rate Limiting (MANDATORY for Production)
```python
# backend-mcp/middleware/rate_limiting.py
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi import Request, HTTPException

# Initialize rate limiter
limiter = Limiter(key_func=get_remote_address)

# Add to FastAPI app
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Usage in routes
@router.post("/api/v1/users/")
@limiter.limit("5/minute")  # Prevent abuse
async def create_user(request: Request, user_data: UserCreateModel):
    return await service.create_user(user_data)

@router.get("/api/v1/users/")
@limiter.limit("100/minute")  # Higher limit for reads
async def get_users(request: Request):
    return await service.get_users()
```

### Error Monitoring (MANDATORY for Production)
```python
# backend-mcp/utils/monitoring.py
import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration

def configure_error_monitoring(settings):
    """Configure error monitoring for production."""
    if settings.sentry_dsn and settings.is_production:
        sentry_sdk.init(
            dsn=settings.sentry_dsn,
            integrations=[
                FastApiIntegration(auto_enabling_integrations=False),
                SqlalchemyIntegration(),
            ],
            traces_sample_rate=0.1,
            environment=settings.environment,
            release=settings.app_version
        )

# Usage in main.py
from .utils.monitoring import configure_error_monitoring
configure_error_monitoring(settings)
```

## 📊 Error Handling Conventions

### Standard Error Response
```python
from fastapi import HTTPException
from typing import Dict, Any

class APIError(HTTPException):
    def __init__(self, status_code: int, detail: str, error_code: str = None):
        super().__init__(status_code=status_code, detail=detail)
        self.error_code = error_code

# Usage
raise APIError(
    status_code=400,
    detail="Invalid user data provided",
    error_code="INVALID_USER_DATA"
)
```

### Error Categories
- **400 Bad Request**: Invalid input data
- **401 Unauthorized**: Authentication required
- **403 Forbidden**: Insufficient permissions
- **404 Not Found**: Resource not found
- **422 Unprocessable Entity**: Validation errors
- **500 Internal Server Error**: Unexpected server errors

## 🧪 Testing Integration

### Test File Naming
- **Unit Tests**: `test_{module_name}.py`
- **Integration Tests**: `test_{resource}_integration.py`
- **Load Tests**: `test_{resource}_load.py`
- **Security Tests**: `test_{resource}_security.py`

### Test Structure
```python
import pytest
from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

class Test{Resource}:
    def test_create_{resource}_success(self):
        # Test implementation
        pass
    
    def test_create_{resource}_validation_error(self):
        # Test implementation
        pass
```

## 🔄 Development Workflow

### 1. Blueprint → Implementation → Test
1. Create/select appropriate blueprint
2. Generate code using blueprint
3. Implement business logic
4. Create comprehensive tests
5. Validate with automation scripts

### 2. Required Validation Scripts
- `scripts/validate_smart_blueprint.py` - Blueprint validation
- `scripts/validate_fastapi_conventions.py` - Code convention validation
- `scripts/validate_ai_context.py` - AI documentation validation

## 📚 Documentation Standards

### Code Documentation
- Use docstrings for all classes and functions
- Follow Google docstring format
- Include type hints for all parameters and return values
- Document complex business logic

### API Documentation
- FastAPI auto-generates OpenAPI documentation
- Use descriptive endpoint summaries and descriptions
- Include example request/response bodies
- Document all possible error responses

---

**Authority**: This file is the single source of truth for all project conventions. All other convention files should reference this master file.

**Last Updated**: 2025-01-07
**Version**: 1.0.0
