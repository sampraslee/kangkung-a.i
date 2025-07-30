# app/services/timeline_service.py
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
import re
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from typing import List, Dict, Any

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash", temperature=0.0, api_key=GEMINI_API_KEY
)


class CareTimeline(BaseModel):
    soil_period: str = Field(
        description="Recommended period for checking or changing soil. e.g., 'Every 6 months' or 'Not usually needed'."
    )
    fertilize_period: str = Field(
        description="Recommended frequency for adding fertilizer. e.g., 'Every 2 weeks'."
    )
    pesticide_period: str = Field(
        description="Recommended frequency for using pesticide. e.g., 'Only when pests are visible'."
    )
    pot_period: str = Field(
        description="Recommended time to check if a larger pot is needed. e.g., 'When roots fill the pot'."
    )


def generate_care_timeline(vegetable_name: str, material_names: List[str]) -> dict:
    """
    Generates a care timeline for a vegetable using its specific materials.
    """
    output_parser = JsonOutputParser(pydantic_object=CareTimeline)

    chat_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You are an expert gardener providing a brief, practical care schedule. 
         Based on the user's chosen vegetable and materials, create a simple timeline for checkups.
         Each period should be a short phrase (less than 5 words).
         Your response must follow the requested JSON format.""",
            ),
            (
                "human",
                "Here is the user's plant information:\n"
                "- Vegetable: {vegetable}\n"
                "- Materials they have: {materials}\n\n"
                "Generate the care timeline for this setup.\n"
                "{format_instructions}",
            ),
        ]
    )

    chain = chat_prompt | llm | output_parser

    print(f"AI Service: Generating timeline for {vegetable_name}...")
    response = chain.invoke(
        {
            "vegetable": vegetable_name,
            "materials": ", ".join(material_names),
            "format_instructions": output_parser.get_format_instructions(),
        }
    )

    return response


def _parse_period_to_duration(period_string: str) -> relativedelta | None:
    """
    Helper function to parse strings like 'Every 2 weeks' into a duration.
    This version is more robust to handle natural language.
    """
    if (
        not period_string
        or "not" in period_string.lower()
        or "as needed" in period_string.lower()
    ):
        return None

    period_string = period_string.lower()

    # Handle common phrases first
    if "weekly" in period_string:
        return relativedelta(weeks=1)
    if "two weeks" in period_string or "bi-weekly" in period_string:
        return relativedelta(weeks=2)
    if "month" in period_string:
        return relativedelta(months=1)

    match = re.search(r"(\d+)\s+(day|days|week|weeks|month|months)", period_string)
    # ---------------------

    if match:
        num = int(match.group(1))
        unit = match.group(2)

        if "week" in unit:
            return relativedelta(weeks=num)
        if "day" in unit:
            return relativedelta(days=num)
        if "month" in unit:
            return relativedelta(months=num)

    word_to_num = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
    }
    # New regex for words like "three"
    match_word = re.search(
        r"(one|two|three|four|five|six|seven|eight|nine|ten)\s+(day|days|week|weeks|month|months)",
        period_string,
    )
    if match_word:
        num_word = word_to_num.get(match_word.group(1))
        unit_word = match_word.group(2)
        if num_word is not None:
            if "week" in unit_word:
                return relativedelta(weeks=num_word)
            if "day" in unit_word:
                return relativedelta(days=num_word)
            if "month" in unit_word:
                return relativedelta(months=num_word)

    # Return None if no pattern is matched
    return None


def convert_periods_to_dates(
    periods: Dict[str, Any], start_date: date, harvest_date: date
) -> List[Dict[str, str]]:
    """
    Converts AI-generated periods into a list of specific dates for a timeline.
    """
    events = []

    # A mapping from the period key to a user-friendly event name
    event_name_map = {
        "soil_period": "Check Soil",
        "fertilize_period": "Fertilize",
        "pesticide_period": "Check for Pests",
        "pot_period": "Check Pot Size",
    }

    for period_key, event_name in event_name_map.items():
        period_str = periods.get(period_key, "")
        duration = _parse_period_to_duration(period_str)

        if not duration:
            continue

        current_date = start_date
        while current_date <= harvest_date:

            # Format the date as: "Day Month Date Year"
            formatted_date = datetime.strftime(current_date, "%a %b %d %Y")
            # Add the event for the current date
            events.append({"event": event_name, "date": formatted_date})
            # Increment to the next event date
            current_date += duration
        # Sort all events by date to create a clean timeline
    sorted_events = sorted(
        events, key=lambda e: datetime.strptime(e["date"], "%a %b %d %Y")
    )
    return sorted_events
