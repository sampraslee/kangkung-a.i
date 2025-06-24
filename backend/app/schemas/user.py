from pydantic import BaseModel, Field


class UserBase(BaseModel):
    username: str = Field(..., example="Aina")


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
