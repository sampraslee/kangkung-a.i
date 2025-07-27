from sqlalchemy.orm import Session
from app import models, schemas
from datetime import datetime, date
from typing import Optional, Union, Dict, Any


def get_progress_by_id(db: Session, progress_id: int):
    return db.query(models.UserVegetableProgress).filter(models.UserVegetableProgress.id == progress_id).first()


def get_user_progress_entries(db: Session, user_id: int):
    return db.query(models.UserVegetableProgress).filter(models.UserVegetableProgress.user_id == user_id).all()


def create_user_vegetable_progress(db: Session, progress: schemas.ProgressCreate):
    vegetable = db.query(models.Vegetable).filter(
        models.Vegetable.id == progress.vegetable_id).first()
    if not vegetable:
        return None

    calculated_harvest_date: Optional[date] = None
    if vegetable.estimated_harvest_time:
        calculated_harvest_date = datetime.utcnow(
        ).date() + vegetable.estimated_harvest_time
    if progress.vegeNickname is None:
        progress.vegeNickname = vegetable.name

    db_progress = models.UserVegetableProgress(
        **progress.model_dump(),
        expectedHarvestDate=calculated_harvest_date
    )
    db.add(db_progress)
    db.commit()
    db.refresh(db_progress)
    return db_progress


# In app/crud/crud_progress.py
from sqlalchemy.orm import Session
from app import models, schemas
from typing import Union, Dict, Any

# ... (your other crud functions like get_progress_by_id) ...

def update_progress(
    db: Session,
    db_obj: models.UserVegetableProgress,
    obj_in: Union[schemas.ProgressUpdate, Dict[str, Any]]
) -> models.UserVegetableProgress:
    """
    Updates a user progress entry with only the provided fields.
    """
    update_data = obj_in.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_obj, field, value)

    db.add(db_obj) 
    db.commit()  
    db.refresh(db_obj) 

    return db_obj


def delete_progress(db: Session, progress_id: int):
    """
    Deletes a UserVegetableProgress entry by its ID.
    """
    # First, get the object by its ID
    db_obj = get_progress_by_id(db, progress_id=progress_id)

    if not db_obj:
        return None  # Return None if the object doesn't exist

    # If it exists, delete it and commit
    db.delete(db_obj)
    db.commit()

    return db_obj  # Return the deleted object to confirm what was removed
