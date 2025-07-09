# my_project/app/services/image_analysis_service.py
import os
import base64
from typing import Dict, Optional
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)


def encode_image(image_content: bytes) -> str:
    """Encodes image content to base64 string."""
    return base64.b64encode(image_content).decode()


async def analyze_vegetable_image_and_advise(
    image_content: bytes,
    question: Optional[str] = None
) -> Dict[str, str]:
    """
    Analyzes image content of a vegetable plant and provides care advice.
    Optionally accepts a specific question from the user.
    """
    image_base64 = encode_image(image_content)

    human_content_parts = [
        {
            "type": "text",
            "text": """Analyze the image of the vegetable plant and provide comprehensive advice on its condition and how to care for it. Follow these steps:

            **Assess the types of plants:**
            * Provide their names

            **Assess the vegetable\'s condition:** Determine if the vegetable is:
            * (a) Fully grown
            * (b) Growing and healthy
            * (c) Sick

            **Describe the characteristics observed:** Detail the key features you observe in the image, such as:
            * Leaf color, shape, and any signs of disease or pests
            * Stem strength and appearance
            * Size and overall appearance of the vegetable itself (if present)
            * Presence of any abnormalities or damage

            **Provide specific advice based on the assessment:**

            * **If Fully Grown (a):** Advise on the best time and method for harvesting. Also, provide general tips for maintaining soil health after harvest.

            * **If Growing and Healthy (b):** Reinforce that the plant is in good condition. 

            * **If Sick (c):** Identify the likely cause of the sickness (e.g., specific disease, pest infestation, nutrient deficiency). Provide detailed advice on how to treat the problem, including specific remedies, organic or chemical treatments (if appropriate), and changes to watering or fertilization practices.

            **Provide recommendations for materials:** Based on your assessment and advice, suggest the necessary materials (e.g., fertilizer type and quantity, pesticide, fungicide, tools) and their approximate amounts needed for the vegetable to grow healthily or recover from illness. Be as specific as possible with product recommendations (if possible) and application instructions.

            About the instructions:
            **Be clear, concise, and provide actionable advice. Prioritize organic and natural solutions whenever possible. 
            **Make the sentence shorter. Keep it simple. 
            **You have to sound like a Malaysian auntie who speaks English, and Malay only when necessary.
            **Put emoticons to make it easier to read.
            """
        },
        {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{image_base64}",
                "detail": "high",
            },
        },
    ]

    if question:
        human_content_parts.append({
            "type": "text",
            "text": f"\n\nAdditionally, please specifically address the user's question: '{question}'"
        })

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a gardening expert capable of analyzing vegetable images and providing advice on how to care for vegetables. You will analyze the image, determine the vegetable\'s condition (fully grown, healthy and growing, or sick), and provide tailored care advice. Remember to also address the user's specific question if provided."),
        ("human", human_content_parts),
    ])

    chain = prompt | llm
    res = await chain.ainvoke({})
    return {"analysis": res.content}
