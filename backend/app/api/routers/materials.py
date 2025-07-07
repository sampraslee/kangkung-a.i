# app/api/routers/materials.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional

# Ensure 'crud' refers to your crud folder
from app import schemas, crud, models
from app.api import deps  # Assuming deps.get_db is defined here
from sqlalchemy.exc import IntegrityError

router = APIRouter(tags=["Materials"])  # Tag for OpenAPI documentation


@router.get("/", response_model=List[schemas.Material])
def read_all_materials(
    skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)
):
    """
    Retrieve a list of all materials.
    """
    materials = crud.crud_material.get_materials(db, skip=skip, limit=limit)
    return materials


@router.get("/{material_id}", response_model=schemas.Material)
def read_material(material_id: int, db: Session = Depends(deps.get_db)):
    """
    Retrieve a single material by its ID.
    """
    db_material = crud.crud_material.get_material(db, material_id=material_id)
    if not db_material:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Material not found"
        )
    return db_material


@router.get("/by-vegetable/{vegetable_id}", response_model=List[schemas.Material])
def read_materials_by_vegetable(vegetable_id: int, db: Session = Depends(deps.get_db)):
    """
    Get all materials for a specific vegetable.
    """
    # Optional: Check if the vegetable exists first
    db_vegetable = crud.crud_vegetable.get_vegetable(db, vegetable_id=vegetable_id)
    if not db_vegetable:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Vegetable with ID {vegetable_id} not found.",
        )

    materials = crud.crud_material.get_materials_by_vegetable(
        db, vegetable_id=vegetable_id
    )
    return materials


@router.patch("/{material_id}", response_model=schemas.Material)
def update_material(
    material_id: int,
    material_in: schemas.MaterialUpdate,  # Using the new MaterialUpdate schema
    db: Session = Depends(deps.get_db),
):
    """
    Update an existing material by ID.
    Allows partial updates and modification of associated vegetables.
    """
    db_material = crud.crud_material.get_material(db, material_id=material_id)
    if not db_material:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Material not found"
        )

    # Validate if all provided vegetable_ids for update exist
    if (
        material_in.vegetable_ids is not None
    ):  # Check if the field was sent in the request
        for veg_id in material_in.vegetable_ids:
            db_vegetable = crud.crud_vegetable.get_vegetable(db, vegetable_id=veg_id)
            if not db_vegetable:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Vegetable with ID {veg_id} not found.",
                )
    try:
        updated_material = crud.crud_material.update_material(
            db=db, db_material=db_material, material_in=material_in
        )
        return updated_material
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Could not update material. Check data integrity (e.g., duplicate name).",
        )


@router.delete("/{material_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_material(material_id: int, db: Session = Depends(deps.get_db)):
    """
    Delete a material by its ID.
    """
    db_material = crud.crud_material.get_material(db, material_id=material_id)
    if not db_material:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Material not found"
        )
    crud.crud_material.delete_material(db, material_id=material_id)
    # FastAPI returns 204 with no content
    return {"message": "Material deleted successfully"}
