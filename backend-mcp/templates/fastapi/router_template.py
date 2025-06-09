"""
{routeName} Router

This module provides API endpoints for {routeName}.
"""

from fastapi import APIRouter, HTTPException, Path, Query, Depends, Body
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Dict, List, Any, Optional
import logging

# Configure logging
logger = logging.getLogger("mcp-fastapi.{routeName}-router")

# Create router
router = APIRouter(prefix="{routePrefix}/{routeName}", tags=["{routeName}"])


# Models
class {modelName}Base(BaseModel):
    """Base model for {routeName} data"""
    id: Optional[str] = None
    name: str
    description: Optional[str] = None


class {modelName}Create(BaseModel):
    """Model for creating a new {routeName}"""
    name: str
    description: Optional[str] = None


class {modelName}Update(BaseModel):
    """Model for updating an existing {routeName}"""
    name: Optional[str] = None
    description: Optional[str] = None


class {modelName}Response({modelName}Base):
    """Response model for {routeName}"""
    id: str


# Mock database (replace with actual database in production)
{routeName}_db: Dict[str, {modelName}Base] = {{}}


# Endpoints
@router.get("/", response_model=List[{modelName}Response])
async def get_all_{routeName}():
    """{modelName} list endpoint"""
    return list({routeName}_db.values())


@router.get("/{{id}}", response_model={modelName}Response)
async def get_{routeName}(id: str = Path(..., description="The ID of the {routeName} to get")):
    """{modelName} detail endpoint"""
    if id not in {routeName}_db:
        raise HTTPException(status_code=404, detail=f"{modelName} with ID '{id}' not found")
    return {routeName}_db[id]


@router.post("/", response_model={modelName}Response, status_code=201)
async def create_{routeName}(item: {modelName}Create):
    """{modelName} create endpoint"""
    # Generate ID (in production, use UUID or database-generated ID)
    import uuid
    id = str(uuid.uuid4())
    
    # Create item
    new_item = {modelName}Base(id=id, **item.dict())
    {routeName}_db[id] = new_item
    
    logger.info(f"Created {routeName} with ID: {id}")
    return new_item


@router.put("/{{id}}", response_model={modelName}Response)
async def update_{routeName}(
    item: {modelName}Update,
    id: str = Path(..., description="The ID of the {routeName} to update")
):
    """{modelName} update endpoint"""
    if id not in {routeName}_db:
        raise HTTPException(status_code=404, detail=f"{modelName} with ID '{id}' not found")
    
    # Update item
    stored_item = {routeName}_db[id]
    update_data = item.dict(exclude_unset=True)
    
    for field, value in update_data.items():
        setattr(stored_item, field, value)
    
    {routeName}_db[id] = stored_item
    logger.info(f"Updated {routeName} with ID: {id}")
    
    return stored_item


@router.delete("/{{id}}", response_model=Dict[str, Any])
async def delete_{routeName}(id: str = Path(..., description="The ID of the {routeName} to delete")):
    """{modelName} delete endpoint"""
    if id not in {routeName}_db:
        raise HTTPException(status_code=404, detail=f"{modelName} with ID '{id}' not found")
    
    # Delete item
    del {routeName}_db[id]
    logger.info(f"Deleted {routeName} with ID: {id}")
    
    return {"success": True, "message": f"{modelName} with ID '{id}' deleted successfully"}


@router.get("/search/", response_model=List[{modelName}Response])
async def search_{routeName}(
    name: Optional[str] = Query(None, description="Filter by name (case-insensitive, partial match)"),
    skip: int = Query(0, description="Number of items to skip"),
    limit: int = Query(100, description="Maximum number of items to return")
):
    """{modelName} search endpoint"""
    results = list({routeName}_db.values())
    
    # Apply filters
    if name:
        results = [item for item in results if name.lower() in item.name.lower()]
    
    # Apply pagination
    return results[skip:skip+limit] 