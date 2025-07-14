# app/models/material.py

from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum

material_vegetable_association = Table(
    "material_vegetable_association",
    Base.metadata,
    Column("material_id", Integer, ForeignKey(
        "materials.id"), primary_key=True),
    Column("vegetable_id", Integer, ForeignKey(
        "vegetables.id"), primary_key=True)
)


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
    type = Column(Enum(MaterialType), nullable=False)
    description = Column (String, nullable=True)

    vegetables = relationship(
        "Vegetable",
        secondary=material_vegetable_association,
        back_populates="materials"
    )
