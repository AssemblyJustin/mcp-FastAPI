# @smart-blueprint-system

**AI Context**: Complete Smart Blueprint system architecture for AI-first FastAPI development.

## Smart Blueprint Philosophy

### Core Principle
**Single Source of Truth**: All code generation information embedded in one JSON file for maximum AI efficiency.

### Why Smart Blueprints?
- **3x Faster Generation**: Single file load vs. multiple file correlation
- **50% Fewer Tokens**: Embedded context vs. separate files  
- **Zero Sync Issues**: No blueprint-to-example relationship to maintain
- **Better AI Caching**: One file to cache vs. multiple
- **Simpler Architecture**: Fewer moving parts, easier maintenance

## Smart Blueprint Structure

### Complete Blueprint Format
```json
{
  "id": "smart-[layer]-[resource]",
  "name": "Human-readable name",
  "description": "Purpose and usage description",
  "version": "1.0.0",
  "strategy": "embedded-template",
  
  "parameters": {
    "resourceName": {
      "type": "string",
      "required": true,
      "pattern": "^[a-z][a-z0-9_]*$",
      "description": "Resource name in snake_case"
    },
    "modelName": {
      "type": "string",
      "required": true,
      "pattern": "^[A-Z][a-zA-Z0-9]*$",
      "description": "Model name in PascalCase"
    },
    "authRequired": {
      "type": "boolean",
      "default": true,
      "description": "Whether authentication is required"
    }
  },
  
  "codeTemplate": {
    "language": "python",
    "executable": true,
    "testable": true,
    "content": "# Embedded Python code with {{variables}} and {{#if conditions}}"
  },
  
  "testTemplate": {
    "language": "python",
    "framework": "pytest",
    "content": "# Embedded test code"
  },
  
  "validation": {
    "syntax": ["python", "fastapi", "pydantic"],
    "required": ["proper-typing", "error-handling"],
    "forbidden": ["hardcoded-secrets"],
    "security": ["input-validation", "authentication-check"]
  },
  
  "metadata": {
    "estimatedTokens": 1200,
    "estimatedComplexity": 5,
    "generationTime": "<1s",
    "aiOptimized": true,
    "tags": ["api", "crud", "{{resourceName}}"]
  }
}
```

## Template Variable System

### Standard Variables
- `{{resourceName}}` - Resource name (snake_case): `user`, `product`
- `{{modelName}}` - Model name (PascalCase): `User`, `Product`
- `{{httpMethod}}` - HTTP method: `GET`, `POST`, `PUT`, `DELETE`
- `{{routePrefix}}` - API prefix: `/api/v1`, `/admin/api`
- `{{authRequired}}` - Boolean for conditional logic
- `{{responseModel}}` - Response model type: `UserResponse`

### Conditional Blocks
```python
# Authentication conditional
{{#if authRequired}}
current_user: User = Depends(get_current_user),
{{/if}}

# HTTP method conditional
{{#if httpMethod == "POST"}}
@router.post("/{{resourceName}}s", status_code=201)
{{else}}
@router.get("/{{resourceName}}s")
{{/if}}
```

### Loop Blocks
```python
# Field iteration
{{#each fields}}
{{name}}: {{type}}{{#if optional}} = None{{/if}}
{{/each}}
```

## Blueprint Categories

### API Layer Blueprints
```
backend-mcp/blueprints/api/
├── routes/
│   ├── smart-crud-route.json      # Complete CRUD operations
│   ├── smart-auth-route.json      # Authentication endpoints
│   ├── smart-upload-route.json    # File upload endpoints
│   └── smart-custom-route.json    # Custom business logic
├── services/
│   ├── smart-business-service.json # Business logic service
│   ├── smart-data-service.json     # Data access service
│   └── smart-auth-service.json     # Authentication service
└── models/
    ├── smart-pydantic-model.json   # Pydantic models
    ├── smart-sqlalchemy-model.json # SQLAlchemy models
    └── smart-response-model.json   # API response models
```

### Infrastructure Blueprints
```
backend-mcp/blueprints/
├── middleware/
│   ├── smart-auth-middleware.json
│   ├── smart-cors-middleware.json
│   └── smart-rate-limit-middleware.json
├── database/
│   ├── smart-migration.json
│   ├── smart-repository.json
│   └── smart-connection.json
└── auth/
    ├── smart-jwt-auth.json
    ├── smart-oauth-auth.json
    └── smart-api-key-auth.json
```

## Development Workflow

### 1. Create Smart Blueprint
```bash
# Create new smart blueprint
cp templates/smart-blueprint-template.json backend-mcp/blueprints/api/routes/smart-route-user.json

# Edit parameters and embedded template
# No separate code example needed
```

### 2. Validate Blueprint
```bash
# Validate template syntax
python scripts/smart_blueprint_processor.py smart-route-user.json validate

# Test template with sample data
python scripts/smart_blueprint_processor.py smart-route-user.json test
```

### 3. Extract Code Example (Optional)
```bash
# Extract clean code for development/review
python scripts/smart_blueprint_processor.py smart-route-user.json extract user_routes.py

# Edit extracted file with full IDE support
# Changes must be manually synced back to blueprint
```

### 4. Generate Code
```bash
# Generate from blueprint
python scripts/generate_from_smart_blueprint.py smart-route-user.json --params '{"resourceName": "user", "modelName": "User"}'

# Output: Generated code ready for use
```

## AI Integration Benefits

### Context Loading Efficiency
```python
# OLD: Multiple file loads
blueprint = load_blueprint("create-user-route.json")
example = load_code_example("user_routes.py") 
test = load_test_template("test_user_routes.py")
# Total: 3 file reads, correlation overhead

# NEW: Single file load
smart_blueprint = load_smart_blueprint("smart-route-user.json")
# Total: 1 file read, embedded context
```

### Token Usage Optimization
```
OLD Approach:
- Blueprint JSON: 800 tokens
- Code Example: 1200 tokens  
- Test Template: 600 tokens
- Correlation overhead: 400 tokens
Total: 3000 tokens

NEW Approach:
- Smart Blueprint: 1200 tokens
- No correlation needed: 0 tokens
Total: 1200 tokens (60% reduction)
```

### Generation Speed
```
OLD: Load blueprint → Load example → Correlate → Generate (2-3 seconds)
NEW: Load smart blueprint → Generate (<1 second)
```

## Quality Assurance

### Embedded Validation
```json
{
  "validation": {
    "syntax": ["python", "fastapi", "pydantic"],
    "linting": ["flake8", "black", "mypy"],
    "security": ["bandit", "safety"],
    "testing": ["pytest"],
    "performance": ["response-time", "memory-usage"]
  }
}
```

### Automated Testing
```bash
# Test embedded template
python scripts/smart_blueprint_processor.py blueprint.json test

# Validate all blueprints
python scripts/validate_all_smart_blueprints.py

# Performance benchmarks
python scripts/benchmark_smart_blueprints.py
```

## Migration Strategy

### Phase 1: Parallel Development
- Keep existing code-examples for reference
- Create smart blueprints alongside
- Compare generation quality and speed

### Phase 2: Gradual Migration
- Migrate high-use blueprints first
- Measure performance improvements
- Update documentation and workflows

### Phase 3: Complete Transition
- Remove code-examples directory
- Update all scripts and tools
- Full smart blueprint adoption

## Developer Tools

### Blueprint Processor
```bash
# Validate template
python scripts/smart_blueprint_processor.py blueprint.json validate

# Extract code example
python scripts/smart_blueprint_processor.py blueprint.json extract output.py

# Test template
python scripts/smart_blueprint_processor.py blueprint.json test

# Get metadata
python scripts/smart_blueprint_processor.py blueprint.json metadata
```

### IDE Integration
```bash
# Generate VS Code snippets from blueprints
python scripts/generate_vscode_snippets.py

# Create syntax highlighting for embedded templates
python scripts/setup_template_highlighting.py

# Blueprint validation in CI/CD
python scripts/ci_validate_blueprints.py
```

## Best Practices

### Template Design
1. **Keep templates focused**: One responsibility per blueprint
2. **Use clear variable names**: Self-documenting template variables
3. **Include comprehensive tests**: Embedded test templates
4. **Validate early**: Syntax and logic validation
5. **Document thoroughly**: Clear descriptions and examples

### Performance Optimization
1. **Minimize template size**: Remove unnecessary whitespace
2. **Cache compiled templates**: Reuse processed templates
3. **Batch operations**: Process multiple blueprints together
4. **Profile generation**: Monitor performance metrics
5. **Optimize variables**: Reduce variable substitution overhead

### Maintenance
1. **Version blueprints**: Track changes and compatibility
2. **Test regularly**: Automated validation in CI/CD
3. **Update documentation**: Keep examples current
4. **Monitor usage**: Track which blueprints are used most
5. **Gather feedback**: Improve based on developer experience

## Success Metrics

### AI Performance
- **Generation Speed**: Target <1 second per blueprint
- **Token Efficiency**: 50%+ reduction in context size
- **Cache Hit Rate**: 90%+ for repeated generations
- **Error Rate**: <2% template failures

### Developer Experience
- **Blueprint Creation Time**: <10 minutes for new blueprint
- **Code Quality**: 100% linting compliance
- **Test Coverage**: 90%+ for generated code
- **Documentation**: Auto-generated API docs

### System Reliability
- **Template Validation**: 100% syntax validation
- **Security Compliance**: 0 security vulnerabilities
- **Performance**: No degradation in generated code
- **Maintainability**: Reduced maintenance overhead
