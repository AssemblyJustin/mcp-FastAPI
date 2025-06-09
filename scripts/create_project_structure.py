#!/usr/bin/env python3
"""
FastAPI MCP Project Structure Creator

This script creates the complete directory structure and foundation files
for the FastAPI MCP framework based on the project structure standard.

Usage:
    python scripts/create_project_structure.py [--dry-run]

Options:
    --dry-run    Show what would be created without actually creating files
"""

from pathlib import Path
from typing import Dict, List

class ProjectStructureCreator:
    """Creates the complete FastAPI MCP project structure."""
    
    def __init__(self, root_dir: str = ".", dry_run: bool = False):
        self.root_dir = Path(root_dir).resolve()
        self.dry_run = dry_run
        self.created_dirs = []
        self.created_files = []
        self.skipped_existing = []
        
    def create_directory(self, path: Path) -> bool:
        """Create a directory if it doesn't exist."""
        if path.exists():
            self.skipped_existing.append(str(path))
            return False
            
        if self.dry_run:
            print(f"[DRY RUN] Would create directory: {path}")
            return True
            
        try:
            path.mkdir(parents=True, exist_ok=True)
            self.created_dirs.append(str(path))
            print(f"✅ Created directory: {path}")
            return True
        except Exception as e:
            print(f"❌ Failed to create directory {path}: {e}")
            return False
    
    def create_file(self, path: Path, content: str = "") -> bool:
        """Create a file with content if it doesn't exist."""
        if path.exists():
            self.skipped_existing.append(str(path))
            return False
            
        if self.dry_run:
            print(f"[DRY RUN] Would create file: {path}")
            return True
            
        try:
            # Ensure parent directory exists
            path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            self.created_files.append(str(path))
            print(f"✅ Created file: {path}")
            return True
        except Exception as e:
            print(f"❌ Failed to create file {path}: {e}")
            return False
    
    def get_root_files_content(self) -> Dict[str, str]:
        """Get content for root level files."""
        return {
            ".env.example": '''# FastAPI MCP Server Environment Configuration Template
# Copy this file to .env and update with your actual values

# Application Settings
APP_NAME="FastAPI MCP Server"
APP_VERSION="1.0.0"
ENVIRONMENT="development"  # development|staging|production
DEBUG=true

# Database Configuration (Choose one approach)
# Traditional Database
DATABASE_URL="postgresql+asyncpg://user:password@localhost:5432/fastapi_mcp"
DATABASE_POOL_SIZE=20
DATABASE_MAX_OVERFLOW=0
DATABASE_ECHO=false

# OR Supabase (comment out traditional database if using this)
# SUPABASE_URL="https://your-project.supabase.co"
# SUPABASE_ANON_KEY="your-anon-key"
# SUPABASE_SERVICE_KEY="your-service-key"

# Security
SECRET_KEY="your-super-secret-key-minimum-32-characters-long"
CORS_ORIGINS=["http://localhost:3000","http://localhost:8000"]
ALLOWED_HOSTS=["*"]

# Monitoring & Logging
LOG_LEVEL="INFO"  # DEBUG|INFO|WARNING|ERROR|CRITICAL
SENTRY_DSN=""  # Optional: Sentry error monitoring
ENABLE_METRICS=true

# Rate Limiting
ENABLE_RATE_LIMITING=true
RATE_LIMIT_REQUESTS=100
RATE_LIMIT_WINDOW=60  # seconds

# Feature Flags
ENABLE_SWAGGER_UI=true
ENABLE_REDOC=true

# MCP Server Configuration
MCP_SERVER_NAME="fastapi-mcp"
MCP_SERVER_VERSION="1.0.0"
''',
            
            ".gitignore": '''# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# pipenv
Pipfile.lock

# poetry
poetry.lock

# pdm
.pdm.toml

# PEP 582
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
.idea/

# VS Code
.vscode/

# FastAPI MCP Specific
tests/outputs/
*.db
*.sqlite
.DS_Store
Thumbs.db

# Docker
.dockerignore
docker-compose.override.yml

# Logs
logs/
*.log

# Temporary files
tmp/
temp/
''',
            
            "requirements.txt": '''# FastAPI MCP Server Dependencies

# Core FastAPI
fastapi==0.104.1
uvicorn[standard]==0.24.0
pydantic==2.5.0
pydantic-settings==2.1.0

# MCP Protocol
mcp==0.3.0

# Database (Traditional)
sqlalchemy[asyncio]==2.0.23
asyncpg==0.29.0
alembic==1.13.1

# Database (Supabase) - Optional
supabase==2.3.0

# Authentication & Security
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6

# HTTP & API
httpx==0.25.2
requests==2.31.0

# Rate Limiting & Middleware
slowapi==0.1.9
python-cors==1.7.0

# Monitoring & Logging
structlog==23.2.0
sentry-sdk[fastapi]==1.38.0

# Development & Testing
pytest==7.4.3
pytest-asyncio==0.21.1
pytest-cov==4.1.0
httpx==0.25.2  # For TestClient
locust==2.17.0  # Load testing

# Code Quality
black==23.11.0
isort==5.12.0
flake8==6.1.0
mypy==1.7.1

# Utilities
python-dotenv==1.0.0
click==8.1.7
rich==13.7.0
jinja2==3.1.2

# Production
gunicorn==21.2.0
''',
            
            "Dockerfile": '''FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

# Install system dependencies
RUN apt-get update \\
    && apt-get install -y --no-install-recommends \\
        build-essential \\
        curl \\
        postgresql-client \\
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip \\
    && pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user
RUN adduser --disabled-password --gecos '' appuser \\
    && chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \\
    CMD curl -f http://localhost:8000/system/health || exit 1

# Run the application
CMD ["uvicorn", "backend_mcp.main:app", "--host", "0.0.0.0", "--port", "8000"]
'''
        }

    def get_backend_structure(self) -> List[str]:
        """Get list of backend-mcp directories to create."""
        return [
            "backend-mcp/blueprints/tools",
            "backend-mcp/blueprints/middleware",
            "backend-mcp/blueprints/database/traditional",
            "backend-mcp/blueprints/database/supabase",
            "backend-mcp/blueprints/system",
            "backend-mcp/server",
            "backend-mcp/tools",
            "backend-mcp/routes",
            "backend-mcp/services",
            "backend-mcp/models",
            "backend-mcp/middleware",
            "backend-mcp/database/models",
            "backend-mcp/database/repositories",
            "backend-mcp/database/migrations",
            "backend-mcp/database/supabase",
            "backend-mcp/config",
            "backend-mcp/utils"
        ]

    def get_test_structure(self) -> List[str]:
        """Get list of test directories to create."""
        return [
            "tests/fixtures",
            "tests/mocks",
            "tests/config"
        ]

    def get_script_files(self) -> Dict[str, str]:
        """Get script files to create with basic content."""
        return {
            "scripts/validate_smart_blueprint.py": '''#!/usr/bin/env python3
"""Blueprint validation script - TO BE IMPLEMENTED"""
print("Blueprint validation script - placeholder")
''',
            "scripts/validate_fastapi_conventions.py": '''#!/usr/bin/env python3
"""FastAPI conventions validation script - TO BE IMPLEMENTED"""
print("FastAPI conventions validation script - placeholder")
''',
            "scripts/validate_ai_context.py": '''#!/usr/bin/env python3
"""AI context validation script - TO BE IMPLEMENTED"""
print("AI context validation script - placeholder")
''',
            "scripts/generate_test_suite.py": '''#!/usr/bin/env python3
"""Test suite generation script - TO BE IMPLEMENTED"""
print("Test suite generation script - placeholder")
''',
            "scripts/performance_monitor.py": '''#!/usr/bin/env python3
"""Performance monitoring script - TO BE IMPLEMENTED"""
print("Performance monitoring script - placeholder")
''',
            "scripts/security_scanner.py": '''#!/usr/bin/env python3
"""Security scanning script - TO BE IMPLEMENTED"""
print("Security scanning script - placeholder")
''',
            "scripts/enforce_coverage.py": '''#!/usr/bin/env python3
"""Coverage enforcement script - TO BE IMPLEMENTED"""
print("Coverage enforcement script - placeholder")
''',
            "scripts/database_migration.py": '''#!/usr/bin/env python3
"""Database migration script - TO BE IMPLEMENTED"""
print("Database migration script - placeholder")
''',
            "scripts/deployment_validator.py": '''#!/usr/bin/env python3
"""Deployment validation script - TO BE IMPLEMENTED"""
print("Deployment validation script - placeholder")
''',
            "scripts/code_formatter.py": '''#!/usr/bin/env python3
"""Code formatting script - TO BE IMPLEMENTED"""
print("Code formatting script - placeholder")
''',
            "scripts/project_initializer.py": '''#!/usr/bin/env python3
"""Project initialization script - TO BE IMPLEMENTED"""
print("Project initialization script - placeholder")
'''
        }

    def get_docs_structure(self) -> List[str]:
        """Get list of docs directories to create."""
        return [
            "docs/guides",
            "docs/api"
        ]

    def get_foundation_files(self) -> Dict[str, str]:
        """Get foundation Python files with basic content."""
        return {
            # Backend MCP Foundation Files
            "backend-mcp/server/__init__.py": "",
            "backend-mcp/server/mcp_server.py": '''"""MCP Server Implementation - TO BE IMPLEMENTED"""
from typing import Any, Dict
print("MCP Server - placeholder implementation")
''',
            "backend-mcp/server/tool_registry.py": '''"""Tool Registry - TO BE IMPLEMENTED"""
print("Tool Registry - placeholder implementation")
''',
            "backend-mcp/server/protocol_handler.py": '''"""Protocol Handler - TO BE IMPLEMENTED"""
print("Protocol Handler - placeholder implementation")
''',

            "backend-mcp/tools/__init__.py": "",
            "backend-mcp/tools/code_generator_tool.py": '''"""Code Generator Tool - TO BE IMPLEMENTED"""
print("Code Generator Tool - placeholder implementation")
''',
            "backend-mcp/tools/blueprint_tool.py": '''"""Blueprint Tool - TO BE IMPLEMENTED"""
print("Blueprint Tool - placeholder implementation")
''',
            "backend-mcp/tools/validator_tool.py": '''"""Validator Tool - TO BE IMPLEMENTED"""
print("Validator Tool - placeholder implementation")
''',

            "backend-mcp/routes/__init__.py": "",
            "backend-mcp/routes/system_routes.py": '''"""System Routes - Health Check Implementation"""
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/system", tags=["system"])

class HealthResponse(BaseModel):
    status: str
    message: str

@router.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint."""
    return HealthResponse(status="healthy", message="FastAPI MCP Server is running")
''',
            "backend-mcp/routes/user_routes.py": '''"""User Routes - TO BE IMPLEMENTED"""
from fastapi import APIRouter
router = APIRouter(prefix="/users", tags=["users"])
# User routes implementation goes here
''',
            "backend-mcp/routes/auth_routes.py": '''"""Auth Routes - TO BE IMPLEMENTED"""
from fastapi import APIRouter
router = APIRouter(prefix="/auth", tags=["auth"])
# Auth routes implementation goes here
''',

            "backend-mcp/services/__init__.py": "",
            "backend-mcp/services/user_service.py": '''"""User Service - TO BE IMPLEMENTED"""
print("User Service - placeholder implementation")
''',
            "backend-mcp/services/auth_service.py": '''"""Auth Service - TO BE IMPLEMENTED"""
print("Auth Service - placeholder implementation")
''',
            "backend-mcp/services/blueprint_service.py": '''"""Blueprint Service - TO BE IMPLEMENTED"""
print("Blueprint Service - placeholder implementation")
''',

            "backend-mcp/models/__init__.py": "",
            "backend-mcp/models/user_model.py": '''"""User Models - TO BE IMPLEMENTED"""
from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    email: str
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool = True

    class Config:
        from_attributes = True
''',
            "backend-mcp/models/auth_model.py": '''"""Auth Models - TO BE IMPLEMENTED"""
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str = None
''',
            "backend-mcp/models/blueprint_model.py": '''"""Blueprint Models - TO BE IMPLEMENTED"""
from pydantic import BaseModel
from typing import Dict, Any

class Blueprint(BaseModel):
    name: str
    action: str
    layer: str
    resource: str
    template: Dict[str, Any]
''',

            "backend-mcp/middleware/__init__.py": "",
            "backend-mcp/middleware/auth.py": '''"""Auth Middleware - TO BE IMPLEMENTED"""
print("Auth Middleware - placeholder implementation")
''',
            "backend-mcp/middleware/cors.py": '''"""CORS Middleware - TO BE IMPLEMENTED"""
print("CORS Middleware - placeholder implementation")
''',
            "backend-mcp/middleware/rate_limiting.py": '''"""Rate Limiting Middleware - TO BE IMPLEMENTED"""
print("Rate Limiting Middleware - placeholder implementation")
''',
            "backend-mcp/middleware/logging.py": '''"""Logging Middleware - TO BE IMPLEMENTED"""
print("Logging Middleware - placeholder implementation")
''',

            "backend-mcp/database/__init__.py": "",
            "backend-mcp/database/connection.py": '''"""Database Connection - TO BE IMPLEMENTED"""
print("Database Connection - placeholder implementation")
''',
            "backend-mcp/database/models/__init__.py": "",
            "backend-mcp/database/repositories/__init__.py": "",
            "backend-mcp/database/migrations/__init__.py": "",
            "backend-mcp/database/supabase/__init__.py": "",
            "backend-mcp/database/supabase/client.py": '''"""Supabase Client - TO BE IMPLEMENTED"""
print("Supabase Client - placeholder implementation")
''',
            "backend-mcp/database/supabase/auth.py": '''"""Supabase Auth - TO BE IMPLEMENTED"""
print("Supabase Auth - placeholder implementation")
''',
            "backend-mcp/database/supabase/storage.py": '''"""Supabase Storage - TO BE IMPLEMENTED"""
print("Supabase Storage - placeholder implementation")
''',

            "backend-mcp/config/__init__.py": "",
            "backend-mcp/config/settings.py": '''"""Application Settings"""
from pydantic_settings import BaseSettings
from typing import List, Optional

class Settings(BaseSettings):
    # Application settings
    app_name: str = "FastAPI MCP Server"
    app_version: str = "1.0.0"
    environment: str = "development"
    debug: bool = True

    # Database settings (choose one approach)
    database_url: Optional[str] = None  # Traditional
    supabase_url: Optional[str] = None  # Supabase
    supabase_anon_key: Optional[str] = None
    supabase_service_key: Optional[str] = None

    # Security settings
    secret_key: str = "your-super-secret-key-minimum-32-characters-long"
    cors_origins: List[str] = ["http://localhost:3000", "http://localhost:8000"]

    # MCP Server settings
    mcp_server_name: str = "fastapi-mcp"
    mcp_server_version: str = "1.0.0"

    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
''',
            "backend-mcp/config/database.py": '''"""Database Configuration - TO BE IMPLEMENTED"""
print("Database Configuration - placeholder implementation")
''',
            "backend-mcp/config/security.py": '''"""Security Configuration - TO BE IMPLEMENTED"""
print("Security Configuration - placeholder implementation")
''',

            "backend-mcp/utils/__init__.py": "",
            "backend-mcp/utils/logging.py": '''"""Logging Utilities - TO BE IMPLEMENTED"""
print("Logging Utilities - placeholder implementation")
''',
            "backend-mcp/utils/monitoring.py": '''"""Monitoring Utilities - TO BE IMPLEMENTED"""
print("Monitoring Utilities - placeholder implementation")
''',
            "backend-mcp/utils/security.py": '''"""Security Utilities - TO BE IMPLEMENTED"""
print("Security Utilities - placeholder implementation")
''',
            "backend-mcp/utils/validation.py": '''"""Validation Utilities - TO BE IMPLEMENTED"""
print("Validation Utilities - placeholder implementation")
''',

            "backend-mcp/dependencies.py": '''"""Dependency Injection Setup"""
from fastapi import Depends
from backend_mcp.config.settings import settings

def get_settings():
    return settings

# Add other dependencies here as needed
''',

            # Test Foundation Files
            "tests/fixtures/__init__.py": "",
            "tests/fixtures/user_fixtures.py": '''"""User Test Fixtures - TO BE IMPLEMENTED"""
import pytest
# User test fixtures go here
''',
            "tests/fixtures/auth_fixtures.py": '''"""Auth Test Fixtures - TO BE IMPLEMENTED"""
import pytest
# Auth test fixtures go here
''',
            "tests/fixtures/database_fixtures.py": '''"""Database Test Fixtures - TO BE IMPLEMENTED"""
import pytest
# Database test fixtures go here
''',

            "tests/mocks/__init__.py": "",
            "tests/mocks/mock_services.py": '''"""Service Mocks - TO BE IMPLEMENTED"""
# Service mocks go here
''',
            "tests/mocks/mock_database.py": '''"""Database Mocks - TO BE IMPLEMENTED"""
# Database mocks go here
''',
            "tests/mocks/mock_external_apis.py": '''"""External API Mocks - TO BE IMPLEMENTED"""
# External API mocks go here
''',

            "tests/config/__init__.py": "",
            "tests/config/test_settings.py": '''"""Test Settings - TO BE IMPLEMENTED"""
# Test configuration goes here
''',
            "tests/config/database_config.py": '''"""Test Database Config - TO BE IMPLEMENTED"""
# Test database configuration goes here
''',
            "tests/config/mock_config.py": '''"""Mock Configuration - TO BE IMPLEMENTED"""
# Mock configuration goes here
'''
        }

    def get_blueprint_files(self) -> Dict[str, str]:
        """Get blueprint files with basic JSON structure."""
        return {
            # Tool Blueprints
            "backend-mcp/blueprints/tools/create-tool-code-generator.json": '''{
  "name": "create-tool-code-generator",
  "action": "create",
  "layer": "tool",
  "resource": "code-generator",
  "description": "Creates a code generation MCP tool",
  "template": {
    "imports": ["from typing import Any, Dict"],
    "class_name": "CodeGeneratorTool",
    "methods": ["generate_code", "validate_template"]
  }
}''',
            "backend-mcp/blueprints/tools/create-tool-validator.json": '''{
  "name": "create-tool-validator",
  "action": "create",
  "layer": "tool",
  "resource": "validator",
  "description": "Creates a validation MCP tool",
  "template": {
    "imports": ["from typing import Any, Dict"],
    "class_name": "ValidatorTool",
    "methods": ["validate_code", "check_conventions"]
  }
}''',

            # Middleware Blueprints
            "backend-mcp/blueprints/middleware/create-middleware-auth.json": '''{
  "name": "create-middleware-auth",
  "action": "create",
  "layer": "middleware",
  "resource": "auth",
  "description": "Creates authentication middleware",
  "template": {
    "imports": ["from fastapi import Request, HTTPException"],
    "class_name": "AuthMiddleware",
    "methods": ["authenticate", "authorize"]
  }
}''',
            "backend-mcp/blueprints/middleware/create-middleware-cors.json": '''{
  "name": "create-middleware-cors",
  "action": "create",
  "layer": "middleware",
  "resource": "cors",
  "description": "Creates CORS middleware",
  "template": {
    "imports": ["from fastapi.middleware.cors import CORSMiddleware"],
    "class_name": "CORSConfig",
    "methods": ["configure_cors"]
  }
}''',

            # Database Blueprints
            "backend-mcp/blueprints/database/traditional/create-repository-user.json": '''{
  "name": "create-repository-user",
  "action": "create",
  "layer": "repository",
  "resource": "user",
  "description": "Creates user repository for traditional database",
  "template": {
    "imports": ["from sqlalchemy.orm import Session"],
    "class_name": "UserRepository",
    "methods": ["create", "get", "update", "delete", "list"]
  }
}''',
            "backend-mcp/blueprints/database/traditional/create-connection-setup.json": '''{
  "name": "create-connection-setup",
  "action": "create",
  "layer": "database",
  "resource": "connection",
  "description": "Creates database connection setup",
  "template": {
    "imports": ["from sqlalchemy import create_engine"],
    "class_name": "DatabaseConnection",
    "methods": ["connect", "disconnect", "get_session"]
  }
}''',
            "backend-mcp/blueprints/database/supabase/create-supabase-client.json": '''{
  "name": "create-supabase-client",
  "action": "create",
  "layer": "database",
  "resource": "supabase-client",
  "description": "Creates Supabase client setup",
  "template": {
    "imports": ["from supabase import create_client"],
    "class_name": "SupabaseClient",
    "methods": ["initialize", "get_client", "authenticate"]
  }
}''',
            "backend-mcp/blueprints/database/supabase/create-supabase-auth.json": '''{
  "name": "create-supabase-auth",
  "action": "create",
  "layer": "database",
  "resource": "supabase-auth",
  "description": "Creates Supabase authentication",
  "template": {
    "imports": ["from supabase import Client"],
    "class_name": "SupabaseAuth",
    "methods": ["sign_up", "sign_in", "sign_out", "get_user"]
  }
}''',

            # System Blueprints
            "backend-mcp/blueprints/system/create-health-check.json": '''{
  "name": "create-health-check",
  "action": "create",
  "layer": "system",
  "resource": "health",
  "description": "Creates health check endpoint",
  "template": {
    "imports": ["from fastapi import APIRouter"],
    "class_name": "HealthCheck",
    "methods": ["check_health", "check_database", "check_dependencies"]
  }
}''',
            "backend-mcp/blueprints/system/create-monitoring.json": '''{
  "name": "create-monitoring",
  "action": "create",
  "layer": "system",
  "resource": "monitoring",
  "description": "Creates monitoring system",
  "template": {
    "imports": ["from typing import Dict, Any"],
    "class_name": "MonitoringSystem",
    "methods": ["collect_metrics", "log_performance", "alert"]
  }
}''',
            "backend-mcp/blueprints/system/create-logging.json": '''{
  "name": "create-logging",
  "action": "create",
  "layer": "system",
  "resource": "logging",
  "description": "Creates logging system",
  "template": {
    "imports": ["import logging", "from typing import Any"],
    "class_name": "LoggingSystem",
    "methods": ["setup_logging", "log_request", "log_error"]
  }
}'''
        }

    def create_all_structure(self) -> None:
        """Create the complete project structure."""
        print("🚀 Creating FastAPI MCP Project Structure...")
        print(f"📁 Root directory: {self.root_dir}")

        if self.dry_run:
            print("🔍 DRY RUN MODE - No files will be created")

        # Create root level files
        print("\n📄 Creating root level files...")
        root_files = self.get_root_files_content()
        for filename, content in root_files.items():
            file_path = self.root_dir / filename
            self.create_file(file_path, content)

        # Create backend directories
        print("\n📁 Creating backend-mcp directories...")
        backend_dirs = self.get_backend_structure()
        for dir_path in backend_dirs:
            full_path = self.root_dir / dir_path
            self.create_directory(full_path)

        # Create test directories
        print("\n🧪 Creating test directories...")
        test_dirs = self.get_test_structure()
        for dir_path in test_dirs:
            full_path = self.root_dir / dir_path
            self.create_directory(full_path)

        # Create docs directories
        print("\n📚 Creating docs directories...")
        docs_dirs = self.get_docs_structure()
        for dir_path in docs_dirs:
            full_path = self.root_dir / dir_path
            self.create_directory(full_path)

        # Create script files
        print("\n🔧 Creating script files...")
        script_files = self.get_script_files()
        for filename, content in script_files.items():
            file_path = self.root_dir / filename
            self.create_file(file_path, content)

        # Create foundation files
        print("\n🏗️ Creating foundation files...")
        foundation_files = self.get_foundation_files()
        for filename, content in foundation_files.items():
            file_path = self.root_dir / filename
            self.create_file(file_path, content)

        # Create blueprint files
        print("\n📐 Creating blueprint files...")
        blueprint_files = self.get_blueprint_files()
        for filename, content in blueprint_files.items():
            file_path = self.root_dir / filename
            self.create_file(file_path, content)

        # Print summary
        self.print_summary()

    def print_summary(self) -> None:
        """Print creation summary."""
        print("\n" + "="*60)
        print("📊 CREATION SUMMARY")
        print("="*60)
        print(f"✅ Directories created: {len(self.created_dirs)}")
        print(f"✅ Files created: {len(self.created_files)}")
        print(f"⏭️ Existing items skipped: {len(self.skipped_existing)}")

        if self.created_dirs:
            print(f"\n📁 Created directories:")
            for dir_path in sorted(self.created_dirs):
                print(f"   • {dir_path}")

        if self.created_files:
            print(f"\n📄 Created files:")
            for file_path in sorted(self.created_files):
                print(f"   • {file_path}")

        if self.skipped_existing:
            print(f"\n⏭️ Skipped existing:")
            for item_path in sorted(self.skipped_existing):
                print(f"   • {item_path}")

        print("\n🎯 NEXT STEPS:")
        print("1. Review created structure")
        print("2. Copy .env.example to .env and configure")
        print("3. Install dependencies: pip install -r requirements.txt")
        print("4. Run health check: python -m backend_mcp.main")
        print("5. Start implementing business logic")
        print("\n✅ Project structure creation complete!")


def main():
    """Main execution function."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Create FastAPI MCP project structure"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be created without creating files"
    )
    parser.add_argument(
        "--root-dir",
        default=".",
        help="Root directory for project creation (default: current directory)"
    )

    args = parser.parse_args()

    try:
        creator = ProjectStructureCreator(
            root_dir=args.root_dir,
            dry_run=args.dry_run
        )
        creator.create_all_structure()
    except KeyboardInterrupt:
        print("\n❌ Creation cancelled by user")
        return 1
    except Exception as e:
        print(f"\n❌ Error creating project structure: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
