# @fastapi-patterns

**AI Context**: FastAPI design patterns and architectural guidelines for MCP blueprint system.

## FastAPI Architecture Layers

### 1. Route Layer (API Endpoints)
**Purpose**: Handle HTTP requests and responses
**Location**: `backend-mcp/code-examples/api/routes/`

```python
# Standard route pattern
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from ...models import UserCreate, UserUpdate, UserResponse
from ...services import UserService
from ...dependencies import get_current_user, get_db

router = APIRouter(prefix="/api/v1", tags=["users"])

@router.post("/users", response_model=UserResponse, status_code=201)
async def create_user(
    user_data: UserCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> UserResponse:
    """Create a new user"""
    try:
        service = UserService(db)
        user = await service.create_user(user_data)
        return UserResponse.from_orm(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
```

### 2. Service Layer (Business Logic)
**Purpose**: Implement business rules and data processing
**Location**: `backend-mcp/code-examples/services/`

```python
# Standard service pattern
from typing import List, Optional
from sqlalchemy.orm import Session
from ..models import User, UserCreate, UserUpdate
from ..utils import hash_password, verify_password

class UserService:
    def __init__(self, db: Session):
        self.db = db
    
    async def create_user(self, user_data: UserCreate) -> User:
        """Create a new user with validation"""
        # Check if user exists
        existing_user = self.db.query(User).filter(
            User.email == user_data.email
        ).first()
        if existing_user:
            raise ValueError("User with this email already exists")
        
        # Hash password
        hashed_password = hash_password(user_data.password)
        
        # Create user
        db_user = User(
            email=user_data.email,
            hashed_password=hashed_password,
            name=user_data.name
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
    
    async def authenticate_user(self, email: str, password: str) -> Optional[User]:
        """Authenticate user credentials"""
        user = self.db.query(User).filter(User.email == email).first()
        if user and verify_password(password, user.hashed_password):
            return user
        return None
```

### 3. Model Layer (Data Structures)
**Purpose**: Define data validation and database mapping
**Location**: `backend-mcp/code-examples/models/`

```python
# Pydantic models for API
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    name: str = Field(..., min_length=1, max_length=100)

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    password: Optional[str] = Field(None, min_length=8)

class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

# SQLAlchemy model for database
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
```

### 4. Middleware Layer (Cross-cutting Concerns)
**Purpose**: Handle authentication, CORS, rate limiting, etc.
**Location**: `backend-mcp/code-examples/middleware/`

```python
# Authentication middleware
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from ..models import User
from ..database import get_db

security = HTTPBearer()

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
) -> User:
    """Get current authenticated user"""
    try:
        payload = jwt.decode(
            credentials.credentials, 
            SECRET_KEY, 
            algorithms=[ALGORITHM]
        )
        user_id: int = payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials"
            )
        
        user = db.query(User).filter(User.id == user_id).first()
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

## Common FastAPI Patterns

### 1. CRUD Operations Pattern
```python
# Complete CRUD for a resource
@router.get("/users", response_model=List[UserResponse])
async def list_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """List users with pagination"""
    service = UserService(db)
    users = await service.get_users(skip=skip, limit=limit)
    return [UserResponse.from_orm(user) for user in users]

@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    """Get user by ID"""
    service = UserService(db)
    user = await service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse.from_orm(user)

@router.put("/users/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update user"""
    service = UserService(db)
    user = await service.update_user(user_id, user_data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse.from_orm(user)

@router.delete("/users/{user_id}", status_code=204)
async def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete user"""
    service = UserService(db)
    success = await service.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
```

### 2. Authentication Pattern
```python
# Login endpoint
@router.post("/auth/login", response_model=TokenResponse)
async def login(
    credentials: LoginRequest,
    db: Session = Depends(get_db)
):
    """Authenticate user and return token"""
    service = AuthService(db)
    user = await service.authenticate_user(
        credentials.email, 
        credentials.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    
    access_token = create_access_token(data={"sub": str(user.id)})
    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
        user=UserResponse.from_orm(user)
    )

# Protected endpoint
@router.get("/auth/me", response_model=UserResponse)
async def get_current_user_info(
    current_user: User = Depends(get_current_user)
):
    """Get current user information"""
    return UserResponse.from_orm(current_user)
```

### 3. File Upload Pattern
```python
@router.post("/upload", response_model=FileResponse)
async def upload_file(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user)
):
    """Upload file with validation"""
    # Validate file type
    if file.content_type not in ["image/jpeg", "image/png", "application/pdf"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid file type"
        )
    
    # Validate file size (10MB max)
    if file.size > 10 * 1024 * 1024:
        raise HTTPException(
            status_code=400,
            detail="File too large"
        )
    
    # Save file
    file_service = FileService()
    saved_file = await file_service.save_file(file, current_user.id)
    return FileResponse.from_orm(saved_file)
```

### 4. Background Task Pattern
```python
from fastapi import BackgroundTasks

@router.post("/send-email", status_code=202)
async def send_email(
    email_data: EmailRequest,
    background_tasks: BackgroundTasks,
    current_user: User = Depends(get_current_user)
):
    """Send email in background"""
    background_tasks.add_task(
        send_email_task,
        email_data.to,
        email_data.subject,
        email_data.body
    )
    return {"message": "Email queued for sending"}

async def send_email_task(to: str, subject: str, body: str):
    """Background task to send email"""
    # Email sending logic here
    pass
```

## Error Handling Patterns

### 1. Custom Exception Handler
```python
from fastapi import Request
from fastapi.responses import JSONResponse

class CustomException(Exception):
    def __init__(self, status_code: int, detail: str):
        self.status_code = status_code
        self.detail = detail

@app.exception_handler(CustomException)
async def custom_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )
```

### 2. Validation Error Handler
```python
from fastapi.exceptions import RequestValidationError

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "detail": "Validation error",
            "errors": exc.errors()
        }
    )
```

## Testing Patterns

### 1. Unit Test Pattern
```python
import pytest
from unittest.mock import Mock, AsyncMock
from backend_mcp.services.user_service import UserService

@pytest.fixture
def mock_db():
    return Mock()

@pytest.fixture
def user_service(mock_db):
    return UserService(mock_db)

@pytest.mark.asyncio
async def test_create_user_success(user_service):
    # Test implementation
    pass
```

### 2. Integration Test Pattern
```python
import pytest
from fastapi.testclient import TestClient
from backend_mcp.main import app

client = TestClient(app)

def test_create_user_api():
    response = client.post("/api/v1/users", json={
        "email": "test@example.com",
        "name": "Test User",
        "password": "password123"
    })
    assert response.status_code == 201
    assert response.json()["email"] == "test@example.com"
```

## Security Best Practices

### 1. Input Validation
- Use Pydantic models for all request/response data
- Implement custom validators for complex rules
- Sanitize user inputs to prevent injection attacks

### 2. Authentication & Authorization
- Use JWT tokens with proper expiration
- Implement role-based access control
- Validate permissions on each protected endpoint

### 3. Rate Limiting
```python
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@router.post("/login")
@limiter.limit("5/minute")
async def login(request: Request, credentials: LoginRequest):
    # Login logic
    pass
```

### 4. CORS Configuration
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
```

## Performance Optimization

### 1. Database Optimization
- Use async database operations
- Implement connection pooling
- Add proper database indexes
- Use query optimization techniques

### 2. Caching
```python
from fastapi_cache import FastAPICache
from fastapi_cache.decorator import cache

@router.get("/users/{user_id}")
@cache(expire=300)  # Cache for 5 minutes
async def get_user(user_id: int):
    # User retrieval logic
    pass
```

### 3. Response Optimization
- Use response models to control serialization
- Implement pagination for list endpoints
- Compress responses for large payloads

## Blueprint Integration

### Template Variables for FastAPI
- `{{resourceName}}` - snake_case resource name
- `{{modelName}}` - PascalCase model name
- `{{httpMethod}}` - HTTP method (GET, POST, PUT, DELETE)
- `{{endpoint}}` - API endpoint path
- `{{authRequired}}` - Boolean for authentication
- `{{responseModel}}` - Response model class
- `{{requestModel}}` - Request model class
- `{{routePrefix}}` - API route prefix
- `{{description}}` - Endpoint description
- `{{tags}}` - OpenAPI tags array
