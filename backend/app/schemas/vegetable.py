from pydantic import BaseModel, Field
from typing import Optional
from datetime import timedelta


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


class VegetableCreate(VegetableBase):
    pass


class Vegetable(VegetableBase):
    id: int

    class Config:
        orm_mode = True
