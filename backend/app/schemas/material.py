# app/schemas/material.py
import enum
from pydantic import BaseModel, Field
from typing import Optional


class MaterialType(str, enum.Enum):
    SOIL = "soil"
    FERTILISER = "fertiliser"
    PESTICIDE = "pesticide"
    TOOLS = "tools"


class MaterialBase(BaseModel):
    name: str = Field(..., example="Premium Potting Mix")
    type: MaterialType
    vegetable_id: int
    image: Optional[str] = Field(None, example="http://example.com/soil.jpg")


class MaterialCreate(MaterialBase):
    pass


class Material(MaterialBase):
    id: int

    class Config:
        orm_mode = True
