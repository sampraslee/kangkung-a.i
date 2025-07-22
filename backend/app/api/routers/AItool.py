from fastapi import APIRouter, File, UploadFile, HTTPException, Form, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.api import deps
from app import crud
from typing import Dict, Optional
from app.services.timeline_service import (
    generate_care_timeline,
    CareTimeline,
    convert_periods_to_dates,
)
from app.services.image_analysis_service import analyze_vegetable_image_and_advise
from app.services.vegetable_filter import filter_vegetable_by_criteria


router = APIRouter()


class UserCriteria(BaseModel):
    criteria: str


@router.post("/filter-vegetables")
def filter_vegetables(userCriteria: UserCriteria, db: Session = Depends(deps.get_db)):
    print("working?")
    vegetable_list = crud.crud_vegetable.get_vegetables(db=db)
    print(vegetable_list)

    if not vegetable_list:
        raise HTTPException(status_code=404, detail="No vegetables found in database")
    print(userCriteria.criteria)
    filtered_vegetables = filter_vegetable_by_criteria(
        userCriteria.criteria, vegetable_list
    )
    return filtered_vegetables


@router.get("/generate-live/{vegetable_id}", response_model=CareTimeline)
def generate_live_timeline(vegetable_id: int, db: Session = Depends(deps.get_db)):
    """
    Generates a care timeline for a given vegetable LIVE from the AI.
    Does NOT save the result to the database.
    """
    # 1. Get the vegetable and its materials from the DB
    vegetable = crud.crud_vegetable.get_vegetable(db, vegetable_id=vegetable_id)
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
    progress = crud.crud_progress.get_progress_by_id(db, progress_id=progress_id)
    if not progress or not progress.startDate or not progress.expectedHarvestDate:
        raise HTTPException(
            status_code=404,
            detail="Progress entry with start and harvest dates not found.",
        )

    # 2. Get the vegetable and its materials to generate the periods
    vegetable = progress.vegetable
    material_names = [material.name for material in vegetable.materials]
    ai_periods = generate_care_timeline(vegetable.name, material_names)

    # 3. Use the new function to convert periods to dates
    timeline_events = convert_periods_to_dates(
        periods=ai_periods,
        start_date=progress.startDate.date(),  # Use .date() to be safe
        harvest_date=progress.expectedHarvestDate,
    )

    return timeline_events


# This means the full path will be /image-analysis/
@router.post("/image_analysis")
async def analyze_image_endpoint(
    file: UploadFile = File(...), question: Optional[str] = Form(None)
) -> str:
    """
    Analyzes an uploaded image of a vegetable plant and provides care advice.
    Optionally accepts a specific question from the user.
    """
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(
            400, detail="Invalid file type. Only JPEG and PNG are allowed."
        )

    if file.size is not None and file.size > 10_000_000:
        raise HTTPException(400, detail="File too large. Maximum size is 10MB.")

    try:
        contents = await file.read()
        analysis_result = await analyze_vegetable_image_and_advise(
            image_content=contents, question=question
        )
        return analysis_result["analysis"]
    except Exception as e:
        raise HTTPException(
            500, detail=f"An error occurred while processing the image: {str(e)}"
        )
