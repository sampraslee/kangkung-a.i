# app/api/routers/materials.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
# Ensure 'crud' refers to your crud folder
from app import schemas, crud, models
from app.api import deps  # Assuming deps.get_db is defined here
from sqlalchemy.exc import IntegrityError

router = APIRouter(
    prefix="/materials",  # Add a prefix for all routes in this router
    tags=["Materials"]  # Tag for OpenAPI documentation
)


@router.post("/", response_model=schemas.Material, status_code=status.HTTP_201_CREATED)
def create_material(material: schemas.MaterialCreate, db: Session = Depends(deps.get_db)):
    # Add logging before trying to create
    print(
        f"Attempting to create material with name: {material.name}, type: {material.type}, vegetable_ids: {material.vegetable_ids}")

    try:
        db_material = crud.get_material_by_name(db, name=material.name)
        if db_material:
            # Log this specific condition
            print(f"Material with name '{material.name}' already exists.")
            raise HTTPException(
                status_code=400, detail="Material with this name already exists or invalid data.")

        # This is where the actual creation logic lives
        created_material = crud.create_material(db=db, material=material)
        return created_material
    except Exception as e:
        # Catch general exceptions here to see more detail if it's not the name conflict
        print(f"Error creating material: {e}")
        db.rollback()  # Rollback the transaction on error
        # Raise a 500 for unhandled errors
        raise HTTPException(
            status_code=500, detail=f"Internal server error: {e}")


@router.get("/", response_model=List[schemas.Material])
def read_all_materials(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(deps.get_db)
):
    """
    Retrieve a list of all materials.
    """
    materials = crud.crud_material.get_materials(db, skip=skip, limit=limit)
    return materials


@router.get("/{material_id}", response_model=schemas.Material)
def read_material(
    material_id: int,
    db: Session = Depends(deps.get_db)
):
    """
    Retrieve a single material by its ID.
    """
    db_material = crud.crud_material.get_material(db, material_id=material_id)
    if not db_material:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Material not found"
        )
    return db_material


@router.get("/by-vegetable/{vegetable_id}", response_model=List[schemas.Material])
def read_materials_by_vegetable(
    vegetable_id: int,
    db: Session = Depends(deps.get_db)
):
    """
    Get all materials for a specific vegetable.
    """
    # Optional: Check if the vegetable exists first
    db_vegetable = crud.crud_vegetable.get_vegetable(
        db, vegetable_id=vegetable_id)
    if not db_vegetable:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Vegetable with ID {vegetable_id} not found."
        )

    materials = crud.crud_material.get_materials_by_vegetable(
        db, vegetable_id=vegetable_id)
    return materials


@router.patch("/{material_id}", response_model=schemas.Material)
def update_material(
    material_id: int,
    material_in: schemas.MaterialUpdate,  # Using the new MaterialUpdate schema
    db: Session = Depends(deps.get_db)
):
    """
    Update an existing material by ID.
    Allows partial updates and modification of associated vegetables.
    """
    db_material = crud.crud_material.get_material(db, material_id=material_id)
    if not db_material:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Material not found"
        )

    # Validate if all provided vegetable_ids for update exist
    if material_in.vegetable_ids is not None:  # Check if the field was sent in the request
        for veg_id in material_in.vegetable_ids:
            db_vegetable = crud.crud_vegetable.get_vegetable(
                db, vegetable_id=veg_id)
            if not db_vegetable:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Vegetable with ID {veg_id} not found."
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
            detail="Could not update material. Check data integrity (e.g., duplicate name)."
        )


@router.delete("/{material_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_material(
    material_id: int,
    db: Session = Depends(deps.get_db)
):
    """
    Delete a material by its ID.
    """
    db_material = crud.crud_material.get_material(db, material_id=material_id)
    if not db_material:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Material not found"
        )
    crud.crud_material.delete_material(db, material_id=material_id)
    # FastAPI returns 204 with no content
    return {"message": "Material deleted successfully"}
