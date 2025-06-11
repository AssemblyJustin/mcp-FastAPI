"""Application Settings"""
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
