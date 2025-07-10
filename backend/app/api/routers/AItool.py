# app/api/routers/timelines.py
from fastapi import APIRouter, File, UploadFile, HTTPException, Form, Depends
from sqlalchemy.orm import Session
from app.api import deps
from app import crud
from typing import Dict, Optional
# Import the Pydantic model too
from app.services.timeline_service import generate_care_timeline, CareTimeline, convert_periods_to_dates
from app.services import chat_service
import uuid
from langchain_core.messages import HumanMessage, AIMessage

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


@router.post("/analyze-image-chat/{progress_id}", response_model=chat_service.AnalysisResponse)
async def analyze_image(progress_id: int, db: Session = Depends(deps.get_db), file: UploadFile = File(...)):
    """
    Receives an image for a specific plant progress, analyzes it, 
    and creates or continues a chat session for that plant.
    """
    # 1. Get the user's plant progress from the database
    progress = crud.crud_progress.get_progress_by_id(
        db, progress_id=progress_id)
    if not progress:
        raise HTTPException(status_code=404, detail="User progress not found")

    # 2. Check if a chat session already exists for this plant
    session_id = progress.chat_session_id
    is_new_chat = False
    if not session_id:
        is_new_chat = True
        # If not, create a new session ID and save it to the database
        session_id = str(uuid.uuid4())
        progress.chat_session_id = session_id
        db.commit()
        db.refresh(progress)

    # 3. Analyze the image
    contents = await file.read()
    analysis_result = await chat_service.analyze_plant_image(image_bytes=contents)

    # 4. If it's a new chat, "prime" the history
    if is_new_chat:
        history = chat_service.get_message_history(session_id)
        history.add_message(HumanMessage(
            content="Here is the picture of my plant, can you analyze it?"))
        history.add_message(AIMessage(content=analysis_result))

    return {"session_id": session_id, "analysis": analysis_result}


@router.post("/continue-chat", response_model=chat_service.ChatResponse)
async def continue_chat_session(request: chat_service.ChatRequest):
    """
    Continues an existing chat session using the session_id.
    """
    ai_response = await chat_service.continue_chat(
        session_id=request.session_id,
        user_input=request.user_input
    )
    return {"ai_response": ai_response}
