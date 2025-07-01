# app/crud/crud_material.py
from sqlalchemy.orm import Session
from app import models, schemas


def get_materials_by_vegetable(db: Session, vegetable_id: int):
    """
    Retrieves all materials for a specific vegetable.
    """
    return db.query(models.Material).filter(models.Material.vegetable_id == vegetable_id).all()


def create_material(db: Session, material: schemas.MaterialCreate):
    """
    Creates a new material entry in the database.
    """
    # Create a new Material database model from the Pydantic schema
    db_material = models.Material(**material.model_dump())

    db.add(db_material)
    db.commit()
    db.refresh(db_material)

    return db_material
