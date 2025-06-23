from sqlalchemy.orm import Session
from app import models, schemas


def get_vegetable(db: Session, vegetable_id: int):
    return db.query(models.Vegetable).filter(models.Vegetable.id == vegetable_id).first()


def get_vegetables(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Vegetable).offset(skip).limit(limit).all()


def create_vegetable(db: Session, vegetable: schemas.VegetableCreate):
    db_vegetable = models.Vegetable(**vegetable.model_dump())
    db.add(db_vegetable)
    db.commit()
    db.refresh(db_vegetable)
    return db_vegetable
