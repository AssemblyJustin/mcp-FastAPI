# FastAPI MCP Documentation

This directory contains comprehensive documentation for the FastAPI MCP project with Smart Blueprints.

## Documentation Categories

### 📋 [Planning Documentation](./planning/)
Project planning documents, roadmaps, and task lists:
- Development roadmap and API creation lists
- Current task priorities and completion tracking
- Smart Blueprint development planning

### 📄 [Summaries](./summaries/)
Project summaries and decision records:
- Architecture decisions
- Migration summaries
- Implementation notes

### 📚 [Human Navigation](./human-navigation/)
Human-friendly navigation guides:
- Project overview
- Getting started guides
- Development workflows

## Related Documentation

### Project Documentation (Root Level)
- [README.md](../README.md) - Main project overview
- [.ai-docs/@core/@project-concept.md](../.ai-docs/@core/@project-concept.md) - Core project concept and vision

### AI Context Documentation
- [.ai-docs/@core/](../.ai-docs/@core/) - Core AI context files (LOAD FIRST)
- [.ai-docs/@context/](../.ai-docs/@context/) - Architecture and patterns
- [.ai-docs/@conventions/](../.ai-docs/@conventions/) - Naming and structure conventions
- [.ai-docs/@prompts/](../.ai-docs/@prompts/) - AI workflow prompts

### Implementation Documentation
- [backend-mcp/](../backend-mcp/) - FastAPI MCP server and Smart Blueprints
- [tests/](../tests/) - Testing infrastructure (unit/integration/load/security)
- [scripts/](../scripts/) - Automation and validation scripts

## Documentation Standards

### File Organization
- **AI Context docs**: `.ai-docs/@core/` (ALWAYS LOAD FIRST)
- **Implementation docs**: `docs/` directory with categorized subdirectories
- **Live docs**: Co-located with code (tests/README.md, backend-mcp/README.md)
- **Smart Blueprints**: `backend-mcp/blueprints/` with embedded templates

### Naming Conventions
- Use descriptive, kebab-case filenames
- Smart Blueprints: `smart-[layer]-[resource].json`
- API files: `[resource]_[type].py` (snake_case)
- Use README.md for directory overviews
- Use .md extension for all documentation

### Content Standards
- Start with clear purpose statement
- Include table of contents for long documents
- Use consistent heading hierarchy
- Include FastAPI code examples where relevant
- Provide cross-references to related documentation
- Reference Smart Blueprint system for code generation
