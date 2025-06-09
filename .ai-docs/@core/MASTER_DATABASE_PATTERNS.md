# MASTER DATABASE PATTERNS
**Single Source of Truth for FastAPI Database Integration Patterns**

## 🎯 Database Strategy Selection

### When to Choose Traditional Database
- ✅ Complex business logic requiring custom SQL
- ✅ Multi-database or hybrid cloud requirements
- ✅ Existing database infrastructure
- ✅ Advanced database features (stored procedures, triggers)
- ✅ Full control over schema and migrations
- ✅ Enterprise compliance requirements

### When to Choose Supabase
- ✅ Rapid prototyping and development
- ✅ Built-in authentication and authorization
- ✅ Real-time features required
- ✅ Integrated file storage needed
- ✅ Serverless/edge deployment
- ✅ Small to medium-scale applications

## 🗄️ Traditional Database Patterns

### Database Setup and Configuration
```python
# backend-mcp/database/connection.py
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://user:pass@localhost/db"
    database_echo: bool = False
    
    class Config:
        env_file = ".env"

settings = Settings()

# Async engine setup
engine = create_async_engine(
    settings.database_url,
    echo=settings.database_echo,
    pool_size=20,
    max_overflow=0,
    pool_pre_ping=True,
    pool_recycle=3600
)

AsyncSessionLocal = async_sessionmaker(
    engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)

class Base(DeclarativeBase):
    pass

# Dependency for FastAPI
async def get_db_session():
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
```

### SQLAlchemy Model Pattern
```python
# backend-mcp/database/models/user_db_model.py
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.sql import func
from ..connection import Base

class UserDBModel(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    name = Column(String(100), nullable=False)
    password_hash = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    def __repr__(self):
        return f"<User(id={self.id}, email='{self.email}')>"
```

### Repository Pattern (Traditional)
```python
# backend-mcp/database/repositories/user_repository.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from sqlalchemy.orm import selectinload
from typing import List, Optional
from ..models.user_db_model import UserDBModel
from ...models.user_model import UserCreateModel, UserUpdateModel

class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def create(self, user_data: UserCreateModel) -> UserDBModel:
        db_user = UserDBModel(**user_data.dict(exclude={'password'}))
        db_user.password_hash = hash_password(user_data.password)
        
        self.db.add(db_user)
        await self.db.flush()
        await self.db.refresh(db_user)
        return db_user
    
    async def get_by_id(self, user_id: int) -> Optional[UserDBModel]:
        result = await self.db.execute(
            select(UserDBModel).where(UserDBModel.id == user_id)
        )
        return result.scalar_one_or_none()
    
    async def get_by_email(self, email: str) -> Optional[UserDBModel]:
        result = await self.db.execute(
            select(UserDBModel).where(UserDBModel.email == email)
        )
        return result.scalar_one_or_none()
    
    async def get_all(self, skip: int = 0, limit: int = 100) -> List[UserDBModel]:
        result = await self.db.execute(
            select(UserDBModel)
            .offset(skip)
            .limit(limit)
            .order_by(UserDBModel.created_at.desc())
        )
        return result.scalars().all()
    
    async def update(self, user_id: int, user_data: UserUpdateModel) -> Optional[UserDBModel]:
        update_data = user_data.dict(exclude_unset=True)
        if update_data:
            await self.db.execute(
                update(UserDBModel)
                .where(UserDBModel.id == user_id)
                .values(**update_data)
            )
            return await self.get_by_id(user_id)
        return None
    
    async def delete(self, user_id: int) -> bool:
        result = await self.db.execute(
            delete(UserDBModel).where(UserDBModel.id == user_id)
        )
        return result.rowcount > 0
```

### Service Layer (Traditional)
```python
# backend-mcp/services/user_service.py
from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from ..database.connection import get_db_session
from ..database.repositories.user_repository import UserRepository
from ..models.user_model import UserModel, UserCreateModel, UserUpdateModel
from typing import List, Optional

class UserService:
    def __init__(self, db: AsyncSession = Depends(get_db_session)):
        self.repository = UserRepository(db)
    
    async def create_user(self, user_data: UserCreateModel) -> UserModel:
        # Check if user exists
        existing_user = await self.repository.get_by_email(user_data.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        
        db_user = await self.repository.create(user_data)
        return UserModel.from_orm(db_user)
    
    async def get_user_by_id(self, user_id: int) -> Optional[UserModel]:
        db_user = await self.repository.get_by_id(user_id)
        return UserModel.from_orm(db_user) if db_user else None
    
    async def get_users(self, skip: int = 0, limit: int = 100) -> List[UserModel]:
        db_users = await self.repository.get_all(skip, limit)
        return [UserModel.from_orm(user) for user in db_users]
    
    async def update_user(self, user_id: int, user_data: UserUpdateModel) -> Optional[UserModel]:
        db_user = await self.repository.update(user_id, user_data)
        return UserModel.from_orm(db_user) if db_user else None
    
    async def delete_user(self, user_id: int) -> bool:
        return await self.repository.delete(user_id)
```

## 🚀 Supabase Integration Patterns

### Supabase Setup and Configuration
```python
# backend-mcp/database/supabase_client.py
from supabase import create_client, Client
from pydantic import BaseSettings
from typing import Optional

class SupabaseSettings(BaseSettings):
    supabase_url: str
    supabase_anon_key: str
    supabase_service_key: str
    
    class Config:
        env_file = ".env"

settings = SupabaseSettings()

# Client instances
supabase_client: Client = create_client(settings.supabase_url, settings.supabase_anon_key)
supabase_admin: Client = create_client(settings.supabase_url, settings.supabase_service_key)

# Dependency for FastAPI
def get_supabase_client() -> Client:
    return supabase_client

def get_supabase_admin() -> Client:
    return supabase_admin
```

### Repository Pattern (Supabase)
```python
# backend-mcp/database/repositories/supabase_user_repository.py
from supabase import Client
from typing import List, Optional, Dict, Any
from ...models.user_model import UserCreateModel, UserUpdateModel
from fastapi import HTTPException, status

class SupabaseUserRepository:
    def __init__(self, supabase: Client):
        self.supabase = supabase
        self.table = "users"
    
    async def create(self, user_data: UserCreateModel) -> Dict[str, Any]:
        try:
            result = self.supabase.table(self.table).insert(user_data.dict()).execute()
            if result.data:
                return result.data[0]
            raise HTTPException(status_code=400, detail="Failed to create user")
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
    
    async def get_by_id(self, user_id: str) -> Optional[Dict[str, Any]]:
        result = self.supabase.table(self.table).select("*").eq('id', user_id).execute()
        return result.data[0] if result.data else None
    
    async def get_by_email(self, email: str) -> Optional[Dict[str, Any]]:
        result = self.supabase.table(self.table).select("*").eq('email', email).execute()
        return result.data[0] if result.data else None
    
    async def get_all(self, skip: int = 0, limit: int = 100) -> List[Dict[str, Any]]:
        result = self.supabase.table(self.table)\
            .select("*")\
            .range(skip, skip + limit - 1)\
            .order('created_at', desc=True)\
            .execute()
        return result.data
    
    async def update(self, user_id: str, user_data: UserUpdateModel) -> Optional[Dict[str, Any]]:
        update_data = user_data.dict(exclude_unset=True)
        if update_data:
            result = self.supabase.table(self.table)\
                .update(update_data)\
                .eq('id', user_id)\
                .execute()
            return result.data[0] if result.data else None
        return None
    
    async def delete(self, user_id: str) -> bool:
        result = self.supabase.table(self.table).delete().eq('id', user_id).execute()
        return len(result.data) > 0
```

### Service Layer (Supabase)
```python
# backend-mcp/services/supabase_user_service.py
from fastapi import Depends, HTTPException, status
from supabase import Client
from ..database.supabase_client import get_supabase_client
from ..database.repositories.supabase_user_repository import SupabaseUserRepository
from ..models.user_model import UserModel, UserCreateModel, UserUpdateModel
from typing import List, Optional

class SupabaseUserService:
    def __init__(self, supabase: Client = Depends(get_supabase_client)):
        self.repository = SupabaseUserRepository(supabase)
    
    async def create_user(self, user_data: UserCreateModel) -> UserModel:
        # Check if user exists
        existing_user = await self.repository.get_by_email(user_data.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        
        user_dict = await self.repository.create(user_data)
        return UserModel(**user_dict)
    
    async def get_user_by_id(self, user_id: str) -> Optional[UserModel]:
        user_dict = await self.repository.get_by_id(user_id)
        return UserModel(**user_dict) if user_dict else None
    
    async def get_users(self, skip: int = 0, limit: int = 100) -> List[UserModel]:
        users_data = await self.repository.get_all(skip, limit)
        return [UserModel(**user) for user in users_data]
    
    async def update_user(self, user_id: str, user_data: UserUpdateModel) -> Optional[UserModel]:
        user_dict = await self.repository.update(user_id, user_data)
        return UserModel(**user_dict) if user_dict else None
    
    async def delete_user(self, user_id: str) -> bool:
        return await self.repository.delete(user_id)
```

## 🔒 Authentication Patterns

### Traditional Database Authentication
```python
# backend-mcp/services/auth_service.py
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import HTTPException, status

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    def __init__(self, user_service: UserService = Depends()):
        self.user_service = user_service
        self.secret_key = settings.secret_key
        self.algorithm = "HS256"

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password: str) -> str:
        return pwd_context.hash(password)

    def create_access_token(self, data: dict, expires_delta: timedelta = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
        return encoded_jwt
```

### Supabase Authentication
```python
# backend-mcp/services/supabase_auth_service.py
from supabase import Client
from fastapi import HTTPException, status

class SupabaseAuthService:
    def __init__(self, supabase: Client = Depends(get_supabase_client)):
        self.supabase = supabase

    async def sign_up(self, email: str, password: str) -> dict:
        try:
            result = self.supabase.auth.sign_up({
                "email": email,
                "password": password
            })
            return result
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    async def sign_in(self, email: str, password: str) -> dict:
        try:
            result = self.supabase.auth.sign_in_with_password({
                "email": email,
                "password": password
            })
            return result
        except Exception as e:
            raise HTTPException(status_code=401, detail="Invalid credentials")

    async def get_user(self, token: str) -> dict:
        try:
            result = self.supabase.auth.get_user(token)
            return result
        except Exception as e:
            raise HTTPException(status_code=401, detail="Invalid token")
```

## 📁 File Storage Patterns

### Traditional File Storage
```python
# backend-mcp/services/file_service.py
import os
import uuid
from fastapi import UploadFile, HTTPException
from pathlib import Path

class FileService:
    def __init__(self):
        self.upload_dir = Path("uploads")
        self.upload_dir.mkdir(exist_ok=True)

    async def upload_file(self, file: UploadFile) -> str:
        file_id = str(uuid.uuid4())
        file_extension = Path(file.filename).suffix
        file_path = self.upload_dir / f"{file_id}{file_extension}"

        try:
            with open(file_path, "wb") as buffer:
                content = await file.read()
                buffer.write(content)
            return str(file_path)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"File upload failed: {str(e)}")

    async def delete_file(self, file_path: str) -> bool:
        try:
            Path(file_path).unlink()
            return True
        except Exception:
            return False
```

### Supabase Storage
```python
# backend-mcp/services/supabase_storage_service.py
from supabase import Client
import uuid
from fastapi import UploadFile, HTTPException

class SupabaseStorageService:
    def __init__(self, supabase: Client = Depends(get_supabase_client)):
        self.supabase = supabase
        self.bucket = "uploads"

    async def upload_file(self, file: UploadFile) -> dict:
        file_id = str(uuid.uuid4())
        file_path = f"{file_id}/{file.filename}"

        try:
            content = await file.read()
            result = self.supabase.storage.from_(self.bucket).upload(file_path, content)

            if result.get('error'):
                raise HTTPException(status_code=400, detail=result['error']['message'])

            public_url = self.supabase.storage.from_(self.bucket).get_public_url(file_path)

            return {
                "file_path": file_path,
                "public_url": public_url,
                "file_name": file.filename
            }
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")

    def get_signed_url(self, file_path: str, expires_in: int = 3600) -> str:
        return self.supabase.storage.from_(self.bucket).create_signed_url(file_path, expires_in)

    async def delete_file(self, file_path: str) -> bool:
        try:
            result = self.supabase.storage.from_(self.bucket).remove([file_path])
            return not result.get('error')
        except Exception:
            return False
```

## 🔄 Migration Between Patterns

### From Traditional to Supabase
```python
# scripts/migrate_to_supabase.py
import asyncio
from sqlalchemy import select
from backend_mcp.database.connection import AsyncSessionLocal
from backend_mcp.database.models.user_db_model import UserDBModel
from backend_mcp.database.supabase_client import supabase_admin

async def migrate_users():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(UserDBModel))
        users = result.scalars().all()

        for user in users:
            supabase_data = {
                "email": user.email,
                "name": user.name,
                "is_active": user.is_active,
                "created_at": user.created_at.isoformat(),
                "updated_at": user.updated_at.isoformat() if user.updated_at else None
            }

            result = supabase_admin.table('users').insert(supabase_data).execute()
            print(f"Migrated user: {user.email}")

if __name__ == "__main__":
    asyncio.run(migrate_users())
```

### From Supabase to Traditional
```python
# scripts/migrate_from_supabase.py
import asyncio
from backend_mcp.database.connection import AsyncSessionLocal
from backend_mcp.database.models.user_db_model import UserDBModel
from backend_mcp.database.supabase_client import supabase_admin

async def migrate_from_supabase():
    # Get all users from Supabase
    result = supabase_admin.table('users').select("*").execute()
    users = result.data

    async with AsyncSessionLocal() as session:
        for user_data in users:
            db_user = UserDBModel(
                email=user_data['email'],
                name=user_data['name'],
                is_active=user_data['is_active'],
                password_hash="MIGRATED_USER_NEEDS_PASSWORD_RESET"
            )
            session.add(db_user)

        await session.commit()
        print(f"Migrated {len(users)} users from Supabase")

if __name__ == "__main__":
    asyncio.run(migrate_from_supabase())
```

## 🧪 Testing Strategies

### Traditional Database Testing
```python
# tests/conftest.py
import pytest
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from backend_mcp.database.connection import Base, get_db_session
from backend_mcp.main import app

# Test database URL
TEST_DATABASE_URL = "postgresql+asyncpg://test:test@localhost/test_db"

@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="session")
async def test_engine():
    engine = create_async_engine(TEST_DATABASE_URL, echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield engine
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await engine.dispose()

@pytest.fixture
async def test_db_session(test_engine):
    TestSessionLocal = async_sessionmaker(test_engine, expire_on_commit=False)
    async with TestSessionLocal() as session:
        yield session
        await session.rollback()

@pytest.fixture
def test_client(test_db_session):
    def override_get_db():
        yield test_db_session

    app.dependency_overrides[get_db_session] = override_get_db
    with TestClient(app) as client:
        yield client
    app.dependency_overrides.clear()
```

### Supabase Testing
```python
# tests/supabase_conftest.py
import pytest
from supabase import create_client
from backend_mcp.database.supabase_client import get_supabase_client
from backend_mcp.main import app

# Test Supabase project
TEST_SUPABASE_URL = "https://test-project.supabase.co"
TEST_SUPABASE_KEY = "test-anon-key"

@pytest.fixture
def test_supabase_client():
    return create_client(TEST_SUPABASE_URL, TEST_SUPABASE_KEY)

@pytest.fixture
def test_client_supabase(test_supabase_client):
    def override_get_supabase():
        return test_supabase_client

    app.dependency_overrides[get_supabase_client] = override_get_supabase
    with TestClient(app) as client:
        yield client
    app.dependency_overrides.clear()

@pytest.fixture(autouse=True)
async def cleanup_test_data(test_supabase_client):
    # Setup
    yield
    # Cleanup - remove test data
    test_supabase_client.table('users').delete().neq('id', 'keep-this-id').execute()
```

---

**Authority**: This file is the single source of truth for all database patterns. Choose the appropriate pattern based on your project requirements.

**Last Updated**: 2025-01-07
**Version**: 1.0.0
