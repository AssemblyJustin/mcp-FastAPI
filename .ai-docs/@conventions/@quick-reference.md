# @quick-reference

**AI Context**: Ultra-quick reference card. ALWAYS load `.ai-docs/@core/MASTER_CONVENTIONS.md` first for complete rules.

## ⚠️ CRITICAL: Load Master Files First
```
1. .ai-docs/@core/MASTER_CONVENTIONS.md (ALL conventions)
2. .ai-docs/@core/MASTER_TESTING.md (ALL testing protocols)
3. .ai-docs/@core/MASTER_ARCHITECTURE.md (ALL architecture patterns)
4. .ai-docs/@core/MASTER_DATABASE_PATTERNS.md (ALL database patterns)
```

## 🔥 Essential FastAPI Patterns

### File Naming (from MASTER_CONVENTIONS.md)
- **Routes**: `{resource}_routes.py` (e.g., `user_routes.py`)
- **Services**: `{resource}_service.py` (e.g., `user_service.py`)
- **Models**: `{resource}_model.py` (e.g., `user_model.py`)
- **Blueprints**: `{action}-{layer}-{resource}.json` (e.g., `create-route-user.json`)

### Directory Structure (from MASTER_CONVENTIONS.md)
```
backend-mcp/
├── routes/          # API endpoints
├── services/        # Business logic
├── models/          # Data structures
├── tools/           # MCP tools
├── middleware/      # Custom middleware
├── database/        # Database config
└── blueprints/      # Smart blueprints
```

### Testing Structure (from MASTER_TESTING.md)
```
tests/
├── unit/           # < 100ms, 90%+ coverage
├── integration/    # < 5s, API endpoints
├── load/           # Performance testing
└── security/       # < 10s, auth/validation
```

## ⚡ Quick Commands

### Blueprint Validation (from MASTER_TESTING.md)
```bash
python scripts/validate_smart_blueprint.py --check-all
python scripts/validate_fastapi_conventions.py --check-all
python scripts/validate_ai_context.py --check-all
```

### Test Generation (from MASTER_TESTING.md)
```bash
python scripts/generate_test_suite.py --blueprint create-route-user
python scripts/generate_api_test_suite.py --endpoint users --type crud
python scripts/performance_monitor.py --benchmark
```

## 🏗️ Architecture Layers (from MASTER_ARCHITECTURE.md)

### 1. Routes Layer
- **Purpose**: HTTP request/response handling
- **Pattern**: APIRouter with dependency injection
- **Performance**: < 200ms response time

### 2. Services Layer
- **Purpose**: Business logic and orchestration
- **Pattern**: Async service classes with repositories
- **Performance**: < 1s for complex operations

### 3. Models Layer
- **Purpose**: Data validation and serialization
- **Pattern**: Pydantic models + SQLAlchemy ORM
- **Performance**: < 100ms validation

### 4. MCP Tools Layer
- **Purpose**: MCP protocol implementation
- **Pattern**: Tool classes with handle_tool_call methods
- **Performance**: < 500ms tool execution

### 5. Database Layer
- **Purpose**: Data persistence and integration
- **Traditional**: SQLAlchemy + PostgreSQL/MySQL (full control)
- **Supabase**: Managed database + auth + real-time (rapid development)
- **📚 Complete Patterns**: See MASTER_DATABASE_PATTERNS.md

## 🔒 Security Patterns (from MASTER_CONVENTIONS.md)

### Authentication
```python
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer

security = HTTPBearer()

async def get_current_user(token: str = Depends(security)):
    # Token validation logic
    pass
```

### Rate Limiting (MANDATORY)
```python
from slowapi import Limiter
limiter = Limiter(key_func=get_remote_address)

@limiter.limit("5/minute")
async def create_user(request: Request, user_data: UserCreateModel):
    pass
```

### Input Validation
```python
from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    email: str = Field(..., regex=r'^[^@]+@[^@]+\.[^@]+$')
    password: str = Field(..., min_length=8)
```

## 📊 Performance Targets (from MASTER_TESTING.md)

### Test Performance
- **Unit Tests**: < 100ms each, < 30s total
- **Integration Tests**: < 5s each, < 5min total
- **Load Tests**: Variable (scenario-based)
- **Security Tests**: < 10s each, < 2min total

### API Performance
- **Simple CRUD**: < 200ms response time
- **Complex Logic**: < 1s response time
- **Database Queries**: < 500ms response time
- **Authentication**: < 100ms response time

## 🎯 Development Workflow (from MASTER_ARCHITECTURE.md)

### 1. Blueprint → Implementation → Test
1. Create/select smart blueprint with embedded template
2. Generate FastAPI code using blueprint
3. Implement business logic
4. Create comprehensive test suite (unit + integration + load + security)
5. Validate with automation scripts

### 2. Quality Gates (from MASTER_TESTING.md)
- ✅ All tests pass
- ✅ 90%+ test coverage
- ✅ Blueprint validation passes
- ✅ Security tests pass
- ✅ Performance targets met

## 🚨 Critical Rules (from MASTER_CONVENTIONS.md)

### Must Do
- ✅ **Load master files first**: Always reference @core/MASTER_*.md
- ✅ **Smart blueprint strategy**: Blueprint → test relationship
- ✅ **FastAPI patterns**: Use standard route/service/model patterns
- ✅ **Comprehensive testing**: Unit + integration + load + security
- ✅ **Security first**: Authentication, validation, error handling
- ✅ **Production ready**: Health checks, logging, rate limiting, monitoring

### Must Not Do
- ❌ **No React content**: This is FastAPI backend only
- ❌ **No separate code examples**: Use embedded templates in blueprints
- ❌ **No root-level APIs**: Must be in backend-mcp/
- ❌ **No hardcoded secrets**: Use environment variables
- ❌ **No SQL injection risks**: Use parameterized queries

## 📚 Reference Hierarchy

```
@core/MASTER_*.md          # 🔥 AUTHORITATIVE (Single Source of Truth)
    ↓
@conventions/@*.md         # Quick reference (this file)
    ↓
@context/@*.md            # Detailed context
    ↓
@prompts/@*.md            # Task-specific prompts
```

---

**Authority**: This is a quick reference only. For complete and authoritative information, always reference the master files in `.ai-docs/@core/`.

**Last Updated**: 2025-01-07
**Version**: 1.0.0
