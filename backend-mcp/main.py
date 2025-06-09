from fastapi import FastAPI, HTTPException, Body, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import os
import logging
import json
from typing import Dict, List, Any, Optional
import uvicorn

# Import routers
from blueprints_router import router as blueprints_router
from code_examples_router import router as code_examples_router

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("mcp-fastapi")

# Create FastAPI app
app = FastAPI(
    title="FastAPI MCP Server",
    description="Model Context Protocol server for backend development",
    version="1.0.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create template engine
templates = Jinja2Templates(directory="backend-mcp/templates")

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Mount static files
app.mount("/static", StaticFiles(directory=f"{BASE_DIR}/backend-mcp/static"), name="static")

# Environment settings
MCP_ENVIRONMENT = os.getenv("MCP_ENVIRONMENT", "development")
MCP_LOG_LEVEL = os.getenv("MCP_LOG_LEVEL", "INFO")

# Data directories
BLUEPRINTS_DIR = f"{BASE_DIR}/backend-mcp/blueprints"
CODE_EXAMPLES_DIR = f"{BASE_DIR}/backend-mcp/code-examples"
TEMPLATES_DIR = f"{BASE_DIR}/backend-mcp/templates"

# Ensure directories exist
os.makedirs(BLUEPRINTS_DIR, exist_ok=True)
os.makedirs(CODE_EXAMPLES_DIR, exist_ok=True)
os.makedirs(TEMPLATES_DIR, exist_ok=True)
os.makedirs(f"{BASE_DIR}/backend-mcp/static", exist_ok=True)

# Include routers
app.include_router(blueprints_router)
app.include_router(code_examples_router)

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "environment": MCP_ENVIRONMENT}

# Root endpoint
@app.get("/")
async def root(request: Request):
    """Root endpoint - returns dashboard template"""
    return templates.TemplateResponse(
        "dashboard.html", 
        {"request": request, "title": "FastAPI MCP Server"}
    )

# Error handlers
@app.exception_handler(404)
async def not_found_handler(request: Request, exc: HTTPException):
    """Handle 404 errors"""
    return JSONResponse(
        status_code=404,
        content={"error": "Resource not found", "path": str(request.url)}
    )

@app.exception_handler(500)
async def server_error_handler(request: Request, exc: Exception):
    """Handle 500 errors"""
    logger.error(f"Internal server error: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error", "detail": str(exc)}
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 