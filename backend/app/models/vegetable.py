from sqlalchemy import Column, Integer, String, Text, Interval
from sqlalchemy.orm import relationship
from app.core.database import Base


class Vegetable(Base):
    __tablename__ = "vegetables"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column("Name", String, nullable=False, unique=True)
    image_url = Column("Image", String, nullable=True)
    estimated_harvest_time = Column("Estimated Harvest Time", Interval, nullable=True)
    watering_frequency = Column("Watering Frequency", Interval, nullable=True)
    amount_of_sunlight = Column("Amount of Sunlight", String, nullable=True)
    planting_instructions = Column("Planting Instructions", Text, nullable=True)
    user_vegetable_progress = relationship(
        "UserVegetableProgress", back_populates="vegetable"
    )

    def __repr__(self):
        return f"<Vegetable(id={self.id}, name='{self.name}')>"
