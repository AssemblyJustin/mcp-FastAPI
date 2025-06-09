# @naming-conventions

**AI Context**: Quick naming reference. ALWAYS load `.ai-docs/@core/MASTER_CONVENTIONS.md` first for complete rules.

## ⚠️ CRITICAL: Load .ai-docs/@core/MASTER_CONVENTIONS.md First
This file is a quick reference only. The authoritative naming rules are in `.ai-docs/@core/MASTER_CONVENTIONS.md`.

## Quick Reference

### API Routes: `{resource}_routes.py`
- Examples: `user_routes.py`, `auth_routes.py`
- Functions: `[action]_[resource]` (snake_case)
- Location: `backend-mcp/routes/`

### Services: `{resource}_service.py`
- Examples: `user_service.py`, `auth_service.py`
- Classes: `{Resource}Service` (PascalCase)
- Location: `backend-mcp/services/`

### Models: `{resource}_model.py`
- Examples: `user_model.py`, `product_model.py`
- Classes: `{Resource}Base`, `{Resource}Create`, `{Resource}Update`
- Location: `backend-mcp/models/`

### Smart Blueprints: `{action}-{layer}-{resource}.json`
- Examples: `create-route-user.json`, `update-service-auth.json`
- Location: `backend-mcp/blueprints/{layer}/`
- Contains: Embedded code templates, test templates, validation rules

### Tests: Follow API testing patterns
- Unit: `test_[resource]_service.py`
- Integration: `test_[resource]_api.py`
- Load: `test_[resource]_load.py`
- Security: `test_[resource]_security.py`

## 🔥 Critical Rules (from .ai-docs/@core/MASTER_CONVENTIONS.md)
- **Smart Blueprint Strategy**: blueprint → test (no separate code examples)
- **No root-level APIs**: Must be in `backend-mcp/`
- **snake_case routes**: `user_routes.py`, not `UserRoutes.py`
- **PascalCase models**: `UserCreate`, not `user_create`
- **kebab-case blueprints**: `create-route-user.json`
- **Embedded templates**: Code templates inside blueprint JSON

## Template Variables
- `{{resourceName}}` - snake_case resource name
- `{{modelName}}` - PascalCase model name
- `{{httpMethod}}`, `{{endpoint}}` - API specifications
- `{{authRequired}}` - Authentication requirement

## AI Validation Checklist
```bash
# Before creating smart blueprints
python scripts/validate_smart_blueprint.py --blueprint [blueprint_name]
python scripts/validate_fastapi_conventions.py --check-all
python scripts/validate_ai_context.py --check-all

# Extract code example for development
python scripts/smart_blueprint_processor.py [blueprint.json] extract [output.py]
```
