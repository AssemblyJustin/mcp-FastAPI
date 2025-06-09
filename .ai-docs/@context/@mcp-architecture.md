# @mcp-architecture

**AI Context**: Complete FastAPI MCP system architecture and AI assistant integration guide.

## System Overview

### FastAPI MCP Purpose
AI-first Model Context Protocol server for backend development with:
- **Smart Blueprint System**: Embedded template-based API code generation
- **Single Source Strategy**: Blueprint → Test (no separate code examples)
- **Backend Design Layers**: Routes → Services → Models
- **Testing Protocol**: Unit, Integration, Load, and Security testing

### Core Components
```
MCP Server (backend-mcp/)
├── Smart Blueprint Engine: Processes embedded templates and generates FastAPI code
├── Blueprint Loader: Manages smart blueprint definitions with embedded code
├── Code Generator: Creates routes, services, and models from embedded templates
├── Template Processor: Handles variable substitution and conditional logic
└── Validation Engine: Ensures API quality, security, and performance
```

## AI Assistant Integration Points

### 1. Context Files to Reference
**ALWAYS reference these files before any action**:
- `.ai-docs/@core/MASTER_CONVENTIONS.md` - All conventions (LOAD FIRST)
- `.ai-docs/@core/MASTER_TESTING.md` - All testing protocols
- `.ai-docs/@core/MASTER_ARCHITECTURE.md` - All architecture patterns
- `@conventions/@project-structure.md` - Backend directory organization
- `@conventions/@naming-conventions.md` - FastAPI naming rules
- `@conventions/@fastapi-conventions.md` - FastAPI-specific patterns
- `@prompts/@api-creation.md` - API creation workflows

### 2. Critical Validation Points
**Before creating ANY API file**:
```python
# Pseudo-code for AI validation
def validate_before_creation(file_path, file_type):
    check_fastapi_conventions()
    verify_backend_structure()
    confirm_naming_convention()
    ensure_1_1_1_relationship()
    validate_api_testing_requirements()
    check_security_patterns()
```

### 3. Required Workflow
**MANDATORY 3-step process**:
1. **Smart Blueprint**: Create in `backend-mcp/blueprints/` with embedded code template
2. **Test Suite**: Create in `tests/` (unit + integration + load + security)
3. **Validation**: Run `python scripts/validate_smart_blueprint.py`

## Blueprint System Architecture

### Smart FastAPI Blueprint Structure
```json
{
  "id": "smart-[layer]-[endpoint]",
  "description": "API endpoint purpose and usage",
  "strategy": "embedded-template",
  "parameters": {
    "routeName": {"type": "string", "required": true},
    "modelName": {"type": "string", "required": true},
    "httpMethod": {"type": "string", "default": "GET"},
    "routePrefix": {"type": "string", "default": "/api/v1"},
    "authRequired": {"type": "boolean", "default": true}
  },
  "codeTemplate": {
    "language": "python",
    "executable": true,
    "testable": true,
    "content": "# Embedded Python code with {{variables}}"
  },
  "testTemplate": {
    "language": "python",
    "framework": "pytest",
    "content": "# Embedded test code"
  },
  "validation": {
    "syntax": ["python", "fastapi", "pydantic"],
    "required": ["proper-typing", "error-handling", "security"],
    "forbidden": ["hardcoded-secrets", "sql-injection-risk"]
  },
  "metadata": {
    "estimatedTokens": 1200,
    "estimatedComplexity": 5,
    "generationTime": "<1s",
    "aiOptimized": true
  }
}
```

### Smart Template Variable System
**Standardized variables for embedded templates**:
- `{{routeName}}` - Route function name (snake_case)
- `{{modelName}}` - Pydantic model name (PascalCase)
- `{{httpMethod}}` - HTTP method (GET, POST, PUT, DELETE)
- `{{routePrefix}}` - API prefix path
- `{{authRequired}}` - Authentication requirement (enables conditional blocks)
- `{{responseModel}}` - Response model type
- `{{#if authRequired}}...{{/if}}` - Conditional template blocks

## Testing Architecture

### Test Types and Purposes
```
Unit Tests (tests/unit/)
├── Purpose: Test individual services/functions
├── Performance: < 100ms per test
├── Coverage: 90%+ for new code
└── Isolation: Mock external dependencies

Integration Tests (tests/integration/)
├── Purpose: Test API endpoints end-to-end
├── Performance: < 2 seconds per test
├── Scope: Database + API + validation
└── Tools: TestClient with real database

Load Tests (tests/load/)
├── Purpose: Performance and scalability testing
├── Performance: Measure response times/throughput
├── Scope: API endpoints under load
└── Tools: Locust or Artillery

Security Tests (tests/security/)
├── Purpose: Authentication, authorization, input validation
├── Performance: < 5 seconds per test
├── Scope: Security vulnerabilities and compliance
└── Tools: Custom security test suite

Manual Tests (tests/manual/)
├── Purpose: API demo scripts and benchmarks
├── Performance: Variable
├── Scope: System demonstration and validation
└── Usage: Postman collections and curl scripts
```

### Test Automation Scripts
```bash
# API pipeline validation
python scripts/validate_api_pipeline.py --check-all

# Test generation
python scripts/generate_api_test_suite.py --endpoint users --type crud

# Performance monitoring
python scripts/api_performance_monitor.py --benchmark

# Security testing
python scripts/security_test_runner.py --scan-all
```

## FastAPI Architecture Layers

### Backend Design Hierarchy
```
Routes (API Endpoints)
├── Examples: /users, /auth/login, /products/{id}
├── Characteristics: HTTP method handling, request/response
├── Dependencies: Services and models
└── Performance: < 1 second generation

Services (Business Logic)
├── Examples: UserService, AuthService, ProductService
├── Characteristics: Core business operations, data processing
├── Dependencies: Models and external services
└── Performance: < 2 seconds generation

Models (Data Layer)
├── Examples: User, Product, Order (Pydantic/SQLAlchemy)
├── Characteristics: Data validation, database mapping
├── Dependencies: Database schema
└── Performance: < 1 second generation

Middleware (Cross-cutting Concerns)
├── Examples: Authentication, CORS, Rate Limiting
├── Characteristics: Request/response processing
├── Dependencies: Configuration and utilities
└── Performance: < 1 second generation
```

### FastAPI File Structure
```python
# Standard FastAPI route template
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from ..models import {{modelName}}, {{modelName}}Create, {{modelName}}Update
from ..services import {{modelName}}Service
from ..dependencies import get_current_user

router = APIRouter(prefix="{{routePrefix}}", tags=["{{routeName}}"])

@router.{{httpMethod.lower()}}("/{{routeName}}")
async def {{routeName}}_endpoint(
    {{#if authRequired}}current_user: User = Depends(get_current_user),{{/if}}
    service: {{modelName}}Service = Depends()
) -> {{responseModel}}:
    """
    {{description}}
    """
    try:
        result = await service.{{operationName}}()
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
```

## AI Assistant Decision Tree

### API Creation Decision Flow
```
1. Determine API Layer Type
   ├── HTTP endpoint? → Route
   ├── Business logic? → Service
   ├── Data structure? → Model
   └── Cross-cutting concern? → Middleware

2. Check Existing APIs
   ├── Similar endpoint exists? → Extend or modify
   └── New endpoint needed? → Create from scratch

3. Follow Creation Workflow
   ├── Create code example
   ├── Create blueprint
   ├── Generate test suite (unit + integration + load + security)
   └── Validate API pipeline

4. Quality Assurance
   ├── Run all tests
   ├── Check performance targets
   ├── Validate security compliance
   ├── Confirm API documentation
   └── Ensure 1:1:1 relationship
```

### Error Resolution Flow
```
1. API Pipeline Validation Failure
   ├── Missing code example? → Create using @prompts/@api-creation.md
   ├── Missing blueprint? → Create with proper reference
   ├── Missing tests? → Generate using automation script
   └── Naming convention error? → Fix using @conventions

2. Test Failure
   ├── Unit test failure? → Fix service/model logic
   ├── Integration test failure? → Check API endpoint consistency
   ├── Load test failure? → Optimize performance or scaling
   ├── Security test failure? → Fix authentication/authorization
   └── Performance failure? → Optimize database queries or caching
```

## Performance Targets

### Generation Performance
- **Route Generation**: < 1 second
- **Service Generation**: < 2 seconds
- **Model Generation**: < 1 second
- **Complete API Pipeline**: < 10 seconds

### Test Performance
- **Unit Tests**: < 100ms each, < 10 seconds total
- **Integration Tests**: < 2 seconds each, < 5 minutes total
- **Load Tests**: < 30 seconds each, < 10 minutes total
- **Security Tests**: < 5 seconds each, < 2 minutes total
- **Full Test Suite**: < 20 minutes total

### Quality Metrics
- **Test Coverage**: 90%+ for new code
- **Python Type Checking**: 0 mypy errors
- **Linting**: 0 flake8/black warnings
- **Security Compliance**: 0 security vulnerabilities
- **API Documentation**: 100% OpenAPI coverage
- **1:1:1 Relationship**: 100% maintained

## AI Assistant Best Practices

### Context Loading
1. **Always load** `@conventions` files first
2. **Reference** `@prompts/@api-creation.md` for workflows
3. **Check** existing APIs before creating new ones
4. **Validate** against `@testing-protocol` requirements
5. **Review** `@fastapi-conventions.md` for patterns

### Quality Assurance
1. **Generate** complete test suites for all APIs (unit + integration + load + security)
2. **Run** validation scripts after creation
3. **Check** performance and security targets are met
4. **Ensure** API documentation compliance
5. **Validate** authentication and authorization

### Error Prevention
1. **Follow** FastAPI naming conventions strictly
2. **Maintain** 1:1:1 relationship always
3. **Use** automation scripts for consistency
4. **Validate** security patterns before deployment
5. **Check** database migration compatibility
