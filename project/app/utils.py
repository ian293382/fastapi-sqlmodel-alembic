from pydantic import BaseModel, create_model
from typing import Dict, Any, Type

from sqlmodel import SQLModel

def get_table_columns(model: Type[SQLModel]) -> Dict[str, Any]:
    return {
        field_name: (field.type_, ... if field.required else None)
        for field_name, field in model.__fields__.items()
        if field_name != 'id'  # 排除 id 字段
    }

def create_dynamic_model(name: str, fields: Dict[str, Any]) -> Type[BaseModel]:
    class Config:
        orm_mode = True

    return create_model(
        name,
        **fields,
        __config__=Config
    )

def get_dynamic_model(model: Type[SQLModel], model_name: str) -> Type[BaseModel]:
    columns = get_table_columns(model)
    return create_dynamic_model(model_name, columns)