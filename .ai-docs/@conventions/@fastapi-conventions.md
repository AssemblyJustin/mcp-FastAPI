# @fastapi-conventions

**AI Context**: FastAPI-specific patterns and conventions. ALWAYS load `.ai-docs/@core/MASTER_CONVENTIONS.md` first.

## ⚠️ CRITICAL: Load Core Conventions First
This file extends the core conventions with FastAPI-specific patterns. Always reference `.ai-docs/@core/MASTER_CONVENTIONS.md` for base rules.

## FastAPI Naming Conventions

### Route Files
- **Route Modules**: `[domain]_routes.py` (e.g., `user_routes.py`, `auth_routes.py`)
- **Route Functions**: `[action]_[resource]` (e.g., `create_user`, `get_user_by_id`)
- **Router Variables**: `router = APIRouter()`

### Model Files
- **Pydantic Models**: `[Resource]Base`, `[Resource]Create`, `[Resource]Update`, `[Resource]Response`
- **SQLAlchemy Models**: `[Resource]` (e.g., `User`, `Product`)
- **Model Files**: `[domain]_models.py` or `models/[domain].py`

### Service Files
- **Service Classes**: `[Resource]Service` (e.g., `UserService`, `AuthService`)
- **Service Files**: `[domain]_service.py` or `services/[domain].py`
- **Service Methods**: `[action]_[resource]` (e.g., `create_user`, `authenticate_user`)

## Directory Structure

### Backend MCP Structure
```
backend-mcp/
├── blueprints/                # Smart blueprints with embedded templates
│   ├── api/
│   │   ├── routes/            # Route blueprints with embedded code
│   │   ├── services/          # Service blueprints with embedded code
│   │   └── models/            # Model blueprints with embedded code
│   ├── middleware/            # Middleware blueprints
│   ├── database/              # Database blueprints
│   └── auth/                  # Authentication blueprints
├── templates/                 # Jinja2 templates (if needed)
├── static/                    # Static files
└── main.py                    # FastAPI MCP server
```

## FastAPI Patterns

### Route Pattern
```python
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from ..models import {{modelName}}, {{modelName}}Create, {{modelName}}Update
from ..services import {{modelName}}Service
from ..dependencies import get_current_user, get_db

router = APIRouter(
    prefix="/{{routePrefix}}",
    tags=["{{routeName}}"]
)

@router.{{httpMethod.lower()}}("/{{endpoint}}")
async def {{functionName}}(
    {{#if requestModel}}request: {{requestModel}},{{/if}}
    {{#if authRequired}}current_user: User = Depends(get_current_user),{{/if}}
    db: Session = Depends(get_db),
    service: {{modelName}}Service = Depends()
) -> {{responseModel}}:
    """
    {{description}}
    """
    try:
        result = await service.{{operationName}}({{parameters}})
        return result
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )
```

### Service Pattern
```python
from typing import List, Optional
from sqlalchemy.orm import Session
from ..models import {{modelName}}
from ..schemas import {{modelName}}Create, {{modelName}}Update

class {{modelName}}Service:
    def __init__(self, db: Session):
        self.db = db
    
    async def create_{{resourceName}}(self, {{resourceName}}_data: {{modelName}}Create) -> {{modelName}}:
        """Create a new {{resourceName}}"""
        db_{{resourceName}} = {{modelName}}(**{{resourceName}}_data.dict())
        self.db.add(db_{{resourceName}})
        self.db.commit()
        self.db.refresh(db_{{resourceName}})
        return db_{{resourceName}}
    
    async def get_{{resourceName}}(self, {{resourceName}}_id: int) -> Optional[{{modelName}}]:
        """Get {{resourceName}} by ID"""
        return self.db.query({{modelName}}).filter({{modelName}}.id == {{resourceName}}_id).first()
    
    async def get_{{resourceName}}s(self, skip: int = 0, limit: int = 100) -> List[{{modelName}}]:
        """Get list of {{resourceName}}s"""
        return self.db.query({{modelName}}).offset(skip).limit(limit).all()
    
    async def update_{{resourceName}}(self, {{resourceName}}_id: int, {{resourceName}}_data: {{modelName}}Update) -> Optional[{{modelName}}]:
        """Update {{resourceName}}"""
        db_{{resourceName}} = self.get_{{resourceName}}({{resourceName}}_id)
        if db_{{resourceName}}:
            for key, value in {{resourceName}}_data.dict(exclude_unset=True).items():
                setattr(db_{{resourceName}}, key, value)
            self.db.commit()
            self.db.refresh(db_{{resourceName}})
        return db_{{resourceName}}
    
    async def delete_{{resourceName}}(self, {{resourceName}}_id: int) -> bool:
        """Delete {{resourceName}}"""
        db_{{resourceName}} = self.get_{{resourceName}}({{resourceName}}_id)
        if db_{{resourceName}}:
            self.db.delete(db_{{resourceName}})
            self.db.commit()
            return True
        return False
```

### Model Pattern
```python
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

# Base model with common fields
class {{modelName}}Base(BaseModel):
    {{#each fields}}
    {{name}}: {{type}}{{#if optional}} = None{{/if}}
    {{/each}}

# Model for creating new records
class {{modelName}}Create({{modelName}}Base):
    pass

# Model for updating records
class {{modelName}}Update(BaseModel):
    {{#each fields}}
    {{name}}: Optional[{{type}}] = None
    {{/each}}

# Model for API responses
class {{modelName}}Response({{modelName}}Base):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

# SQLAlchemy model
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class {{modelName}}(Base):
    __tablename__ = "{{tableName}}"
    
    id = Column(Integer, primary_key=True, index=True)
    {{#each fields}}
    {{name}} = Column({{sqlType}}{{#if nullable}}, nullable=True{{/if}})
    {{/each}}
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
```

## Security Patterns

### Authentication Dependency
```python
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt

security = HTTPBearer()

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Get current authenticated user"""
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials"
            )
        # Get user from database
        user = get_user_by_id(user_id)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found"
            )
        return user
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )
```

### Input Validation
```python
from pydantic import BaseModel, validator, Field
from typing import Optional

class {{modelName}}Create(BaseModel):
    email: str = Field(..., regex=r'^[^@]+@[^@]+\.[^@]+$')
    password: str = Field(..., min_length=8)
    name: str = Field(..., min_length=1, max_length=100)
    
    @validator('password')
    def validate_password(cls, v):
        if not any(c.isupper() for c in v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not any(c.islower() for c in v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not any(c.isdigit() for c in v):
            raise ValueError('Password must contain at least one digit')
        return v
```

## Testing Patterns

### Unit Test Pattern
```python
import pytest
from unittest.mock import Mock, patch
from ..services import {{modelName}}Service
from ..schemas import {{modelName}}Create, {{modelName}}Update

class Test{{modelName}}Service:
    @pytest.fixture
    def service(self):
        mock_db = Mock()
        return {{modelName}}Service(mock_db)
    
    @pytest.fixture
    def sample_{{resourceName}}_data(self):
        return {{modelName}}Create(
            {{#each fields}}
            {{name}}={{sampleValue}},
            {{/each}}
        )
    
    async def test_create_{{resourceName}}(self, service, sample_{{resourceName}}_data):
        """Test creating a new {{resourceName}}"""
        result = await service.create_{{resourceName}}(sample_{{resourceName}}_data)
        assert result is not None
        assert result.{{primaryField}} == sample_{{resourceName}}_data.{{primaryField}}
```

### Integration Test Pattern
```python
import pytest
from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

class Test{{modelName}}API:
    def test_create_{{resourceName}}(self):
        """Test creating {{resourceName}} via API"""
        {{resourceName}}_data = {
            {{#each fields}}
            "{{name}}": {{sampleValue}},
            {{/each}}
        }
        response = client.post("/{{routePrefix}}/{{resourceName}}s", json={{resourceName}}_data)
        assert response.status_code == 201
        assert response.json()["{{primaryField}}"] == {{resourceName}}_data["{{primaryField}}"]
    
    def test_get_{{resourceName}}(self):
        """Test getting {{resourceName}} by ID"""
        response = client.get("/{{routePrefix}}/{{resourceName}}s/1")
        assert response.status_code == 200
        assert "id" in response.json()
```

## Blueprint Template Variables

### Standard Variables
- `{{modelName}}` - Pydantic model name (PascalCase)
- `{{resourceName}}` - Resource name (snake_case)
- `{{routePrefix}}` - API route prefix (e.g., "/api/v1")
- `{{tableName}}` - Database table name (snake_case)
- `{{functionName}}` - Route function name (snake_case)
- `{{httpMethod}}` - HTTP method (GET, POST, PUT, DELETE)
- `{{authRequired}}` - Boolean for authentication requirement
- `{{responseModel}}` - Response model type
- `{{requestModel}}` - Request model type

### Field Variables
- `{{fields}}` - Array of field definitions
- `{{fields.name}}` - Field name
- `{{fields.type}}` - Field type
- `{{fields.optional}}` - Boolean for optional fields
- `{{fields.sqlType}}` - SQLAlchemy column type
- `{{fields.sampleValue}}` - Sample value for testing

## AI Validation Checklist

### Before Creating API Files
```bash
# Validate FastAPI conventions
python scripts/validate_fastapi_conventions.py --check-all

# Validate API pipeline
python scripts/validate_api_pipeline.py --endpoint [endpoint_name]

# Security validation
python scripts/validate_api_security.py --scan-routes
```

### Required Validations
1. ✅ **Route naming** follows snake_case pattern
2. ✅ **Model naming** follows PascalCase pattern
3. ✅ **Authentication** properly implemented
4. ✅ **Input validation** using Pydantic
5. ✅ **Error handling** with proper HTTP status codes
6. ✅ **Database operations** use proper transactions
7. ✅ **API documentation** auto-generated with OpenAPI
8. ✅ **1:1:1 relationship** maintained (example → blueprint → test)
