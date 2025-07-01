from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum


class MaterialType(str, enum.Enum):
    SOIL = "soil"
    FERTILISER = "fertiliser"
    PESTICIDE = "pesticide"
    TOOLS = "tools"


class Material(Base):
    __tablename__ = "materials"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    image = Column(String, nullable=True)
    type = Column(Enum(MaterialType), nullable=False)  # Use the Enum here
    vegetable_id = Column(Integer, ForeignKey("vegetables.id"), nullable=False)

    vegetable = relationship("Vegetable", back_populates="materials")
