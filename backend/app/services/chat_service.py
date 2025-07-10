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


class ChatRequest(BaseModel):
    session_id: str
    user_input: str


class ChatResponse(BaseModel):
    ai_response: str


class AnalysisResponse(BaseModel):
    session_id: str
    analysis: str


load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash", temperature=0.3, api_key=GEMINI_API_KEY)

# --- DISCLAIMER ---
# This global 'store' is simple for a demo but is NOT production-ready.
# In a real app, use a database, Redis, or another persistent cache for chat history.
store = {}


def get_message_history(session_id: str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


chat_prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a gardening expert and can provide tailored care advice. 
        You communicate like a Malaysian who speaks English and occasionally Malay. 
        Be clear, concise, use emoticons, and prioritize planting solutions and vegetable guidance.
        Anything that is not related you will say you do not know."""),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}"),
])
chain_with_history = RunnableWithMessageHistory(
    chat_prompt | llm,
    get_message_history,
    input_messages_key="input",
    history_messages_key="history"
)


async def analyze_plant_image(image_bytes: bytes) -> str:
    image_base64 = base64.b64encode(image_bytes).decode()

    analysis_prompt = ChatPromptTemplate.from_messages([
        ("system",
         """You are a gardening expert capable of analyzing vegetable images and providing advice on how to care for vegetables. 
        You will analyze the image, determine the vegetable\'s condition 
        (fully grown, healthy and growing, or sick), and provide tailored care advice. 
        You communicate like a Malaysian who speaks English and occasionally Malay. 
        Be clear, concise, use emoticons, and prioritize organic solutions. Anything that is not related you will say you do not know."""),
        ("human", [
            {"type": "text", "text": """Analyze the image of the vegetable plant, 
                and provide comprehensive advice on its condition and how to care for it. Follow these steps:

                **Assess the types of plants:**
                * Provide their names

                **Assess the vegetable\'s condition:** Determine if the vegetable is:
                * Fully grown
                * Growing and healthy
                * Sick

                **Describe the characteristics observed:** Detail the key features you observe in the image, such as:
                * Leaf color, shape, and any signs of disease or pests
                * Stem strength and appearance
                * Size and overall appearance of the vegetable itself (if present)
                * Presence of any abnormalities or damage

                **Provide specific advice based on the assessment:**

                * **If Fully Grown :** Advise on the best time and method for harvesting. 
                Also, provide general tips for maintaining soil health after harvest.

                * **If Growing and Healthy :** Reinforce that the plant is in good condition. 

                * **If Sick :** Identify the likely cause of the sickness (e.g., specific disease, pest infestation, nutrient deficiency). 
                Provide detailed advice on how to treat the problem, including specific remedies, 
                organic or chemical treatments (if appropriate), and changes to watering or fertilization practices.
                """},
            {"type": "image_url", "image_url": f"data:image/jpeg;base64,{image_base64}"}
        ]),
    ])

    vision_chain = analysis_prompt | llm
    response = await vision_chain.ainvoke({})
    return response.content


async def continue_chat(session_id: str, user_input: str) -> str:
    response = await chain_with_history.ainvoke(
        {"input": user_input},
        {"configurable": {"session_id": session_id}}
    )
    return response.content
