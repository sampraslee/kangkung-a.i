from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.api import deps
from app import schemas, crud

router = APIRouter()

# == Vegetable Endpoints ==


@router.get("/vegetables/", response_model=List[schemas.Vegetable])
def read_vegetables(
    skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)
):
    return crud.crud_vegetable.get_vegetables(db, skip=skip, limit=limit)


@router.get("/vegetables/{vegetable_id}", response_model=schemas.Vegetable)
def read_vegetable(vegetable_id: int, db: Session = Depends(deps.get_db)):
    db_vegetable = crud.crud_vegetable.get_vegetable(db, vegetable_id=vegetable_id)
    if db_vegetable is None:
        raise HTTPException(status_code=404, detail="Vegetable not found")
    return db_vegetable


# == User Vegetable Progress Endpoints ==


@router.post("/progress/", response_model=schemas.Progress)
def create_user_progress(
    progress: schemas.ProgressCreate, db: Session = Depends(deps.get_db)
):
    return crud.crud_progress.create_user_vegetable_progress(db=db, progress=progress)


@router.get("/progress/{user_id}", response_model=List[schemas.Progress])
def read_user_progress(user_id: int, db: Session = Depends(deps.get_db)):
    return crud.crud_progress.get_user_progress_entries(db=db, user_id=user_id)


@router.patch("/progress/{progress_id}", response_model=schemas.Progress)
def update_user_progress(
    progress_id: int,
    progress_update: schemas.ProgressUpdate,
    db: Session = Depends(deps.get_db),
):
    db_progress = crud.crud_progress.get_progress_by_id(db, progress_id=progress_id)
    if not db_progress:
        raise HTTPException(status_code=404, detail="Progress entry not found")
    return crud.crud_progress.update_progress(
        db=db, db_obj=db_progress, obj_in=progress_update
    )


@router.delete("/progress/{progress_id}", status_code=200)
def delete_user_progress(progress_id: int, db: Session = Depends(deps.get_db)):
    """
    Deletes a user's vegetable progress entry.
    """
    deleted_progress = crud.crud_progress.delete_progress(
        db=db, progress_id=progress_id
    )

    if deleted_progress is None:
        raise HTTPException(
            status_code=404,
            detail=f"Progress entry with id {progress_id} not found",
        )

    return {
        "message": "Progress entry deleted successfully",
        "deleted_id": deleted_progress.id,
    }
