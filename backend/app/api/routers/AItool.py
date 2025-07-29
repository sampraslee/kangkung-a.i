from fastapi import APIRouter, File, UploadFile, HTTPException, Form, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.api import deps
from app import crud
from app.services.timeline_service import (
    generate_care_timeline,
    CareTimeline,
    convert_periods_to_dates,
)
from app.services.vegetable_filter import filter_vegetable_by_criteria
from app.services import chat_service
from datetime import datetime
from app.services import weatherAI

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


@router.post(
    "/analyze-image-chat/{progress_id}", response_model=chat_service.AnalysisResponse
)
async def analyze_image_and_save(
    progress_id: int, db: Session = Depends(deps.get_db), file: UploadFile = File(...)
):
    """
    Analyzes a plant image for a specific progress entry,
    and saves the new analysis to the database.
    """
    progress = crud.crud_progress.get_progress_by_id(db, progress_id=progress_id)
    if not progress:
        raise HTTPException(status_code=404, detail="User progress not found")

    contents = await file.read()
    previous_notes = progress.checkUpNotes

    vegetable_name = progress.vegetable.name

    analysis_result = await chat_service.analyze_plant_image(
        image_bytes=contents,
        vegetable_name=vegetable_name,
        previous_notes=previous_notes,
    )

    today_date = datetime.now().strftime("%Y-%m-%d %H:%M")
    new_log_entry = (
        f"\n\n--- Check-up on {today_date} ---\n\n"
        f"[USER]: (Uploaded an image for analysis of {vegetable_name})\n\n"
        f"[AI]:\n{analysis_result}"
    )

    if progress.checkUpNotes:
        progress.checkUpNotes += new_log_entry
    else:
        progress.checkUpNotes = new_log_entry.strip()

    db.commit()

    return {"session_id": str(progress_id), "analysis": analysis_result}


@router.post("/continue-chat/{progress_id}", response_model=chat_service.ChatResponse)
async def continue_chat_session_and_save(
    progress_id: int,
    request: chat_service.ChatRequest,
    db: Session = Depends(deps.get_db),
):
    """
    Continues a chat based on the full history from checkUpNotes
    and saves the new turn to the database.
    """
    progress = crud.crud_progress.get_progress_by_id(db, progress_id=progress_id)
    if not progress or not progress.checkUpNotes:
        raise HTTPException(
            status_code=404, detail="No chat history found for this plant."
        )

    vegetable_name = progress.vegetable.name
    ai_response = await chat_service.continue_chat(
        history=progress.checkUpNotes,
        user_input=request.user_input,
        vegetable_name=vegetable_name,
    )
    new_log_entry = f"\n\n[USER]: {request.user_input}\n\n" f"[AI]:\n{ai_response}"

    progress.checkUpNotes += new_log_entry
    db.commit()

    return {"ai_response": ai_response}


@router.post(
    "/summarize-chat/{progress_id}", response_model=chat_service.SummaryResponse
)
async def summarize_chat_history(progress_id: int, db: Session = Depends(deps.get_db)):
    """
    Summarizes the entire chat history for a plant and replaces the
    checkUpNotes with the summary.
    """
    progress = crud.crud_progress.get_progress_by_id(db, progress_id=progress_id)
    if not progress or not progress.checkUpNotes:
        raise HTTPException(status_code=404, detail="No notes found to summarize.")

    # 1. Call the summarization service with the current notes
    summary = await chat_service.summarize_notes(notes=progress.checkUpNotes)

    # 2. Replace the old notes with the new summary in the database
    progress.checkUpNotes = summary
    db.commit()

    return {"summary": summary}


@router.get("/weather-notification", summary="Get weekly weather notification")
async def get_weather_notification(plant: str = "Kangkung"):
    """
    Generates a weekly weather-based plant care notification.

    Query Parameters:
    - plant: Name of the plant (default: Kangkung)

    Returns:
    - A friendly plant care notification string
    """
    weekly_weather_summary = await weatherAI.fetch_and_summarize_weather()
    notification = weatherAI.WeatherNotification(
        plant=plant, weekly_weather_summary=weekly_weather_summary
    )
    message = await weatherAI.get_weekly_weather_notification(notification)

    return {"notification": message}
