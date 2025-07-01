# app/schemas/minimals.py
from pydantic import BaseModel
from typing import Optional
import enum


class MaterialType(str, enum.Enum):
    SOIL = "soil"
    FERTILISER = "fertiliser"
    PESTICIDE = "pesticide"
    TOOLS = "tools"


class MaterialMinimal(BaseModel):
    id: int
    name: str
    type: MaterialType
    image: Optional[str] = None

    class Config:
        from_attributes = True


class VegetableMinimal(BaseModel):
    id: int
    name: str
    image_url: Optional[str] = None

    class Config:
        from_attributes = True
