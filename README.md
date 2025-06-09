# FastAPI MCP

AI-first Model Context Protocol server for FastAPI backend development with Smart Blueprints.

## 🤖 For AI Assistants

**CRITICAL**: Use context loading prompts for new chats:
1. **Choose prompt** from `.ai-docs/@prompts/@prompt-[task-type].md`
2. **Copy complete prompt** and paste in new chat
3. **Wait for ✅ confirmation** before proceeding

**Quick Reference**: Always load `.ai-docs/@core/@conventions.md` FIRST
**Validation**: `python scripts/validate_ai_context.py --check-all`

## 🚀 Quick Start

```bash
# Windows: setup.bat && start.bat
# Linux/Mac: ./setup.sh && ./start.sh
# Manual: python -m venv .venv && .venv/Scripts/activate && pip install mcp anyio pydantic && cd frontend-mcp && python -m py_server.server
```

## 📁 AI-Optimized Structure

```
FastAPI-MCP/
├── .ai-docs/@core/        # 🤖 AI CONTEXT (load first)
│   ├── @conventions.md    # Master rules
│   ├── @testing-protocol.md # Testing rules
│   └── @project-concept.md # AI philosophy
├── backend-mcp/           # FastAPI MCP server + smart blueprints
│   ├── blueprints/        # Smart blueprints with embedded templates
│   ├── templates/         # Jinja2 templates (if needed)
│   └── main.py           # FastAPI MCP server
├── tests/                 # Testing infrastructure (unit/integration/load/security)
├── scripts/               # Automation (validate_*.py, smart_blueprint_processor.py)
└── docs/                  # Human documentation
```

## 🔧 MCP Tools

- `generate_from_smart_blueprint` - FastAPI routes, services, models
- `smart_crud_route` - Complete CRUD API endpoints
- `smart_auth_route` - Authentication endpoints
- `smart_service` - Business logic services
- `smart_model` - Pydantic and SQLAlchemy models

## 📖 Documentation

**For AI**: `.ai-docs/@core/` (optimized context)
**For Humans**: `docs/` (comprehensive guides)
**For Testing**: `tests/README.md` (current state)
