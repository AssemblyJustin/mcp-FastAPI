"""Dependency Injection Setup"""
from fastapi import Depends
from backend_mcp.config.settings import settings

def get_settings():
    return settings

# Add other dependencies here as needed
