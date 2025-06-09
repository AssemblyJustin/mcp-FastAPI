# @api-creation

**AI Context**: FastAPI API creation workflow and prompts. ALWAYS load core conventions first.

## ⚠️ CRITICAL: Pre-Creation Checklist
**MANDATORY steps before creating ANY API component**:
1. 🔥 **Load `.ai-docs/@core/@conventions.md`** (ALWAYS FIRST)
2. 🔥 **Load `.ai-docs/@conventions/@fastapi-conventions.md`** (FastAPI patterns)
3. ✅ **Check existing APIs** in `backend-mcp/code-examples/`
4. ✅ **Verify naming conventions** match FastAPI standards
5. ✅ **Confirm 1:1:1 relationship** (example → blueprint → test)

## API Creation Workflow

### Step 1: Determine API Type
```
Route Creation:
├── CRUD operations? → Use crud-route blueprint
├── Authentication? → Use auth-route blueprint
├── File upload? → Use upload-route blueprint
└── Custom logic? → Use custom-route blueprint

Service Creation:
├── Business logic? → Use service blueprint
├── Data processing? → Use processor-service blueprint
├── External API? → Use client-service blueprint
└── Background task? → Use task-service blueprint

Model Creation:
├── Database entity? → Use sqlalchemy-model blueprint
├── API request/response? → Use pydantic-model blueprint
├── Configuration? → Use config-model blueprint
└── Validation schema? → Use validation-model blueprint
```

### Step 2: Create Smart Blueprint
**Location**: `backend-mcp/blueprints/[category]/smart-[name].json`

**Smart Blueprint Structure**:
```json
{
  "id": "smart-{{layer}}-{{resourceName}}",
  "strategy": "embedded-template",
  "codeTemplate": {
    "language": "python",
    "executable": true,
    "content": "# Embedded Python code here"
  }
}
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from ...models import {{modelName}}, {{modelName}}Create, {{modelName}}Update
from ...services import {{modelName}}Service
from ...dependencies import get_current_user, get_db

router = APIRouter(
    prefix="/{{routePrefix}}",
    tags=["{{resourceName}}"]
)

@router.{{httpMethod.lower()}}("/{{endpoint}}")
async def {{functionName}}(
    {{#if requestModel}}request: {{requestModel}},{{/if}}
    {{#if authRequired}}current_user: User = Depends(get_current_user),{{/if}}
    db: Session = Depends(get_db)
) -> {{responseModel}}:
    """
    {{description}}
    
    Args:
        {{#if requestModel}}request: {{requestModel}} - Request data{{/if}}
        {{#if authRequired}}current_user: User - Authenticated user{{/if}}
        db: Session - Database session
    
    Returns:
        {{responseModel}}: {{responseDescription}}
    
    Raises:
        HTTPException: 400 for validation errors
        HTTPException: 401 for authentication errors
        HTTPException: 404 for not found
        HTTPException: 500 for server errors
    """
    try:
        service = {{modelName}}Service(db)
        result = await service.{{operationName}}({{parameters}})
        return result
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except PermissionError as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=str(e)
        )
    except Exception as e:
        logger.error(f"Error in {{functionName}}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )
```

### Step 3: Add Test Template
**Embedded in Smart Blueprint**:

**Blueprint Structure**:
```json
{
  "id": "create-{{resourceName}}-route",
  "name": "Create {{modelName}} Route",
  "description": "Create FastAPI route for {{resourceName}} operations",
  "version": "1.0.0",
  "parameters": {
    "required": ["resourceName", "modelName", "httpMethod", "endpoint"],
    "optional": ["authRequired", "routePrefix", "responseModel"],
    "resourceName": {
      "type": "string",
      "description": "Resource name in snake_case",
      "required": true,
      "pattern": "^[a-z][a-z0-9_]*$"
    },
    "modelName": {
      "type": "string", 
      "description": "Pydantic model name in PascalCase",
      "required": true,
      "pattern": "^[A-Z][a-zA-Z0-9]*$"
    },
    "httpMethod": {
      "type": "string",
      "description": "HTTP method",
      "required": true,
      "enum": ["GET", "POST", "PUT", "DELETE", "PATCH"]
    },
    "endpoint": {
      "type": "string",
      "description": "API endpoint path",
      "required": true,
      "pattern": "^/[a-z0-9/_-]*$"
    },
    "authRequired": {
      "type": "boolean",
      "description": "Whether authentication is required",
      "default": true
    },
    "routePrefix": {
      "type": "string",
      "description": "API route prefix",
      "default": "/api/v1"
    },
    "responseModel": {
      "type": "string",
      "description": "Response model type",
      "default": "{{modelName}}Response"
    }
  },
  "template": "fastapi/route_template.py",
  "codeExample": "api/routes/{{resourceName}}_routes.py",
  "validation": {
    "syntax": ["python", "fastapi", "pydantic"],
    "required": ["proper-typing", "error-handling", "authentication", "documentation"],
    "forbidden": ["hardcoded-secrets", "sql-injection-risk", "missing-validation"],
    "security": ["input-validation", "authentication-check", "authorization-check"]
  },
  "rollback": {
    "strategy": "delete-file",
    "checkpoints": ["before-creation", "after-validation", "after-testing"]
  },
  "metadata": {
    "estimatedTokens": 2500,
    "estimatedComplexity": 7,
    "dependencies": ["pydantic-models", "service-layer", "database-session"],
    "tags": ["api", "route", "{{resourceName}}"]
  }
}
```

### Step 4: Generate Test Files
**Generated from Smart Blueprint**:
- `tests/unit/test_{{resourceName}}_service.py` - Unit tests
- `tests/integration/test_{{resourceName}}_api.py` - Integration tests
- `tests/load/test_{{resourceName}}_load.py` - Load tests
- `tests/security/test_{{resourceName}}_security.py` - Security tests

**Unit Test Template**:
```python
# File: tests/unit/test_{{resourceName}}_service.py
import pytest
from unittest.mock import Mock, patch, AsyncMock
from backend_mcp.services.{{resourceName}}_service import {{modelName}}Service
from backend_mcp.models.{{resourceName}}_models import {{modelName}}Create, {{modelName}}Update

class Test{{modelName}}Service:
    @pytest.fixture
    def mock_db(self):
        return Mock()
    
    @pytest.fixture
    def service(self, mock_db):
        return {{modelName}}Service(mock_db)
    
    @pytest.fixture
    def sample_{{resourceName}}_data(self):
        return {{modelName}}Create(
            {{#each sampleFields}}
            {{name}}={{value}},
            {{/each}}
        )
    
    @pytest.mark.asyncio
    async def test_create_{{resourceName}}_success(self, service, sample_{{resourceName}}_data):
        """Test successful {{resourceName}} creation"""
        # Arrange
        expected_result = Mock()
        service.db.add = Mock()
        service.db.commit = Mock()
        service.db.refresh = Mock()
        
        # Act
        result = await service.create_{{resourceName}}(sample_{{resourceName}}_data)
        
        # Assert
        assert result is not None
        service.db.add.assert_called_once()
        service.db.commit.assert_called_once()
        service.db.refresh.assert_called_once()
    
    @pytest.mark.asyncio
    async def test_get_{{resourceName}}_by_id_found(self, service):
        """Test getting {{resourceName}} by ID when found"""
        # Arrange
        {{resourceName}}_id = 1
        expected_{{resourceName}} = Mock()
        service.db.query.return_value.filter.return_value.first.return_value = expected_{{resourceName}}
        
        # Act
        result = await service.get_{{resourceName}}({{resourceName}}_id)
        
        # Assert
        assert result == expected_{{resourceName}}
        service.db.query.assert_called_once()
    
    @pytest.mark.asyncio
    async def test_get_{{resourceName}}_by_id_not_found(self, service):
        """Test getting {{resourceName}} by ID when not found"""
        # Arrange
        {{resourceName}}_id = 999
        service.db.query.return_value.filter.return_value.first.return_value = None
        
        # Act
        result = await service.get_{{resourceName}}({{resourceName}}_id)
        
        # Assert
        assert result is None
```

**Integration Test Template**:
```python
# File: tests/integration/test_{{resourceName}}_api.py
import pytest
from fastapi.testclient import TestClient
from backend_mcp.main import app
from backend_mcp.database import get_db
from tests.conftest import override_get_db, test_db

client = TestClient(app)
app.dependency_overrides[get_db] = override_get_db

class Test{{modelName}}API:
    def test_create_{{resourceName}}_success(self, test_db):
        """Test creating {{resourceName}} via API"""
        {{resourceName}}_data = {
            {{#each sampleFields}}
            "{{name}}": {{jsonValue}},
            {{/each}}
        }
        
        response = client.post("/{{routePrefix}}/{{resourceName}}s", json={{resourceName}}_data)
        
        assert response.status_code == 201
        response_data = response.json()
        assert "id" in response_data
        {{#each sampleFields}}
        assert response_data["{{name}}"] == {{resourceName}}_data["{{name}}"]
        {{/each}}
    
    def test_create_{{resourceName}}_validation_error(self):
        """Test creating {{resourceName}} with invalid data"""
        invalid_data = {
            # Missing required fields or invalid values
        }
        
        response = client.post("/{{routePrefix}}/{{resourceName}}s", json=invalid_data)
        
        assert response.status_code == 422
        assert "detail" in response.json()
    
    def test_get_{{resourceName}}_success(self, test_db):
        """Test getting {{resourceName}} by ID"""
        # First create a {{resourceName}}
        {{resourceName}}_data = {
            {{#each sampleFields}}
            "{{name}}": {{jsonValue}},
            {{/each}}
        }
        create_response = client.post("/{{routePrefix}}/{{resourceName}}s", json={{resourceName}}_data)
        {{resourceName}}_id = create_response.json()["id"]
        
        # Then get it
        response = client.get(f"/{{routePrefix}}/{{resourceName}}s/{{{resourceName}}_id}")
        
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["id"] == {{resourceName}}_id
    
    def test_get_{{resourceName}}_not_found(self):
        """Test getting non-existent {{resourceName}}"""
        response = client.get("/{{routePrefix}}/{{resourceName}}s/999999")
        
        assert response.status_code == 404
        assert "not found" in response.json()["detail"].lower()
```

### Step 5: Validation
**Run validation scripts**:
```bash
# Validate smart blueprint
python scripts/validate_smart_blueprint.py --blueprint smart-{{layer}}-{{resourceName}}.json

# Test embedded template
python scripts/smart_blueprint_processor.py smart-{{layer}}-{{resourceName}}.json test

# Extract code example for review
python scripts/smart_blueprint_processor.py smart-{{layer}}-{{resourceName}}.json extract

# Run generated tests
python -m pytest tests/unit/test_{{resourceName}}_service.py -v
python -m pytest tests/integration/test_{{resourceName}}_api.py -v
```

## Common API Patterns

### CRUD Route Pattern
```python
# GET /resources - List resources
@router.get("/{{resourceName}}s", response_model=List[{{modelName}}Response])
async def list_{{resourceName}}s(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):

# GET /resources/{id} - Get resource by ID  
@router.get("/{{resourceName}}s/{{{resourceName}}_id}", response_model={{modelName}}Response)
async def get_{{resourceName}}(
    {{resourceName}}_id: int,
    db: Session = Depends(get_db)
):

# POST /resources - Create resource
@router.post("/{{resourceName}}s", response_model={{modelName}}Response, status_code=201)
async def create_{{resourceName}}(
    {{resourceName}}: {{modelName}}Create,
    db: Session = Depends(get_db)
):

# PUT /resources/{id} - Update resource
@router.put("/{{resourceName}}s/{{{resourceName}}_id}", response_model={{modelName}}Response)
async def update_{{resourceName}}(
    {{resourceName}}_id: int,
    {{resourceName}}: {{modelName}}Update,
    db: Session = Depends(get_db)
):

# DELETE /resources/{id} - Delete resource
@router.delete("/{{resourceName}}s/{{{resourceName}}_id}", status_code=204)
async def delete_{{resourceName}}(
    {{resourceName}}_id: int,
    db: Session = Depends(get_db)
):
```

### Authentication Route Pattern
```python
@router.post("/login", response_model=TokenResponse)
async def login(
    credentials: LoginRequest,
    db: Session = Depends(get_db)
):

@router.post("/register", response_model=UserResponse, status_code=201)
async def register(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):

@router.post("/refresh", response_model=TokenResponse)
async def refresh_token(
    refresh_token: str,
    db: Session = Depends(get_db)
):

@router.post("/logout", status_code=204)
async def logout(
    current_user: User = Depends(get_current_user)
):
```

## AI Assistant Prompts

### Route Creation Prompt
```
Create a FastAPI route for {{resourceName}} with the following specifications:
- HTTP Method: {{httpMethod}}
- Endpoint: {{endpoint}}
- Authentication: {{authRequired}}
- Request Model: {{requestModel}}
- Response Model: {{responseModel}}

Follow the 1:1:1 relationship:
1. Create code example in backend-mcp/code-examples/api/routes/
2. Create blueprint in backend-mcp/blueprints/api/routes/
3. Create test suite in tests/ (unit + integration + load + security)
4. Validate with scripts/validate_api_pipeline.py
```

### Service Creation Prompt
```
Create a FastAPI service for {{resourceName}} with the following operations:
- CRUD operations: {{operations}}
- Business logic: {{businessLogic}}
- External dependencies: {{dependencies}}

Include proper error handling, logging, and async/await patterns.
Follow FastAPI service conventions and maintain 1:1:1 relationship.
```

### Model Creation Prompt
```
Create Pydantic models for {{resourceName}} with the following fields:
- Fields: {{fields}}
- Validation rules: {{validationRules}}
- Database mapping: {{databaseMapping}}

Create Base, Create, Update, and Response models.
Include proper validation and documentation.
```

## Quality Gates

### Pre-Creation Validation
1. ✅ **Naming conventions** match FastAPI standards
2. ✅ **Directory structure** follows backend-mcp organization
3. ✅ **Dependencies** are properly defined
4. ✅ **Security patterns** are included

### Post-Creation Validation
1. ✅ **Code compiles** without errors
2. ✅ **Tests pass** (unit + integration + load + security)
3. ✅ **API documentation** is auto-generated
4. ✅ **Performance targets** are met
5. ✅ **Security scans** pass
6. ✅ **1:1:1 relationship** is maintained
