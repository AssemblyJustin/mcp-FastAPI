# @database-blueprint-examples

**AI Context**: Smart blueprint examples for both database patterns. ALWAYS load `.ai-docs/@core/MASTER_DATABASE_PATTERNS.md` first.

## ⚠️ CRITICAL: Load Master Files First
```
1. .ai-docs/@core/MASTER_DATABASE_PATTERNS.md (database patterns)
2. .ai-docs/@core/MASTER_CONVENTIONS.md (conventions)
3. .ai-docs/@core/MASTER_ARCHITECTURE.md (architecture)
```

## 🗄️ Traditional Database Blueprints

### Traditional Service Blueprint
```json
{
  "metadata": {
    "name": "create-traditional-service",
    "version": "1.0.0",
    "category": "services",
    "description": "Creates FastAPI service with traditional database (SQLAlchemy)"
  },
  "template": {
    "embedded_code": "# Traditional Database Service Template\nfrom fastapi import Depends, HTTPException, status\nfrom sqlalchemy.ext.asyncio import AsyncSession\nfrom ..database.connection import get_db_session\nfrom ..database.repositories.{{resource}}_repository import {{Resource}}Repository\nfrom ..models.{{resource}}_model import {{Resource}}Model, {{Resource}}CreateModel, {{Resource}}UpdateModel\nfrom typing import List, Optional\n\nclass {{Resource}}Service:\n    def __init__(self, db: AsyncSession = Depends(get_db_session)):\n        self.repository = {{Resource}}Repository(db)\n    \n    async def create_{{resource}}(self, {{resource}}_data: {{Resource}}CreateModel) -> {{Resource}}Model:\n        # Business logic validation\n        existing = await self.repository.get_by_email({{resource}}_data.email)\n        if existing:\n            raise HTTPException(\n                status_code=status.HTTP_400_BAD_REQUEST,\n                detail=\"{{Resource}} already exists\"\n            )\n        \n        db_{{resource}} = await self.repository.create({{resource}}_data)\n        return {{Resource}}Model.from_orm(db_{{resource}})\n    \n    async def get_{{resource}}_by_id(self, {{resource}}_id: int) -> Optional[{{Resource}}Model]:\n        db_{{resource}} = await self.repository.get_by_id({{resource}}_id)\n        return {{Resource}}Model.from_orm(db_{{resource}}) if db_{{resource}} else None\n    \n    async def get_{{resource}}s(self, skip: int = 0, limit: int = 100) -> List[{{Resource}}Model]:\n        db_{{resource}}s = await self.repository.get_all(skip, limit)\n        return [{{Resource}}Model.from_orm({{resource}}) for {{resource}} in db_{{resource}}s]\n    \n    async def update_{{resource}}(self, {{resource}}_id: int, {{resource}}_data: {{Resource}}UpdateModel) -> Optional[{{Resource}}Model]:\n        db_{{resource}} = await self.repository.update({{resource}}_id, {{resource}}_data)\n        return {{Resource}}Model.from_orm(db_{{resource}}) if db_{{resource}} else None\n    \n    async def delete_{{resource}}(self, {{resource}}_id: int) -> bool:\n        return await self.repository.delete({{resource}}_id)",
    "dependencies": ["fastapi", "sqlalchemy", "asyncpg"],
    "imports": [
      "from fastapi import Depends, HTTPException, status",
      "from sqlalchemy.ext.asyncio import AsyncSession",
      "from typing import List, Optional"
    ]
  },
  "parameters": {
    "resource": {"type": "string", "required": true, "description": "Resource name (snake_case)"},
    "Resource": {"type": "string", "required": true, "description": "Resource name (PascalCase)"}
  },
  "validation": {
    "required_files": [
      "models/{{resource}}_model.py",
      "database/repositories/{{resource}}_repository.py",
      "database/models/{{resource}}_db_model.py"
    ],
    "test_requirements": ["unit", "integration"],
    "performance_targets": {"response_time": "< 500ms"}
  },
  "relationships": {
    "depends_on": ["create-traditional-repository", "create-traditional-db-model"],
    "generates": ["services/{{resource}}_service.py"]
  }
}
```

### Traditional Repository Blueprint
```json
{
  "metadata": {
    "name": "create-traditional-repository",
    "version": "1.0.0",
    "category": "repositories",
    "description": "Creates repository with SQLAlchemy async patterns"
  },
  "template": {
    "embedded_code": "# Traditional Database Repository Template\nfrom sqlalchemy.ext.asyncio import AsyncSession\nfrom sqlalchemy import select, update, delete\nfrom typing import List, Optional\nfrom ..models.{{resource}}_db_model import {{Resource}}DBModel\nfrom ...models.{{resource}}_model import {{Resource}}CreateModel, {{Resource}}UpdateModel\n\nclass {{Resource}}Repository:\n    def __init__(self, db: AsyncSession):\n        self.db = db\n    \n    async def create(self, {{resource}}_data: {{Resource}}CreateModel) -> {{Resource}}DBModel:\n        db_{{resource}} = {{Resource}}DBModel(**{{resource}}_data.dict())\n        self.db.add(db_{{resource}})\n        await self.db.flush()\n        await self.db.refresh(db_{{resource}})\n        return db_{{resource}}\n    \n    async def get_by_id(self, {{resource}}_id: int) -> Optional[{{Resource}}DBModel]:\n        result = await self.db.execute(\n            select({{Resource}}DBModel).where({{Resource}}DBModel.id == {{resource}}_id)\n        )\n        return result.scalar_one_or_none()\n    \n    async def get_all(self, skip: int = 0, limit: int = 100) -> List[{{Resource}}DBModel]:\n        result = await self.db.execute(\n            select({{Resource}}DBModel)\n            .offset(skip)\n            .limit(limit)\n            .order_by({{Resource}}DBModel.created_at.desc())\n        )\n        return result.scalars().all()\n    \n    async def update(self, {{resource}}_id: int, {{resource}}_data: {{Resource}}UpdateModel) -> Optional[{{Resource}}DBModel]:\n        update_data = {{resource}}_data.dict(exclude_unset=True)\n        if update_data:\n            await self.db.execute(\n                update({{Resource}}DBModel)\n                .where({{Resource}}DBModel.id == {{resource}}_id)\n                .values(**update_data)\n            )\n            return await self.get_by_id({{resource}}_id)\n        return None\n    \n    async def delete(self, {{resource}}_id: int) -> bool:\n        result = await self.db.execute(\n            delete({{Resource}}DBModel).where({{Resource}}DBModel.id == {{resource}}_id)\n        )\n        return result.rowcount > 0",
    "dependencies": ["sqlalchemy", "asyncpg"],
    "imports": [
      "from sqlalchemy.ext.asyncio import AsyncSession",
      "from sqlalchemy import select, update, delete",
      "from typing import List, Optional"
    ]
  },
  "parameters": {
    "resource": {"type": "string", "required": true},
    "Resource": {"type": "string", "required": true}
  },
  "validation": {
    "required_files": ["database/models/{{resource}}_db_model.py"],
    "test_requirements": ["unit", "integration"],
    "performance_targets": {"query_time": "< 100ms"}
  }
}
```

## 🚀 Supabase Integration Blueprints

### Supabase Service Blueprint
```json
{
  "metadata": {
    "name": "create-supabase-service",
    "version": "1.0.0",
    "category": "services",
    "description": "Creates FastAPI service with Supabase integration"
  },
  "template": {
    "embedded_code": "# Supabase Service Template\nfrom fastapi import Depends, HTTPException, status\nfrom supabase import Client\nfrom ..database.supabase_client import get_supabase_client\nfrom ..database.repositories.supabase_{{resource}}_repository import Supabase{{Resource}}Repository\nfrom ..models.{{resource}}_model import {{Resource}}Model, {{Resource}}CreateModel, {{Resource}}UpdateModel\nfrom typing import List, Optional\n\nclass Supabase{{Resource}}Service:\n    def __init__(self, supabase: Client = Depends(get_supabase_client)):\n        self.repository = Supabase{{Resource}}Repository(supabase)\n    \n    async def create_{{resource}}(self, {{resource}}_data: {{Resource}}CreateModel) -> {{Resource}}Model:\n        # Business logic validation\n        existing = await self.repository.get_by_email({{resource}}_data.email)\n        if existing:\n            raise HTTPException(\n                status_code=status.HTTP_400_BAD_REQUEST,\n                detail=\"{{Resource}} already exists\"\n            )\n        \n        {{resource}}_dict = await self.repository.create({{resource}}_data)\n        return {{Resource}}Model(**{{resource}}_dict)\n    \n    async def get_{{resource}}_by_id(self, {{resource}}_id: str) -> Optional[{{Resource}}Model]:\n        {{resource}}_dict = await self.repository.get_by_id({{resource}}_id)\n        return {{Resource}}Model(**{{resource}}_dict) if {{resource}}_dict else None\n    \n    async def get_{{resource}}s(self, skip: int = 0, limit: int = 100) -> List[{{Resource}}Model]:\n        {{resource}}s_data = await self.repository.get_all(skip, limit)\n        return [{{Resource}}Model(**{{resource}}) for {{resource}} in {{resource}}s_data]\n    \n    async def update_{{resource}}(self, {{resource}}_id: str, {{resource}}_data: {{Resource}}UpdateModel) -> Optional[{{Resource}}Model]:\n        {{resource}}_dict = await self.repository.update({{resource}}_id, {{resource}}_data)\n        return {{Resource}}Model(**{{resource}}_dict) if {{resource}}_dict else None\n    \n    async def delete_{{resource}}(self, {{resource}}_id: str) -> bool:\n        return await self.repository.delete({{resource}}_id)\n    \n    async def setup_realtime_subscription(self, callback):\n        \"\"\"Setup real-time subscription for {{resource}} changes\"\"\"\n        return self.repository.setup_realtime(callback)",
    "dependencies": ["fastapi", "supabase"],
    "imports": [
      "from fastapi import Depends, HTTPException, status",
      "from supabase import Client",
      "from typing import List, Optional"
    ]
  },
  "parameters": {
    "resource": {"type": "string", "required": true, "description": "Resource name (snake_case)"},
    "Resource": {"type": "string", "required": true, "description": "Resource name (PascalCase)"}
  },
  "validation": {
    "required_files": [
      "models/{{resource}}_model.py",
      "database/repositories/supabase_{{resource}}_repository.py"
    ],
    "test_requirements": ["unit", "integration"],
    "performance_targets": {"response_time": "< 300ms"}
  },
  "relationships": {
    "depends_on": ["create-supabase-repository"],
    "generates": ["services/supabase_{{resource}}_service.py"]
  }
}
```

### Supabase Repository Blueprint
```json
{
  "metadata": {
    "name": "create-supabase-repository",
    "version": "1.0.0",
    "category": "repositories",
    "description": "Creates repository with Supabase client patterns"
  },
  "template": {
    "embedded_code": "# Supabase Repository Template\nfrom supabase import Client\nfrom typing import List, Optional, Dict, Any\nfrom ...models.{{resource}}_model import {{Resource}}CreateModel, {{Resource}}UpdateModel\nfrom fastapi import HTTPException, status\n\nclass Supabase{{Resource}}Repository:\n    def __init__(self, supabase: Client):\n        self.supabase = supabase\n        self.table = \"{{resource}}s\"\n    \n    async def create(self, {{resource}}_data: {{Resource}}CreateModel) -> Dict[str, Any]:\n        try:\n            result = self.supabase.table(self.table).insert({{resource}}_data.dict()).execute()\n            if result.data:\n                return result.data[0]\n            raise HTTPException(status_code=400, detail=\"Failed to create {{resource}}\")\n        except Exception as e:\n            raise HTTPException(status_code=400, detail=str(e))\n    \n    async def get_by_id(self, {{resource}}_id: str) -> Optional[Dict[str, Any]]:\n        result = self.supabase.table(self.table).select(\"*\").eq('id', {{resource}}_id).execute()\n        return result.data[0] if result.data else None\n    \n    async def get_by_email(self, email: str) -> Optional[Dict[str, Any]]:\n        result = self.supabase.table(self.table).select(\"*\").eq('email', email).execute()\n        return result.data[0] if result.data else None\n    \n    async def get_all(self, skip: int = 0, limit: int = 100) -> List[Dict[str, Any]]:\n        result = self.supabase.table(self.table)\\\n            .select(\"*\")\\\n            .range(skip, skip + limit - 1)\\\n            .order('created_at', desc=True)\\\n            .execute()\n        return result.data\n    \n    async def update(self, {{resource}}_id: str, {{resource}}_data: {{Resource}}UpdateModel) -> Optional[Dict[str, Any]]:\n        update_data = {{resource}}_data.dict(exclude_unset=True)\n        if update_data:\n            result = self.supabase.table(self.table)\\\n                .update(update_data)\\\n                .eq('id', {{resource}}_id)\\\n                .execute()\n            return result.data[0] if result.data else None\n        return None\n    \n    async def delete(self, {{resource}}_id: str) -> bool:\n        result = self.supabase.table(self.table).delete().eq('id', {{resource}}_id).execute()\n        return len(result.data) > 0\n    \n    def setup_realtime(self, callback):\n        \"\"\"Setup real-time subscription for table changes\"\"\"\n        return self.supabase.postgrest.realtime.on(\n            f\"public:{self.table}\",\n            callback\n        ).subscribe()",
    "dependencies": ["supabase"],
    "imports": [
      "from supabase import Client",
      "from typing import List, Optional, Dict, Any",
      "from fastapi import HTTPException, status"
    ]
  },
  "parameters": {
    "resource": {"type": "string", "required": true},
    "Resource": {"type": "string", "required": true}
  },
  "validation": {
    "test_requirements": ["unit", "integration"],
    "performance_targets": {"query_time": "< 200ms"}
  }
}
```

## 🔄 Universal Route Blueprint

### Database-Agnostic Route Blueprint
```json
{
  "metadata": {
    "name": "create-universal-route",
    "version": "1.0.0",
    "category": "routes",
    "description": "Creates FastAPI route that works with both database patterns"
  },
  "template": {
    "embedded_code": "# Universal Route Template (works with both database patterns)\nfrom fastapi import APIRouter, Depends, HTTPException, status, Query\nfrom typing import List, Union\nfrom ..services.{{resource}}_service import {{Resource}}Service\nfrom ..models.{{resource}}_model import {{Resource}}Model, {{Resource}}CreateModel, {{Resource}}UpdateModel\nfrom ..middleware.auth import get_current_user\n\nrouter = APIRouter(\n    prefix=\"/api/v1/{{resource}}s\",\n    tags=[\"{{resource}}s\"],\n    dependencies=[Depends(get_current_user)]\n)\n\n@router.post(\"/\", response_model={{Resource}}Model, status_code=status.HTTP_201_CREATED)\nasync def create_{{resource}}(\n    {{resource}}_data: {{Resource}}CreateModel,\n    service: {{Resource}}Service = Depends()\n):\n    \"\"\"Create a new {{resource}}\"\"\"\n    try:\n        return await service.create_{{resource}}({{resource}}_data)\n    except ValueError as e:\n        raise HTTPException(status_code=400, detail=str(e))\n\n@router.get(\"/\", response_model=List[{{Resource}}Model])\nasync def get_{{resource}}s(\n    skip: int = Query(0, ge=0),\n    limit: int = Query(100, ge=1, le=1000),\n    service: {{Resource}}Service = Depends()\n):\n    \"\"\"Get all {{resource}}s with pagination\"\"\"\n    return await service.get_{{resource}}s(skip=skip, limit=limit)\n\n@router.get(\"/{{{resource}}_id}\", response_model={{Resource}}Model)\nasync def get_{{resource}}(\n    {{resource}}_id: Union[int, str],  # Flexible for both int and UUID\n    service: {{Resource}}Service = Depends()\n):\n    \"\"\"Get {{resource}} by ID\"\"\"\n    {{resource}} = await service.get_{{resource}}_by_id({{resource}}_id)\n    if not {{resource}}:\n        raise HTTPException(\n            status_code=status.HTTP_404_NOT_FOUND,\n            detail=\"{{Resource}} not found\"\n        )\n    return {{resource}}\n\n@router.put(\"/{{{resource}}_id}\", response_model={{Resource}}Model)\nasync def update_{{resource}}(\n    {{resource}}_id: Union[int, str],\n    {{resource}}_data: {{Resource}}UpdateModel,\n    service: {{Resource}}Service = Depends()\n):\n    \"\"\"Update {{resource}} by ID\"\"\"\n    {{resource}} = await service.update_{{resource}}({{resource}}_id, {{resource}}_data)\n    if not {{resource}}:\n        raise HTTPException(\n            status_code=status.HTTP_404_NOT_FOUND,\n            detail=\"{{Resource}} not found\"\n        )\n    return {{resource}}\n\n@router.delete(\"/{{{resource}}_id}\", status_code=status.HTTP_204_NO_CONTENT)\nasync def delete_{{resource}}(\n    {{resource}}_id: Union[int, str],\n    service: {{Resource}}Service = Depends()\n):\n    \"\"\"Delete {{resource}} by ID\"\"\"\n    success = await service.delete_{{resource}}({{resource}}_id)\n    if not success:\n        raise HTTPException(\n            status_code=status.HTTP_404_NOT_FOUND,\n            detail=\"{{Resource}} not found\"\n        )",
    "dependencies": ["fastapi"],
    "imports": [
      "from fastapi import APIRouter, Depends, HTTPException, status, Query",
      "from typing import List, Union"
    ]
  },
  "parameters": {
    "resource": {"type": "string", "required": true},
    "Resource": {"type": "string", "required": true}
  },
  "validation": {
    "required_files": ["services/{{resource}}_service.py", "models/{{resource}}_model.py"],
    "test_requirements": ["unit", "integration", "load"],
    "performance_targets": {"response_time": "< 200ms"}
  }
}
```

## 🏥 Production System Blueprints

### Health Check Route Blueprint
```json
{
  "metadata": {
    "name": "create-health-check-route",
    "version": "1.0.0",
    "category": "system",
    "description": "Creates production-ready health check endpoints"
  },
  "template": {
    "embedded_code": "# Health Check Route Template\nfrom fastapi import APIRouter, Depends\nfrom datetime import datetime\nfrom typing import Dict, Any\nfrom ..config.settings import settings\n\nrouter = APIRouter(prefix=\"/system\", tags=[\"system\"])\n\n@router.get(\"/health\", response_model=Dict[str, Any])\nasync def health_check():\n    \"\"\"Health check for load balancers and monitoring.\"\"\"\n    health_status = {\n        \"status\": \"healthy\",\n        \"timestamp\": datetime.utcnow().isoformat(),\n        \"version\": settings.app_version,\n        \"environment\": settings.environment\n    }\n    \n    # Database health check\n    try:\n        # Add database-specific health check here\n        health_status[\"database\"] = \"healthy\"\n    except Exception:\n        health_status[\"database\"] = \"unhealthy\"\n        health_status[\"status\"] = \"degraded\"\n    \n    return health_status\n\n@router.get(\"/ready\")\nasync def readiness_check():\n    \"\"\"Readiness check for Kubernetes.\"\"\"\n    return {\"status\": \"ready\", \"timestamp\": datetime.utcnow().isoformat()}",
    "dependencies": ["fastapi"],
    "imports": [
      "from fastapi import APIRouter",
      "from datetime import datetime",
      "from typing import Dict, Any"
    ]
  },
  "parameters": {},
  "validation": {
    "test_requirements": ["unit", "integration"],
    "performance_targets": {"response_time": "< 50ms"}
  },
  "relationships": {
    "generates": ["routes/system_routes.py"]
  }
}
```

### Rate Limited Route Blueprint
```json
{
  "metadata": {
    "name": "create-rate-limited-route",
    "version": "1.0.0",
    "category": "routes",
    "description": "Creates FastAPI route with rate limiting"
  },
  "template": {
    "embedded_code": "# Rate Limited Route Template\nfrom fastapi import APIRouter, Depends, Request\nfrom slowapi import Limiter\nfrom slowapi.util import get_remote_address\nfrom ..services.{{resource}}_service import {{Resource}}Service\nfrom ..models.{{resource}}_model import {{Resource}}Model, {{Resource}}CreateModel\n\nlimiter = Limiter(key_func=get_remote_address)\nrouter = APIRouter(prefix=\"/api/v1/{{resource}}s\", tags=[\"{{resource}}s\"])\n\n@router.post(\"/\", response_model={{Resource}}Model)\n@limiter.limit(\"5/minute\")  # Prevent abuse\nasync def create_{{resource}}(\n    request: Request,\n    {{resource}}_data: {{Resource}}CreateModel,\n    service: {{Resource}}Service = Depends()\n):\n    \"\"\"Create {{resource}} with rate limiting.\"\"\"\n    return await service.create_{{resource}}({{resource}}_data)\n\n@router.get(\"/\", response_model=List[{{Resource}}Model])\n@limiter.limit(\"100/minute\")  # Higher limit for reads\nasync def get_{{resource}}s(\n    request: Request,\n    service: {{Resource}}Service = Depends()\n):\n    \"\"\"Get {{resource}}s with rate limiting.\"\"\"\n    return await service.get_{{resource}}s()",
    "dependencies": ["fastapi", "slowapi"],
    "imports": [
      "from fastapi import APIRouter, Depends, Request",
      "from slowapi import Limiter",
      "from slowapi.util import get_remote_address"
    ]
  },
  "parameters": {
    "resource": {"type": "string", "required": true},
    "Resource": {"type": "string", "required": true}
  },
  "validation": {
    "required_files": ["services/{{resource}}_service.py"],
    "test_requirements": ["unit", "integration", "security"],
    "performance_targets": {"response_time": "< 200ms"}
  }
}
```

---

**Authority**: This file provides blueprint examples for both database patterns. Always reference the master database patterns file for complete implementation details.

**Last Updated**: 2025-01-07
**Version**: 1.0.0
