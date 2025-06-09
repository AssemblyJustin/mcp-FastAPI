# Changelog

All notable changes to OpinionatedMCP will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- Comprehensive peer review documentation
- Enhanced project structure analysis

## [1.3.0] - 2025-01-07
### Added
- Data flow analysis documentation showing TaskMaster → MCP → Generated Code pipeline
- Example task flow demo script for testing and understanding MCP data flow
- Comprehensive testing standards documentation
- Testing directory structure design documentation
- Enhanced documentation organization with chronological summaries

### Changed
- Moved `data_flow_breakdown.md` from frontend-mcp to docs/summaries with proper naming
- Moved `example_task_flow.py` from frontend-mcp to tests/manual/demos with updated imports
- Reorganized testing documentation files to docs/summaries with yymmddhhmm naming convention
- Updated frontend-mcp directory to contain only core MCP server package files
- Enhanced summaries README with new documentation entries

### Removed
- Misplaced documentation files from frontend-mcp directory
- Empty docs/testing directory after reorganization

## [1.2.0] - 2025-01-07
### Added
- Comprehensive testing structure reorganization with 25 organized directories
- Multi-tier testing framework (unit, integration, e2e, manual)
- Test configuration files for pytest, jest, and playwright
- Shared test utilities for Python and TypeScript
- Proper test output management with gitignore rules
- Testing standards and conventions documentation

### Changed
- Migrated 33 test files to new organized structure
- Updated all Python test files with correct relative imports
- Fixed output paths to use tests/outputs/ directory
- Moved tests/e2e/atoms/ to tests/e2e/components/atoms/
- Consolidated test outputs from multiple locations

### Fixed
- Import path issues in all migrated test files
- Test output directory duplication and conflicts

## [1.1.0] - 2025-01-06
### Added
- Directory consolidation with blueprints and code-examples moved to frontend-mcp
- Root directory cleanup moving planning documents to docs/planning
- Test output consolidation from test-output/ to tests/outputs/
- Documentation organization with proper docs/ structure
- Summary organization implementation with chronological tracking

### Changed
- Consolidated duplicate directories for better organization
- Moved utility scripts from root to scripts/ directory
- Organized documentation files into proper docs/ structure
- Implemented yymmddhhmm naming convention for summaries

### Removed
- Duplicate blueprints/ and code-examples/ directories from root
- Scattered planning documents from root directory
- Old test-output/ directory structure

## [1.0.0] - 2025-01-06
### Added
- Initial OpinionatedMCP server implementation
- Blueprint-based code generation system
- Atomic design component structure (atoms, molecules, organisms)
- Frontend MCP server with specialized tools for React development
- Multi-platform deployment options (Docker, portable, native)
- Cross-platform setup scripts (Windows .bat and Unix .sh)
- AI-first development philosophy and standards
- Core MCP tools: generate_component, generate_hook, generate_service, generate_from_blueprint
- Template engine with parameterization support
- Code examples for React components, hooks, and services

### Features
- **Blueprint System**: Template-based code generation with 1:1 code-example relationship
- **Atomic Design**: Organized component structure following atomic design principles
- **Multi-Platform**: Windows and Unix deployment support
- **AI-Optimized**: Designed for AI agent code generation workflows
- **Testing Ready**: Initial testing framework setup
- **Documentation**: Comprehensive README and project concept documentation

## Project Structure Evolution

### Current Structure (v1.3.0)
```
OpinionatedMCP/
├── CHANGELOG.md           # Version history (NEW)
├── PROJECT CONCEPT.md     # AI-first development philosophy
├── README.md             # Main project documentation
├── deploy-options/       # Multiple deployment strategies
├── docs/                 # Organized documentation
│   ├── planning/         # Development roadmaps
│   └── summaries/        # Chronological project history
├── frontend-mcp/         # Clean MCP server package
│   ├── blueprints/       # Code generation templates
│   ├── code-examples/    # Reference implementations
│   └── py_server/        # Core server implementation
├── implementation/       # AI workflow guides
├── scripts/             # Utility and maintenance scripts
└── tests/               # Comprehensive testing framework
    ├── unit/            # Fast, isolated tests
    ├── integration/     # Workflow validation
    ├── e2e/            # Browser-based testing
    ├── manual/         # Demos and validation
    └── outputs/        # Generated test files
```

## Migration Notes

### For Developers
- Test files have been reorganized - update any local scripts that reference old paths
- Import paths in test files have been updated to work with new structure
- All test outputs now go to tests/outputs/ directory (gitignored)

### For AI Agents
- Blueprint and code-example files remain in same relative locations within frontend-mcp/
- MCP server functionality unchanged - only file organization improved
- Documentation now properly organized for better context retrieval

## Links
- [Project Repository](https://github.com/your-username/OpinionatedMCP)
- [Documentation](docs/README.md)
- [Testing Guide](tests/README.md)
- [Deployment Options](deploy-options/)
