"""Blueprint Models - TO BE IMPLEMENTED"""
from pydantic import BaseModel
from typing import Dict, Any

class Blueprint(BaseModel):
    name: str
    action: str
    layer: str
    resource: str
    template: Dict[str, Any]
