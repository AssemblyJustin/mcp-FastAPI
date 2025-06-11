"""
Generated FastAPI User Routes
Generated at: 2025-06-09T20:46:56.102358
Blueprint: ../backend-mcp/blueprints/api/routes/smart-crud-route.json
Parameters: {'resourceName': 'user', 'modelName': 'User', 'authRequired': True, 'routePrefix': '/api/v1'}
"""

from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List, Optional
from sqlalchemy.orm import Session

from ...models.user_models import (
    UserCreate,
    UserUpdate,
    UserResponse
)
from ...services.user_service import UserService
from ...dependencies import get_db, get_current_user
from ...models.auth_models import User

router = APIRouter(
    prefix="/api/v1/users",
    tags=["users"]
)


@router.get("/", response_model=List[UserResponse])
async def list_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
) -> List[UserResponse]:
    """List users with pagination"""
    try:
        service = UserService(db)
        items = await service.get_users(skip=skip, limit=limit)
        return [UserResponse.from_orm(item) for item in items]
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to retrieve users")


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
) -> UserResponse:
    """Get user by ID"""
    try:
        service = UserService(db)
        item = await service.get_user(user_id)
        if not item:
            raise HTTPException(status_code=404, detail="User not found")
        return UserResponse.from_orm(item)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to retrieve user")


@router.post("/", response_model=UserResponse, status_code=201)
async def create_user(
    user_data: UserCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
) -> UserResponse:
    """Create new user"""
    try:
        service = UserService(db)
        item = await service.create_user(user_data)
        return UserResponse.from_orm(item)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to create user")


@router.put("/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: int,
    user_data: UserUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
) -> UserResponse:
    """Update user"""
    try:
        service = UserService(db)
        item = await service.update_user(user_id, user_data)
        if not item:
            raise HTTPException(status_code=404, detail="User not found")
        return UserResponse.from_orm(item)
    except HTTPException:
        raise
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to update user")


@router.delete("/{user_id}", status_code=204)
async def delete_user(
    user_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
) -> None:
    """Delete user"""
    try:
        service = UserService(db)
        success = await service.delete_user(user_id)
        if not success:
            raise HTTPException(status_code=404, detail="User not found")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to delete user")