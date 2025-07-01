# app/api/routers/materials.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas, crud, models
from app.api import deps

router = APIRouter()


@router.post("/", response_model=schemas.Material)
def create_material(
    material: schemas.MaterialCreate,
    db: Session = Depends(deps.get_db)
):
    """
    Create a new material associated with a vegetable.
    """
    # Optional: Check if the vegetable exists first
    db_vegetable = crud.crud_vegetable.get_vegetable(
        db, vegetable_id=material.vegetable_id)
    if not db_vegetable:
        raise HTTPException(
            status_code=404,
            detail=f"Vegetable with id {material.vegetable_id} not found"
        )

    return crud.crud_material.create_material(db=db, material=material)


@router.get("/by-vegetable/{vegetable_id}", response_model=List[schemas.Material])
def read_materials_by_vegetable(
    vegetable_id: int,
    db: Session = Depends(deps.get_db)
):
    """
    Get all materials for a specific vegetable.
    """
    materials = crud.crud_material.get_materials_by_vegetable(
        db, vegetable_id=vegetable_id)
    return materials
