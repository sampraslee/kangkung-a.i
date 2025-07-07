from pydantic import BaseModel, Field, computed_field
from typing import Optional
from datetime import timedelta
import humanize


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
        return humanize.naturaldelta(self.estimated_harvest_time, months=True)

    @computed_field
    def estimated_harvest_time_in_seconds(self) -> int:
        return self.estimated_harvest_time.total_seconds()

    @computed_field
    def watering_frequency_formatted(self) -> str:
        return humanize.naturaldelta(self.watering_frequency)


class VegetableCreate(VegetableBase):
    pass


class Vegetable(VegetableBase):
    id: int

    class Config:
        orm_mode = True
