from sqlalchemy import Column, Integer, String, Text, Interval
from sqlalchemy.orm import relationship
from app.core.database import Base


class Vegetable(Base):
    __tablename__ = "vegetables"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    estimated_harvest_time = Column(Interval, nullable=True)
    water_needs = Column(Interval, nullable=True)
    sunlight_needs = Column(String, nullable=True)
    image_url = Column(String, nullable=True)
    instruction = Column(Text, nullable=True)
    user_vegetable_progress = relationship(
        "UserVegetableProgress", back_populates="vegetable"
    )

    def __repr__(self):
        return f"<Vegetable(id={self.id}, name='{self.name}')>"
