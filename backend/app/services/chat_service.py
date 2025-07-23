# app/services/chat_service.py
import os
import base64
import uuid
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from pydantic import BaseModel
from typing import Optional


class ChatRequest(BaseModel):
    session_id: str
    user_input: str


class ChatResponse(BaseModel):
    ai_response: str


class AnalysisResponse(BaseModel):
    session_id: str
    analysis: str


class SummaryResponse(BaseModel):
    summary: str


load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash", temperature=0.3, api_key=GEMINI_API_KEY)


async def analyze_plant_image(image_bytes: bytes, vegetable_name: str, previous_notes: Optional[str]) -> str:
    # --- MODIFICATION 1: The function now requires the vegetable_name ---
    image_base64 = base64.b64encode(image_bytes).decode()

    # --- MODIFICATION 2: The prompt is completely rewritten for better control ---
    prompt_text = f"""
    You are analyzing an image of a **{vegetable_name}** plant. Please follow these steps:

    **1. The Plant:**
    * First, confirm if the plant in the image looks like a **{vegetable_name}**.
    * If it does not match, stop and politely tell the user what plant is in the image and that the image does not seem to be a {vegetable_name} and they should start a new check-up for the correct plant.
    * If it matches, proceed to the next steps.

    **1. Assess the vegetable's condition:** Determine if the vegetable is:
    * Fully grown
    * Growing and healthy
    * Sick

    **2. The characteristics observed:** Detail the key features you observe in the image, such as leaf color, stem strength, and any signs of disease or pests.

    **3. Specific advice based on the assessment:**
    * **If Fully Grown:** Advise on harvesting.
    * **If Growing and Healthy:** Reinforce good care practices.
    * **If Sick:** Identify the likely cause and suggest organic-first solutions.
    """

    if previous_notes:
        prompt_text = f"For context, here are notes from the last check-up:\n---\n{previous_notes}\n---\n\n{prompt_text}"

    analysis_prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a gardening expert and can provide tailored care advice. 
        You communicate like a Malaysian who speaks English and occasionally Malay. 
        Be clear, concise, use emoticons, and prioritize planting solutions and vegetable guidance.
        Anything that is not related you will say you do not know."""),
        ("human", [
            {"type": "text", "text": prompt_text},
            {"type": "image_url", "image_url": f"data:image/jpeg;base64,{image_base64}"}
        ]),
    ])

    vision_chain = analysis_prompt | llm
    response = await vision_chain.ainvoke({})
    return response.content


async def continue_chat(history: str, user_input: str, vegetable_name: str) -> str:
    chat_prompt = ChatPromptTemplate.from_messages([
        ("system", f"""You are a gardening expert providing tailored care advice for a plant.
         You communicate like a Malaysian who speaks English and occasionally Malay. 
         Be clear, concise, use emoticons, and prioritize planting solutions and guidance.
         If the user asks about anything not related to gardening"""),
        ("user", "Here is our conversation so far:\n---\n{history}\n---"),
        ("human", "My new question is: {input}"),
    ])

    chain = chat_prompt | llm
    response = await chain.ainvoke({"history": history, "input": user_input})
    return response.content


async def summarize_notes(notes: str) -> str:
    """
    Takes a long conversation history and returns a concise summary.
    """
    summarization_prompt = ChatPromptTemplate.from_messages([
        ("system",
         """You are a gardening expert and can make a concise and accurate summary of text.  
         Read the entire conversation log between a user and you. 
         Your task is to create a concise summary that includes:
         1. The type of plant.
         2. Key health issues identified over time (e.g., pests, deficiencies).
         3. Important treatments or advice given.
         4. The last known status of the plant.
         Keep the summary in a single block of text."""),
        ("human",
         "Please summarize these notes. The summary must only be related to the plant I am planting. :\n\n{notes_history}")
    ])

    chain = summarization_prompt | llm
    response = await chain.ainvoke({"notes_history": notes})

    return response.content
