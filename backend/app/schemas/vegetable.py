from pydantic import BaseModel, Field, computed_field
from typing import Optional, List
from datetime import timedelta

from app.schemas.minimals import MaterialMinimal, VegetableMinimal


class VegetableBase(BaseModel):
    name: str = Field(..., example="Kangkung")
    estimated_harvest_time: Optional[timedelta] = Field(None, example="P42D")
    watering_frequency: Optional[timedelta] = Field(None, example="P2D")
    amount_of_sunlight: Optional[str] = Field(
        None, example="6 hours of direct sunlight"
    )
    image_url: Optional[str] = Field(None, example="http://example.com/kangkung.jpg")
    planting_instructions: Optional[str] = Field(
        None, example="Plant in fertile soil..."
    )

    @computed_field
    def estimated_harvest_time_formatted(self) -> str:
        if self.estimated_harvest_time:
            days = self.estimated_harvest_time.days
            return f"{days} Days"

    @computed_field
    def estimated_harvest_time_in_seconds(self) -> int:
        return self.estimated_harvest_time.total_seconds()

    @computed_field
    def watering_frequency_formatted(self) -> Optional[str]:
        if self.watering_frequency is None:
            return None
        days = self.watering_frequency.days
        if days == 1:
            return "Daily"
        else:
            return f"Every {days} days"


class VegetableCreate(VegetableBase):
    material_ids: Optional[List[int]] = Field(
        None,
        description="Optional list of IDs of materials to associate this vegetable with.",
    )


class VegetableUpdate(VegetableBase):
    name: Optional[str] = None
    estimated_harvest_time: Optional[timedelta] = None
    watering_frequency: Optional[timedelta] = None
    amount_of_sunlight: Optional[str] = None
    image_url: Optional[str] = None
    planting_instructions: Optional[str] = None
    material_ids: Optional[List[int]] = Field(
        None,
        description="Optional list of IDs of materials to associate/dissociate this vegetable with (replaces current associations).",
    )


class Vegetable(VegetableBase):
    id: int
    materials: List[MaterialMinimal] = []

    class Config:
        from_attributes = True
