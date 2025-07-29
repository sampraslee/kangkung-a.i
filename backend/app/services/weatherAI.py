import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_community.document_loaders.weather import WeatherDataLoader
from langchain_community.utilities import OpenWeatherMapAPIWrapper


class WeatherNotification(BaseModel):
    plant: str
    weekly_weather_summary: str


load_dotenv()

llm_weather = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash", api_key=os.getenv("GEMINI_API_KEY")
)


async def get_weekly_weather_notification(notification: WeatherNotification) -> str:
    """
    Generate a professional weekly weather notification for plant care based on the week's weather summary.

    Args:
        notification (WeatherNotification): Contains the plant name and a summary of the week's weather.

    Returns:
        str: A professional notification advising the user on plant care for the week.
    """
    system_prompt_text = """
    You are a professional gardening expert providing tailored care advice based on weekly weather patterns.

    Your expertise includes:
    * Analyzing Malaysian weekly weather patterns and their impact on plants

    When creating the notification:
    1. Use the plant name and weekly weather summary provided
    2. Provide specific, data-driven advice for plant care this week
    3. Maintain a friendly tone
    5. Be concise and use simple words
    4. Your advice should be easy for a novice gardener to understand
    """

    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt_text),
            (
                "human",
                "Plant: {plant}\nWeekly Weather Summary: {weekly_weather_summary}\nPlease provide a professional plant care notification based on the weather forecast.",
            ),
        ]
    )

    chain = prompt_template | llm_weather
    res = await chain.ainvoke(
        {
            "plant": notification.plant,
            "weekly_weather_summary": notification.weekly_weather_summary,
        }
    )
    return res.content


async def fetch_and_summarize_weather() -> str:
    """
    Fetches weekly weather data for Petaling Jaya, MY and summarizes it.

    Returns:
        str: A summarized string of the weekly weather forecast.
    """
    location = "Petaling Jaya, MY"  # Fixed location

    openweathermap_api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    if not openweathermap_api_key:
        raise ValueError("OPENWEATHERMAP_API_KEY not found in environment variables.")

    owm_client = OpenWeatherMapAPIWrapper(openweathermap_api_key=openweathermap_api_key)
    loader = WeatherDataLoader.from_params(
        places=[location], openweathermap_api_key=openweathermap_api_key
    )

    # Load documents (weather data)
    documents = await loader.aload()

    weekly_summary_parts = []
    for doc in documents:
        weekly_summary_parts.append(doc.page_content)

    full_weather_data = "\n".join(weekly_summary_parts)

    summary_prompt_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a helpful assistant. Summarize the following detailed weather data into a concise, easy-to-understand weekly weather summary. Focus on key elements like overall conditions, temperature trends, and significant weather events (e.g., rain, sunny, cloudy) relevant for general planning.",
            ),
            ("human", "Weather Data: {weather_data}"),
        ]
    )
    summary_chain = summary_prompt_template | llm_weather
    summarized_content = await summary_chain.ainvoke(
        {"weather_data": full_weather_data}
    )

    return summarized_content.content


# Example
async def main():
    # Fetch and summarize the weekly weather for Petaling Jaya
    weekly_weather_summary = await fetch_and_summarize_weather()
    print("Generated Weekly Weather Summary:\n", weekly_weather_summary)

    notification = WeatherNotification(
        plant="Kangkung", weekly_weather_summary=weekly_weather_summary
    )
    message = await get_weekly_weather_notification(notification)
    print("\nAI Generated Plant Notification:\n", message)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
