# app/api/routers/timelines.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app import crud
# Import the Pydantic model too
from app.services.timeline_service import generate_care_timeline, CareTimeline, convert_periods_to_dates

router = APIRouter()


@router.get("/generate-live/{vegetable_id}", response_model=CareTimeline)
def generate_live_timeline(vegetable_id: int, db: Session = Depends(deps.get_db)):
    """
    Generates a care timeline for a given vegetable LIVE from the AI.
    Does NOT save the result to the database.
    """
    # 1. Get the vegetable and its materials from the DB
    vegetable = crud.crud_vegetable.get_vegetable(
        db, vegetable_id=vegetable_id)
    if not vegetable:
        raise HTTPException(status_code=404, detail="Vegetable not found")

    vegetable_name = vegetable.name
    # The many-to-many relationship makes getting material names easy
    material_names = [material.name for material in vegetable.materials]

    # 2. Call the AI service with the fetched data
    timeline_data = generate_care_timeline(vegetable_name, material_names)

    # 3. Return the AI's response directly
    return timeline_data


@router.get("/calculate-dates/{progress_id}")
def get_timeline_dates(progress_id: int, db: Session = Depends(deps.get_db)):
    """
    Generates and calculates a full event timeline with specific dates
    for a user's plant progress.
    """
    # 1. Get the user's plant progress from the DB
    progress = crud.crud_progress.get_progress_by_id(
        db, progress_id=progress_id)
    if not progress or not progress.startDate or not progress.expectedHarvestDate:
        raise HTTPException(
            status_code=404,
            detail="Progress entry with start and harvest dates not found."
        )

    # 2. Get the vegetable and its materials to generate the periods
    vegetable = progress.vegetable
    material_names = [material.name for material in vegetable.materials]
    ai_periods = generate_care_timeline(vegetable.name, material_names)

    # 3. Use the new function to convert periods to dates
    timeline_events = convert_periods_to_dates(
        periods=ai_periods,
        start_date=progress.startDate.date(),  # Use .date() to be safe
        harvest_date=progress.expectedHarvestDate
    )

    return timeline_events
