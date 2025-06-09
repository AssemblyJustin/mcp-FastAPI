# @prompt-conventions-validation

**Purpose**: Identify files that violate project conventions.

## 🎯 Minimal Validation Prompt

```
Load: .ai-docs/@core/MASTER_CONVENTIONS.md

Check for violations:
- Forbidden root dirs: blueprints/, code-examples/, test-output/
- Forbidden root files: TESTING_*.md
- Required dirs: backend-mcp/, tests/, docs/, scripts/, .ai-docs/
- Python files: snake_case (.py)
- FastAPI patterns: routes, services, models layers
- No spaces in filenames
- Tests only in tests/ directory

Run: python scripts/validate_fastapi_conventions.py --check-all

Report violations only.
```
