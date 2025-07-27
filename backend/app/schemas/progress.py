from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime, date


class ProgressBase(BaseModel):
    vegeNickname: Optional[str] = Field(None)
    lastWatered: Optional[datetime] = Field(None)
    lastFertilized: Optional[datetime] = Field(None)
    lastCheckup: Optional[date] = Field(None)
    checkUpNotes: Optional[str] = Field(
        None, example="Started planting. This is my first checkup.")
    startDate: Optional[datetime] = None


class ProgressCreate(ProgressBase):
    user_id: int
    vegetable_id: int


class ProgressUpdate(ProgressBase):
    pass


class Progress(ProgressBase):
    id: int
    user_id: int
    vegetable_id: int
    startDate: datetime
    expectedHarvestDate: Optional[date]

    class Config:
        orm_mode = True
