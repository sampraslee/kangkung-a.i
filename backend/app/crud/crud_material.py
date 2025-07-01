# app/crud/crud_material.py
from sqlalchemy.orm import Session, joinedload
from fastapi import APIRouter, Depends, HTTPException, status
from app import models, schemas
from typing import List, Optional
from sqlalchemy.exc import IntegrityError


def _get_vegetables_by_ids(db: Session, vegetable_ids: List[int]) -> List[models.Vegetable]:
    """
    Helper function to fetch Vegetable ORM objects by their IDs.
    Used for associating materials with vegetables.
    """
    if not vegetable_ids:
        return []
    return db.query(models.Vegetable).filter(models.Vegetable.id.in_(vegetable_ids)).all()


def get_material(db: Session, material_id: int) -> Optional[models.Material]:
    """
    Retrieves a single material by its ID, eagerly loading its associated vegetables.
    """
    return db.query(models.Material).options(joinedload(models.Material.vegetables)).filter(models.Material.id == material_id).first()


def get_materials(db: Session, skip: int = 0, limit: int = 100) -> List[models.Material]:
    """
    Retrieves a list of all materials, eagerly loading their associated vegetables.
    """
    return db.query(models.Material).options(joinedload(models.Material.vegetables)).offset(skip).limit(limit).all()


def get_materials_by_vegetable(db: Session, vegetable_id: int) -> List[models.Material]:
    """
    Retrieves all materials associated with a specific vegetable.
    This now queries through the many-to-many relationship by starting from Vegetable.
    """
    vegetable = db.query(models.Vegetable).options(joinedload(
        models.Vegetable.materials)).filter(models.Vegetable.id == vegetable_id).first()
    if vegetable:
        return vegetable.materials
    return []


def get_material_by_name(db: Session, name: str):
    return db.query(models.Material).filter(models.Material.name == name).first()


def create_material(db: Session, material: schemas.MaterialCreate):
    print(f"CRUD: create_material called with data: {material.dict()}")

    try:
        db_material = models.Material(
            name=material.name,
            type=material.type,
            image=material.image
        )
        db.add(db_material)
        db.flush()
        if material.vegetable_ids:
            for veg_id in material.vegetable_ids:
                db_vegetable = db.query(models.Vegetable).get(veg_id)
                if db_vegetable is None:
                    print(f"CRUD: Vegetable with ID {veg_id} not found.")
                    raise ValueError(f"Vegetable with ID {veg_id} not found.")

                db_material.vegetables.append(db_vegetable)

        db.commit()
        db.refresh(db_material)
        return db_material
    except IntegrityError as e:
        db.rollback()
        print(f"CRUD: Database IntegrityError during material creation: {e}")
        raise
    except ValueError as e:
        db.rollback()
        print(f"CRUD: ValueError during material creation: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        db.rollback()
        print(f"CRUD: Generic Exception during material creation: {e}")
        raise


def update_material(
    db: Session,
    db_material: models.Material,
    material_in: schemas.MaterialUpdate
) -> models.Material:
    """
    Updates an existing material entry in the database.
    Handles updating basic fields and many-to-many associations.
    """
    update_data = material_in.model_dump(
        exclude_unset=True, exclude={"vegetable_ids"})

    for key, value in update_data.items():
        setattr(db_material, key, value)

    if material_in.vegetable_ids is not None:
        db_material.vegetables.clear()
        if material_in.vegetable_ids:
            vegetables_to_associate = _get_vegetables_by_ids(
                db, material_in.vegetable_ids)
            db_material.vegetables.extend(vegetables_to_associate)
    db.add(db_material)
    db.commit()
    db.refresh(db_material)

    return db_material


def delete_material(db: Session, material_id: int) -> Optional[models.Material]:
    """
    Deletes a material from the database.
    Note: Deleting a material will automatically delete its entries in the
    material_vegetable_association table due to cascade settings on the ORM relationship.
    It will NOT delete associated Vegetable objects.
    """
    db_material = db.query(models.Material).filter(
        models.Material.id == material_id).first()
    if db_material:
        db.delete(db_material)
        db.commit()
    return db_material
