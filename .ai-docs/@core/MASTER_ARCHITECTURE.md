# MASTER ARCHITECTURE
**Single Source of Truth for FastAPI MCP Architecture Patterns**

## 🎯 Architecture Philosophy

### Core Principles
1. **MCP-First Design**: Built around Model Context Protocol patterns
2. **Smart Blueprint System**: AI-optimized code generation with embedded templates
3. **FastAPI Backend Focus**: Pure backend architecture, no frontend concerns
4. **Layered Architecture**: Clear separation of concerns across layers
5. **AI-First Development**: Optimized for AI code generation and understanding

## 🏗️ System Architecture Overview

### High-Level Architecture
```
┌─────────────────────────────────────────────────────────────┐
│                    MCP Client                               │
│                 (External Systems)                         │
└─────────────────────┬───────────────────────────────────────┘
                      │ MCP Protocol
┌─────────────────────▼───────────────────────────────────────┐
│                FastAPI MCP Server                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │   Routes    │  │ Middleware  │  │   Tools     │        │
│  │   Layer     │  │   Layer     │  │   Layer     │        │
│  └─────┬───────┘  └─────┬───────┘  └─────┬───────┘        │
│        │                │                │                │
│  ┌─────▼───────┐  ┌─────▼───────┐  ┌─────▼───────┐        │
│  │  Services   │  │ Validation  │  │ MCP Handler │        │
│  │   Layer     │  │   Layer     │  │   Layer     │        │
│  └─────┬───────┘  └─────────────┘  └─────┬───────┘        │
│        │                                 │                │
│  ┌─────▼───────┐  ┌─────────────┐  ┌─────▼───────┐        │
│  │   Models    │  │  Database   │  │   Config    │        │
│  │   Layer     │  │   Layer     │  │   Layer     │        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
└─────────────────────────────────────────────────────────────┘
```

## 🔧 Smart Blueprint System Architecture

### Blueprint Engine Components
```
┌─────────────────────────────────────────────────────────────┐
│                Blueprint Engine                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │  Blueprint  │  │  Template   │  │ Validation  │        │
│  │   Parser    │  │   Engine    │  │   Engine    │        │
│  └─────┬───────┘  └─────┬───────┘  └─────┬───────┘        │
│        │                │                │                │
│        ▼                ▼                ▼                │
│  ┌─────────────────────────────────────────────────────┐  │
│  │            Code Generator                           │  │
│  └─────┬───────────────────────────────────────────────┘  │
│        │                                                  │
│        ▼                                                  │
│  ┌─────────────────────────────────────────────────────┐  │
│  │         Generated FastAPI Code                      │  │
│  └─────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Blueprint Structure
```json
{
  "metadata": {
    "name": "create-route-user",
    "version": "1.0.0",
    "category": "routes",
    "description": "Creates FastAPI route for user management"
  },
  "template": {
    "embedded_code": "Jinja2 template with FastAPI patterns",
    "dependencies": ["fastapi", "pydantic", "sqlalchemy"],
    "imports": ["from fastapi import APIRouter", "from pydantic import BaseModel"]
  },
  "parameters": {
    "resource_name": {"type": "string", "required": true},
    "methods": {"type": "array", "default": ["GET", "POST"]},
    "auth_required": {"type": "boolean", "default": true}
  },
  "validation": {
    "required_files": ["models/{resource}_model.py", "services/{resource}_service.py"],
    "test_requirements": ["unit", "integration"],
    "performance_targets": {"response_time": "< 200ms"}
  },
  "relationships": {
    "depends_on": ["create-model-{resource}", "create-service-{resource}"],
    "generates": ["routes/{resource}_routes.py"]
  }
}
```

## 🏛️ Layer Architecture Details

### 1. Routes Layer (`backend-mcp/routes/`)
**Responsibility**: HTTP request/response handling and API contract definition

**Architecture Pattern**:
```python
# Standard route module structure
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from ..services.{resource}_service import {Resource}Service
from ..models.{resource}_model import {Resource}Model, {Resource}CreateModel
from ..middleware.auth import get_current_user

router = APIRouter(
    prefix="/api/v1/{resource}",
    tags=["{resource}"],
    dependencies=[Depends(get_current_user)]
)

# Route implementations follow standard patterns
@router.post("/", response_model={Resource}Model, status_code=status.HTTP_201_CREATED)
@router.get("/", response_model=List[{Resource}Model])
@router.get("/{id}", response_model={Resource}Model)
@router.put("/{id}", response_model={Resource}Model)
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
```

### 2. Services Layer (`backend-mcp/services/`)
**Responsibility**: Business logic, data orchestration, and external integrations

**Architecture Pattern**:
```python
# Standard service class structure
from typing import List, Optional
from ..models.{resource}_model import {Resource}Model, {Resource}CreateModel
from ..database.repositories.{resource}_repository import {Resource}Repository

class {Resource}Service:
    def __init__(self, repository: {Resource}Repository = Depends()):
        self.repository = repository
    
    async def create_{resource}(self, data: {Resource}CreateModel) -> {Resource}Model:
        # Business logic validation
        # Data transformation
        # Repository interaction
        pass
    
    async def get_{resource}_by_id(self, id: int) -> Optional[{Resource}Model]:
        # Retrieval logic
        pass
    
    async def update_{resource}(self, id: int, data: {Resource}UpdateModel) -> {Resource}Model:
        # Update logic with validation
        pass
    
    async def delete_{resource}(self, id: int) -> bool:
        # Deletion logic
        pass
```

### 3. Models Layer (`backend-mcp/models/`)
**Responsibility**: Data structures, validation, and serialization

**Architecture Pattern**:
```python
# Standard model structure with Pydantic
from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime
from enum import Enum

class {Resource}Status(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

class {Resource}BaseModel(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    status: {Resource}Status = {Resource}Status.ACTIVE
    
    @validator('name')
    def validate_name(cls, v):
        if not v.strip():
            raise ValueError('Name cannot be empty')
        return v.strip()

class {Resource}CreateModel({Resource}BaseModel):
    pass

class {Resource}UpdateModel(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    status: Optional[{Resource}Status] = None

class {Resource}Model({Resource}BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
```

### 4. MCP Tools Layer (`backend-mcp/tools/`)
**Responsibility**: MCP protocol implementation and tool definitions

**Architecture Pattern**:
```python
# Standard MCP tool structure
from mcp.server import Server
from mcp.types import Tool, TextContent
from typing import Any, Dict
from ..services.{resource}_service import {Resource}Service

class {Resource}MCPTool:
    def __init__(self, service: {Resource}Service):
        self.service = service
    
    def get_tool_definition(self) -> Tool:
        return Tool(
            name="{resource}_manager",
            description="Manage {resource} entities",
            inputSchema={
                "type": "object",
                "properties": {
                    "action": {"type": "string", "enum": ["create", "read", "update", "delete"]},
                    "data": {"type": "object"}
                },
                "required": ["action"]
            }
        )
    
    async def handle_tool_call(self, arguments: Dict[str, Any]) -> TextContent:
        action = arguments.get("action")
        data = arguments.get("data", {})
        
        if action == "create":
            result = await self.service.create_{resource}(data)
        elif action == "read":
            result = await self.service.get_{resource}_by_id(data.get("id"))
        # ... other actions
        
        return TextContent(
            type="text",
            text=f"{Resource} {action} completed: {result}"
        )
```

## 🔌 MCP Integration Architecture

### MCP Server Structure
```python
# backend-mcp/server/mcp_server.py
from mcp.server import Server
from mcp.server.stdio import stdio_server
from ..tools.{resource}_tool import {Resource}MCPTool
from ..services.{resource}_service import {Resource}Service

class FastAPIMCPServer:
    def __init__(self):
        self.server = Server("fastapi-mcp")
        self.setup_tools()
    
    def setup_tools(self):
        # Register MCP tools
        {resource}_tool = {Resource}MCPTool({Resource}Service())
        self.server.add_tool({resource}_tool.get_tool_definition())
    
    async def run(self):
        async with stdio_server() as streams:
            await self.server.run(streams[0], streams[1])
```

### Tool Registration Pattern
```python
# Automatic tool discovery and registration
import importlib
import pkgutil
from ..tools import *

class ToolRegistry:
    def __init__(self):
        self.tools = {}
    
    def discover_tools(self):
        # Auto-discover all MCP tools
        for importer, modname, ispkg in pkgutil.iter_modules(tools.__path__):
            module = importlib.import_module(f"backend_mcp.tools.{modname}")
            # Register tools from module
    
    def register_tool(self, tool_class):
        tool_instance = tool_class()
        self.tools[tool_instance.name] = tool_instance
```

## 🗄️ Database Architecture

### Repository Pattern
```python
# backend-mcp/database/repositories/{resource}_repository.py
from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete
from ..models.{resource}_db_model import {Resource}DBModel
from ...models.{resource}_model import {Resource}CreateModel, {Resource}UpdateModel

class {Resource}Repository:
    def __init__(self, db: Session = Depends(get_db_session)):
        self.db = db
    
    async def create(self, data: {Resource}CreateModel) -> {Resource}DBModel:
        db_obj = {Resource}DBModel(**data.dict())
        self.db.add(db_obj)
        await self.db.commit()
        await self.db.refresh(db_obj)
        return db_obj
    
    async def get_by_id(self, id: int) -> Optional[{Resource}DBModel]:
        result = await self.db.execute(
            select({Resource}DBModel).where({Resource}DBModel.id == id)
        )
        return result.scalar_one_or_none()
```

### Database Model Pattern
```python
# backend-mcp/database/models/{resource}_db_model.py
from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.sql import func
from ..base import Base
from ...models.{resource}_model import {Resource}Status

class {Resource}DBModel(Base):
    __tablename__ = "{resource}s"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    description = Column(String(500), nullable=True)
    status = Column(Enum({Resource}Status), default={Resource}Status.ACTIVE)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
```

## 🔒 Security Architecture

### Authentication Flow
```
Client Request → JWT Token → Auth Middleware → Route Handler
                     ↓
              Token Validation → User Context → Business Logic
```

### Authorization Pattern
```python
# backend-mcp/middleware/auth.py
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from ..services.auth_service import AuthService
from ..models.user_model import UserModel

security = HTTPBearer()

async def get_current_user(
    token: str = Depends(security),
    auth_service: AuthService = Depends()
) -> UserModel:
    user = await auth_service.verify_token(token.credentials)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )
    return user

async def require_admin(
    current_user: UserModel = Depends(get_current_user)
) -> UserModel:
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    return current_user
```

## 📊 Performance Architecture

### Caching Strategy
```python
# backend-mcp/middleware/cache.py
from functools import wraps
from typing import Any, Callable
import redis
import json

class CacheManager:
    def __init__(self):
        self.redis_client = redis.Redis(host='localhost', port=6379, db=0)
    
    def cache_result(self, ttl: int = 300):
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            async def wrapper(*args, **kwargs) -> Any:
                cache_key = f"{func.__name__}:{hash(str(args) + str(kwargs))}"
                cached = self.redis_client.get(cache_key)
                
                if cached:
                    return json.loads(cached)
                
                result = await func(*args, **kwargs)
                self.redis_client.setex(
                    cache_key, 
                    ttl, 
                    json.dumps(result, default=str)
                )
                return result
            return wrapper
        return decorator
```

### Async Processing Pattern
```python
# backend-mcp/services/async_service.py
import asyncio
from typing import List
from concurrent.futures import ThreadPoolExecutor

class AsyncProcessingService:
    def __init__(self):
        self.executor = ThreadPoolExecutor(max_workers=4)
    
    async def process_batch(self, items: List[Any]) -> List[Any]:
        tasks = [self.process_item(item) for item in items]
        return await asyncio.gather(*tasks)
    
    async def process_item(self, item: Any) -> Any:
        # CPU-intensive work in thread pool
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(
            self.executor, 
            self._cpu_intensive_work, 
            item
        )
```

## 🔄 Development Workflow Architecture

### Blueprint → Code → Test Pipeline
```
Blueprint Definition → Template Engine → Code Generation → Test Generation → Validation
        ↓                    ↓               ↓              ↓              ↓
   JSON Schema      →   Jinja2 Engine  →  FastAPI Code  →  Test Suite  →  Quality Gates
```

### Continuous Integration Architecture
```yaml
# .github/workflows/ci.yml
name: FastAPI MCP CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.11
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: |
          python -m pytest tests/ --cov=backend_mcp --cov-report=xml
      - name: Validate blueprints
        run: |
          python scripts/validate_smart_blueprint.py --check-all
      - name: Security scan
        run: |
          python scripts/security_scanner.py --scan-all
```

## 🚀 Production Application Setup

### Main Application Pattern (Production-Ready)
```python
# backend-mcp/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

from .config.settings import settings
from .utils.logging import configure_logging
from .utils.monitoring import configure_error_monitoring
from .routes import user_routes, system_routes

# Configure logging and monitoring
configure_logging(settings.log_level, settings.environment)
configure_error_monitoring(settings)

# Create FastAPI app
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    docs_url="/docs" if settings.enable_swagger_ui else None,
    redoc_url="/redoc" if settings.enable_redoc else None,
)

# Rate limiting
if settings.enable_rate_limiting:
    limiter = Limiter(key_func=get_remote_address)
    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(system_routes.router)  # Health checks (MANDATORY)
app.include_router(user_routes.router)

@app.on_event("startup")
async def startup_event():
    """Application startup tasks."""
    logger.info("application_startup", version=settings.app_version)

@app.on_event("shutdown")
async def shutdown_event():
    """Application shutdown tasks."""
    logger.info("application_shutdown")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug,
        log_level=settings.log_level.lower()
    )
```

---

**Authority**: This file is the single source of truth for all architecture patterns. All other architecture files should reference this master file.

**Last Updated**: 2025-01-07
**Version**: 1.0.0
