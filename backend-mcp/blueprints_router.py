"""
Smart Blueprint Router for FastAPI MCP

This module provides API endpoints for managing Smart Blueprints with embedded templates.
"""

from fastapi import APIRouter, HTTPException, Body, Depends, Path, Query, UploadFile, File
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Dict, List, Any, Optional, Union
import json
import os
import logging
import shutil
from pathlib import Path as FilePath

from template_engine import (
    load_blueprint,
    list_available_blueprints,
    generate_from_blueprint,
    find_blueprints_dir
)

# Configure logging
logger = logging.getLogger("mcp-fastapi.blueprints-router")

# Create router
router = APIRouter(prefix="/api/blueprints", tags=["blueprints"])


# Models
class BlueprintBase(BaseModel):
    """Base model for blueprint data"""
    id: str
    name: str
    description: str
    version: str = "1.0.0"


class BlueprintParameter(BaseModel):
    """Model for blueprint parameters"""
    type: str
    required: bool = False
    default: Optional[Any] = None
    description: Optional[str] = None


class CodeTemplate(BaseModel):
    """Model for embedded code template"""
    language: str
    executable: bool = True
    testable: bool = True
    content: str


class TestTemplate(BaseModel):
    """Model for embedded test template"""
    language: str
    framework: str
    content: str


class BlueprintCreate(BlueprintBase):
    """Model for creating a new Smart Blueprint"""
    strategy: str = "embedded-template"
    parameters: Dict[str, BlueprintParameter]
    codeTemplate: CodeTemplate
    testTemplate: Optional[TestTemplate] = None
    validation: Optional[Dict[str, Any]] = None
    rollback: Optional[Dict[str, Any]] = None
    metadata: Optional[Dict[str, Any]] = None


class GenerateFromBlueprintRequest(BaseModel):
    """Model for generating code from a blueprint"""
    blueprintId: str
    parameters: Dict[str, Any]
    outputPath: str


# Endpoints
@router.get("/", response_model=List[BlueprintBase])
async def get_all_blueprints():
    """Get all available blueprints"""
    return list_available_blueprints()


@router.get("/{blueprint_id}", response_model=Dict[str, Any])
async def get_blueprint(blueprint_id: str = Path(..., description="The ID of the blueprint to get")):
    """Get a specific blueprint by ID"""
    blueprint = load_blueprint(blueprint_id)
    if not blueprint:
        raise HTTPException(status_code=404, detail=f"Blueprint with ID '{blueprint_id}' not found")
    return blueprint


@router.post("/", response_model=Dict[str, Any])
async def create_blueprint(blueprint: BlueprintCreate):
    """Create a new blueprint"""
    blueprints_dir = find_blueprints_dir()
    blueprint_path = os.path.join(blueprints_dir, f"{blueprint.id}.json")
    
    # Check if blueprint already exists
    if os.path.exists(blueprint_path):
        raise HTTPException(status_code=409, detail=f"Blueprint with ID '{blueprint.id}' already exists")
    
    try:
        # Convert to dict for JSON serialization
        blueprint_dict = blueprint.dict(exclude_none=True)
        
        # Write to file
        with open(blueprint_path, "w", encoding="utf-8") as f:
            json.dump(blueprint_dict, f, indent=2)
        
        return {
            "success": True,
            "message": f"Blueprint '{blueprint.id}' created successfully",
            "blueprint": blueprint_dict
        }
    except Exception as e:
        logger.error(f"Error creating blueprint {blueprint.id}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to create blueprint: {str(e)}")


@router.put("/{blueprint_id}", response_model=Dict[str, Any])
async def update_blueprint(
    blueprint: BlueprintCreate,
    blueprint_id: str = Path(..., description="The ID of the blueprint to update")
):
    """Update an existing blueprint"""
    # Ensure IDs match
    if blueprint.id != blueprint_id:
        raise HTTPException(status_code=400, detail="Blueprint ID in path must match ID in body")
    
    blueprints_dir = find_blueprints_dir()
    blueprint_path = os.path.join(blueprints_dir, f"{blueprint_id}.json")
    
    # Check if blueprint exists
    if not os.path.exists(blueprint_path):
        raise HTTPException(status_code=404, detail=f"Blueprint with ID '{blueprint_id}' not found")
    
    try:
        # Convert to dict for JSON serialization
        blueprint_dict = blueprint.dict(exclude_none=True)
        
        # Write to file
        with open(blueprint_path, "w", encoding="utf-8") as f:
            json.dump(blueprint_dict, f, indent=2)
        
        return {
            "success": True,
            "message": f"Blueprint '{blueprint_id}' updated successfully",
            "blueprint": blueprint_dict
        }
    except Exception as e:
        logger.error(f"Error updating blueprint {blueprint_id}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to update blueprint: {str(e)}")


@router.delete("/{blueprint_id}", response_model=Dict[str, Any])
async def delete_blueprint(blueprint_id: str = Path(..., description="The ID of the blueprint to delete")):
    """Delete a blueprint"""
    blueprints_dir = find_blueprints_dir()
    blueprint_path = os.path.join(blueprints_dir, f"{blueprint_id}.json")
    
    # Check if blueprint exists
    if not os.path.exists(blueprint_path):
        raise HTTPException(status_code=404, detail=f"Blueprint with ID '{blueprint_id}' not found")
    
    try:
        # Delete the file
        os.remove(blueprint_path)
        
        return {
            "success": True,
            "message": f"Blueprint '{blueprint_id}' deleted successfully"
        }
    except Exception as e:
        logger.error(f"Error deleting blueprint {blueprint_id}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to delete blueprint: {str(e)}")


@router.post("/generate", response_model=Dict[str, Any])
async def generate_code_from_blueprint(request: GenerateFromBlueprintRequest):
    """Generate code from a blueprint"""
    result = generate_from_blueprint(
        request.blueprintId,
        request.parameters,
        request.outputPath
    )
    
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["error"])
    
    return result


@router.post("/upload", response_model=Dict[str, Any])
async def upload_blueprint(
    file: UploadFile = File(...),
    overwrite: bool = Query(False, description="Overwrite existing blueprint if it exists")
):
    """Upload a blueprint JSON file"""
    if not file.filename.endswith(".json"):
        raise HTTPException(status_code=400, detail="File must be a JSON file")
    
    try:
        # Read file content
        content = await file.read()
        
        # Parse JSON
        try:
            blueprint_data = json.loads(content)
        except json.JSONDecodeError:
            raise HTTPException(status_code=400, detail="Invalid JSON file")
        
        # Check required fields
        if "id" not in blueprint_data:
            raise HTTPException(status_code=400, detail="Blueprint must have an 'id' field")
        
        blueprint_id = blueprint_data["id"]
        blueprints_dir = find_blueprints_dir()
        blueprint_path = os.path.join(blueprints_dir, f"{blueprint_id}.json")
        
        # Check if blueprint already exists
        if os.path.exists(blueprint_path) and not overwrite:
            raise HTTPException(
                status_code=409, 
                detail=f"Blueprint with ID '{blueprint_id}' already exists. Use 'overwrite=true' to replace it."
            )
        
        # Write to file
        with open(blueprint_path, "wb") as f:
            f.write(content)
        
        return {
            "success": True,
            "message": f"Blueprint '{blueprint_id}' uploaded successfully",
            "blueprint": blueprint_data
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error uploading blueprint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to upload blueprint: {str(e)}")


@router.get("/extract/{blueprint_id}", response_model=Dict[str, Any])
async def extract_code_example(blueprint_id: str = Path(..., description="The ID of the blueprint to extract code from")):
    """Extract code example from Smart Blueprint embedded template"""
    blueprint = load_blueprint(blueprint_id)
    if not blueprint:
        raise HTTPException(status_code=404, detail=f"Blueprint with ID '{blueprint_id}' not found")

    if "codeTemplate" not in blueprint:
        raise HTTPException(status_code=400, detail=f"Blueprint '{blueprint_id}' does not have an embedded code template")

    return {
        "success": True,
        "blueprint_id": blueprint_id,
        "code_template": blueprint["codeTemplate"],
        "extracted_code": blueprint["codeTemplate"].get("content", "")
    }