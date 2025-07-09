# app/schemas/material.py
import enum
from pydantic import BaseModel, Field
from typing import Optional, List

from app.schemas.minimals import VegetableMinimal, MaterialMinimal


class MaterialType(str, enum.Enum):
    SOIL = "soil"
    FERTILISER = "fertiliser"
    PESTICIDE = "pesticide"
    TOOLS = "tools"


class MaterialBase(BaseModel):
    name: str = Field(..., example="Premium Potting Mix")
    type: MaterialType
    image: Optional[str] = Field(None, example="http://example.com/soil.jpg")
    description: str


class MaterialCreate(MaterialBase):
    vegetable_ids: Optional[List[int]] = Field(
        None,
        description="Optional list of IDs of vegetables to associate this material with."
    )


class Material(MaterialBase):
    id: int
    # Use the directly imported type (NO QUOTES)
    vegetables: List[VegetableMinimal] = []

    class Config:
        from_attributes = True


class MaterialUpdate(MaterialBase):
    name: Optional[str] = None
    type: Optional[MaterialType] = None
    vegetable_ids: Optional[List[int]] = Field(
        None,
        description="Optional list of IDs of vegetables to associate/dissociate this material with (replaces current associations)."
    )
