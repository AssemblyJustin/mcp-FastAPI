# AI-First FastAPI MCP Development Standards (LEGACY)

**⚠️ NOTICE**: This file contains legacy concepts. Current standards are in:
- **`.ai-docs/@core/MASTER_CONVENTIONS.md`** - All current conventions
- **`.ai-docs/@core/MASTER_TESTING.md`** - All current testing protocols
- **`.ai-docs/@core/MASTER_ARCHITECTURE.md`** - All current architecture patterns

## Overview
This document establishes AI-optimized standards for FastAPI MCP development, prioritizing AI code generation efficiency, speed, and accuracy for backend API development. Every aspect is designed to minimize AI context overhead while maximizing FastAPI code generation predictability and quality.

**Core Principle**: Zero file resolution overhead, embedded context, direct AI execution with maintainable FastAPI code examples.

## AI-First Philosophy

### Design Principles
- **Embedded Context**: All required information embedded directly in smart blueprints
- **Smart Blueprint-Based**: Standardized, reusable code generation with embedded templates
- **Zero Ambiguity**: Precise, structured instructions with no interpretation needed
- **Minimal Overhead**: Optimized for AI context window efficiency
- **Direct Execution**: AI can execute tasks without external file reading during generation
- **Single Source Truth**: Code templates embedded in blueprints, no separate examples

### AI Optimization Goals
- **Sub-second Task Resolution**: No external lookups or file reads during execution
- **Predictable Code Generation**: Smart blueprint-based consistency with embedded templates
- **Context Window Efficiency**: Minimal token usage for maximum output
- **Batch Processing Capable**: Multiple tasks executed efficiently
- **Error Recovery Built-in**: Automatic rollback and validation
- **Developer-Friendly**: Extractable code examples with full IDE support

## 1. AI-First Task Structure

### Core Task Schema
```json
{
  "id": "string",
  "blueprint": "blueprint-identifier",
  "parameters": {
    // All context embedded - no external resolution required during execution
  },
  "metadata": {
    "priority": "high|medium|low",
    "estimatedTokens": "number",
    "dependencies": ["task-ids"]
  },
  "validation": {
    "syntax": "validation-rules",
    "quality": "quality-gates"
  },
  "rollback": {
    "strategy": "rollback-approach",
    "checkpoints": ["checkpoint-definitions"]
  }
}
```

### FastAPI MCP Blueprint Library Structure

Blueprints and code examples are separated for maintainability:

```
backend-mcp/
├── blueprints/
│   ├── api/
│   │   ├── routes/
│   │   │   ├── create-crud-route.json
│   │   │   ├── create-auth-route.json
│   │   │   └── create-upload-route.json
│   │   ├── services/
│   │   │   ├── create-business-service.json
│   │   │   ├── create-auth-service.json
│   │   │   └── create-data-service.json
│   │   └── models/
│   │       ├── create-pydantic-model.json
│   │       ├── create-sqlalchemy-model.json
│   │       └── create-response-model.json
│   ├── middleware/
│   │   ├── create-auth-middleware.json
│   │   ├── create-cors-middleware.json
│   │   └── create-rate-limit-middleware.json
│   └── database/
│       ├── create-migration.json
│       └── create-repository.json
└── code-examples/
    ├── api/
    │   ├── routes/
    │   │   ├── user_routes.py
    │   │   ├── auth_routes.py
    │   │   ├── product_routes.py
    │   │   └── upload_routes.py
    │   ├── services/
    │   │   ├── user_service.py
    │   │   ├── auth_service.py
    │   │   ├── product_service.py
    │   │   └── email_service.py
    │   └── models/
    │       ├── user_models.py
    │       ├── product_models.py
    │       └── auth_models.py
    ├── middleware/
    │   ├── auth_middleware.py
    │   ├── cors_middleware.py
    │   └── rate_limit_middleware.py
    └── database/
        ├── migrations/
        └── repositories/
```

### Blueprint-Based Task Examples

#### FastAPI Route Task
```json
{
  "id": "B-001",
  "blueprint": "smart-route-crud",
  "parameters": {
    "resourceName": "user",
    "modelName": "User",
    "routePrefix": "/api/v1",
    "authRequired": true,
    "httpMethods": ["GET", "POST", "PUT", "DELETE"]
  },
  "validation": {
    "syntax": "python-fastapi",
    "quality": ["flake8", "black", "mypy"]
  }
}
```

#### FastAPI Service Task
```json
{
  "id": "B-002",
  "blueprint": "smart-service-business",
  "parameters": {
    "serviceName": "UserService",
    "resourceName": "user",
    "modelName": "User",
    "operations": ["create", "read", "update", "delete", "list"],
    "businessLogic": ["validation", "authentication", "authorization"]
  },
  "validation": {
    "syntax": "python",
    "quality": ["flake8", "black", "mypy"],
    "security": ["bandit"]
  }
}
```

#### Backend API Task
```json
{
  "id": "B-001",
  "blueprint": "add-fastapi-endpoint",
  "parameters": {
    "targetFile": "api/auth/routes.py",
    "codeExample": "backend/api/auth-endpoint.py",
    "method": "POST",
    "path": "/login",
    "functionName": "login_user",
    "parameterization": {
      "endpoint": "/login",
      "method": "POST",
      "requestSchema": "LoginRequest",
      "responseSchema": "LoginResponse"
    },
    "requestSchema": {
      "name": "LoginRequest",
      "fields": {
        "email": "str",
        "password": "str"
      }
    },
    "responseSchema": {
      "name": "LoginResponse", 
      "fields": {
        "token": "str",
        "user": "UserResponse"
      }
    },
    "requiredImports": [
      { "name": "FastAPI", "from": "fastapi" },
      { "name": "LoginRequest", "from": ".schemas" }
    ],
    "middleware": ["authenticate_user"],
    "errorHandling": "standard-auth-errors"
  }
}
```

## 2. Code Examples Structure

### Code Example Files

Code examples are maintainable TypeScript/Python files that can be linted, formatted, and tested:

**Smart Blueprint with Embedded Template**:
```json
{
  "id": "smart-route-user",
  "codeTemplate": {
    "language": "python",
    "content": "from fastapi import APIRouter, Depends, HTTPException\nfrom typing import List\nfrom ..models import {{modelName}}Create, {{modelName}}Response\nfrom ..services import {{modelName}}Service\n\nrouter = APIRouter(prefix=\"{{routePrefix}}/{{resourceName}}s\")\n\n@router.get(\"/\", response_model=List[{{modelName}}Response])\nasync def list_{{resourceName}}s(\n    service: {{modelName}}Service = Depends()\n) -> List[{{modelName}}Response]:\n    items = await service.get_{{resourceName}}s()\n    return [{{modelName}}Response.from_orm(item) for item in items]"
  }
}
```

**`code-examples/backend/api/auth-endpoint.py`**:
```python
from fastapi import APIRouter, HTTPException, Depends
from ..schemas import {{requestSchema}}, {{responseSchema}}
from ..services import AuthService

router = APIRouter()

@router.{{method.lower()}}("{{endpoint}}")
async def {{functionName}}(request: {{requestSchema}}) -> {{responseSchema}}:
    """
    {{endpoint}} endpoint implementation
    """
    try:
        # Authentication logic here
        auth_service = AuthService()
        result = await auth_service.authenticate(request.email, request.password)
        
        if not result.success:
            raise HTTPException(status_code=401, detail="Invalid credentials")
            
        return {{responseSchema}}(
            token=result.token,
            user=result.user
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

### Smart Blueprint Categories

#### API Layer Blueprints
- **smart-route-crud**: Complete CRUD API endpoints
- **smart-route-auth**: Authentication endpoints
- **smart-route-upload**: File upload endpoints
- **smart-route-custom**: Custom business logic endpoints

#### Service Layer Blueprints
- **smart-service-business**: Business logic service
- **smart-service-data**: Data access service
- **smart-service-auth**: Authentication service
- **smart-service-external**: External API integration

#### Model Layer Blueprints
- **smart-model-pydantic**: Pydantic validation models
- **smart-model-sqlalchemy**: SQLAlchemy ORM models
- **smart-model-response**: API response models

#### Infrastructure Blueprints
- **smart-middleware-auth**: Authentication middleware
- **smart-middleware-cors**: CORS configuration
- **smart-database-migration**: Database migrations
- **smart-background-task**: Background job processing

#### Infrastructure Blueprints
- **add-docker-service**: Add Docker service
- **add-k8s-deployment**: Add Kubernetes deployment
- **add-terraform-resource**: Add infrastructure resource
- **add-github-action**: Add CI/CD workflow

### Blueprint Parameter Standards
```typescript
interface BlueprintParameters {
  // File operations
  targetFile: string
  insertionStrategy: "after-element" | "before-element" | "replace" | "append" | "prepend" | "create-file"
  insertionTarget?: ElementSelector

  // Code generation
  codeExample: string  // Path to code example file
  parameterization: Record<string, any>  // Parameters for code example substitution
  requiredImports: ImportStatement[]
  contextBefore: string
  contextAfter: string

  // Validation
  syntaxValidation: string[]
  qualityGates: string[]

  // Metadata
  estimatedComplexity: number
  tokenUsage: number
}
```

## 3. AI Execution Workflow

### Blueprint Resolution Process
```typescript
// Step 1: Blueprint and Code Example Resolution (pre-loaded, 0 external reads during execution)
const blueprint = BLUEPRINT_LIBRARY[task.blueprint]
const codeExample = CODE_EXAMPLES[task.parameters.codeExample]
const resolvedTask = blueprint.resolve(task.parameters)

// Step 2: Code Generation (direct execution with parameterization)
const parameterizedCode = blueprint.parameterize(codeExample, resolvedTask.parameters.parameterization)
const generatedCode = blueprint.generate(parameterizedCode, resolvedTask.parameters)

// Step 3: Validation (built-in)
const validation = blueprint.validate(generatedCode)

// Step 4: Application (with rollback)
const result = applyChanges(generatedCode, {
  rollback: resolvedTask.rollback,
  validation: validation
})
```

### Code Example Parameterization
```typescript
interface CodeParameterization {
  // Component parameterization
  componentName: string
  propsInterface: string
  defaultProps: Record<string, any>
  
  // API parameterization
  endpoint: string
  method: string
  requestSchema: string
  responseSchema: string
  functionName: string
  
  // Custom replacements
  customReplacements: Record<string, string>
}

// Example parameterization process
function parameterizeCode(codeExample: string, params: CodeParameterization): string {
  let result = codeExample
  
  // Replace template variables
  result = result.replace(//{/{componentName/}/}/g, params.componentName)
  result = result.replace(//{/{propsInterface/}/}/g, params.propsInterface)
  result = result.replace(//{/{defaultProps/.(/w+)/}/}/g, (match, prop) => params.defaultProps[prop])
  
  // Apply custom replacements
  Object.entries(params.customReplacements || {}).forEach(([key, value]) => {
    result = result.replace(new RegExp(`/{/{${key}/}/}`, 'g'), value)
  })
  
  return result
}
```

### Batch Processing
```json
{
  "batchOperation": {
    "id": "feature-authentication",
    "tasks": [
      { "id": "B-001", "blueprint": "add-fastapi-endpoint", "codeExample": "backend/api/auth-endpoint.py" },
      { "id": "F-001", "blueprint": "add-react-component", "codeExample": "frontend/atoms/Button.tsx" },
      { "id": "T-001", "blueprint": "add-test-suite", "codeExample": "tests/auth-test.py" }
    ],
    "execution": "sequential",
    "failureStrategy": "rollback-all",
    "dependencies": {
      "F-001": ["B-001"],
      "T-001": ["B-001", "F-001"]
    }
  }
}
```

## 4. Enhanced TaskMaster MCP Tools

### AI-Optimized Tools
```typescript
// Ultra-fast blueprint-based generation with code examples
mcp_taskmaster_generate_from_blueprint(
  blueprintId: string,
  parameters: BlueprintParameters,
  options?: {
    stagingArea?: string,
    validateImmediately?: boolean,
    autoFormat?: boolean,
    dryRun?: boolean
  }
): Promise<GenerationResult>

// Code example management
mcp_taskmaster_list_code_examples(
  category?: string,
  language?: string
): Promise<CodeExample[]>

mcp_taskmaster_validate_code_example(
  examplePath: string,
  blueprintId: string
): Promise<ValidationResult>

// Batch blueprint execution
mcp_taskmaster_execute_blueprint_sequence(
  tasks: BlueprintTask[],
  options?: {
    executionStrategy?: "sequential" | "parallel",
    failureStrategy?: "continue" | "rollback-all" | "rollback-failed",
    maxConcurrency?: number
  }
): Promise<BatchResult>

// Blueprint validation and optimization
mcp_taskmaster_validate_blueprint(
  blueprintId: string,
  parameters: BlueprintParameters
): Promise<ValidationResult>

// Blueprint performance analysis
mcp_taskmaster_analyze_blueprint_performance(
  blueprintId: string,
  metrics?: PerformanceMetrics
): Promise<PerformanceAnalysis>
```

## 5. Quality Gates and Validation

### Built-in Validation Pipeline
```json
{
  "validationPipeline": {
    "syntax": {
      "typescript": ["tsc", "--noEmit"],
      "python": ["mypy", "flake8"],
      "yaml": ["yamllint"]
    },
    "quality": {
      "frontend": ["eslint", "prettier", "jest"],
      "backend": ["black", "isort", "pytest"],
      "infrastructure": ["terraform validate", "hadolint"]
    },
    "security": {
      "dependencies": ["npm audit", "safety"],
      "code": ["semgrep", "bandit"]
    },
    "performance": {
      "build": ["webpack-bundle-analyzer"],
      "runtime": ["lighthouse", "load-testing"]
    }
  }
}
```

### Error Recovery
```json
{
  "errorRecovery": {
    "strategies": {
      "syntax-error": "rollback-immediate",
      "quality-failure": "fix-and-retry",
      "security-issue": "rollback-and-alert",
      "performance-degradation": "rollback-and-optimize"
    },
    "rollbackCheckpoints": [
      "before-generation",
      "after-validation",
      "before-application"
    ],
    "maxRetries": 3,
    "backoffStrategy": "exponential"
  }
}
```

## 6. Performance Optimization

### Context Window Management
```typescript
interface ContextOptimization {
  maxTokensPerTask: number
  embeddedContextLimit: number
  templateCaching: boolean
  parameterCompression: boolean
  batchSizeOptimization: boolean
}

const AI_OPTIMIZATION_CONFIG = {
  maxTokensPerTask: 2000,
  embeddedContextLimit: 1500,
  templateCaching: true,
  parameterCompression: true,
  batchSizeOptimization: true
}
```

### Blueprint Caching
```typescript
interface BlueprintCacheStrategy {
  cacheLevel: "memory" | "disk" | "distributed"
  ttl: number
  invalidationStrategy: "time-based" | "content-based"
  compressionEnabled: boolean
}
```

### Conversion Guidelines
```typescript
// OLD: Human-centric task
{
  "description": "Add login button to header using primary button pattern",
  "tags": ["@Header", "@Button", "@primaryButton"]
}

// NEW: AI-optimized blueprint task with code example reference
{
  "blueprint": "add-react-component",
  "parameters": {
    "targetFile": "components/Header.tsx",
    "codeExample": "frontend/atoms/Button.tsx",
    "component": { "name": "Button", "props": { "variant": "primary" } },
    "insertionTarget": { "element": "nav", "occurrence": 1 }
  }
}
```

### Code Example Creation Guidelines
```typescript
// Code examples should be:
// 1. Valid, lintable code files
// 2. Use template variables for parameterization: {{variableName}}
// 3. Include proper TypeScript/Python types
// 4. Follow project coding standards
// 5. Be testable independently

// Example: Button.tsx
export const {{componentName}}: React.FC<{{propsInterface}}> = ({{props}}) => {
  return (
    <button 
      className={`btn btn-{{variant}} {{className}}`}
      onClick={{onClick}}
      disabled={{disabled}}
    >
      {{children}}
    </button>
  );
};
```

## 8. Success Metrics

### AI Performance KPIs
- **Generation Speed**: < 2 seconds per task
- **Accuracy Rate**: > 95% first-attempt success
- **Context Efficiency**: < 1500 tokens per task
- **Batch Throughput**: > 10 tasks per minute
- **Error Rate**: < 2% requiring manual intervention

### Quality Metrics
- **Code Quality**: 100% passing linting and formatting on generated code
- **Test Coverage**: > 90% for generated code
- **Security Compliance**: 0 security vulnerabilities
- **Performance**: No performance degradation
- **Developer Experience**: Code examples maintainable with standard tooling

### Blueprint Library Metrics
- **Code Example Coverage**: All blueprints have corresponding, tested examples
- **Blueprint Accuracy**: > 98% successful parameterization
- **Example Maintainability**: Code examples pass linting and can be independently tested
- **Version Consistency**: Blueprints and examples stay synchronized


