import os
from typing import List
from app import schemas
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

GEMINI = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash", api_key=os.getenv("GEMINI_API_KEY")
)


class FilteredVegetable(BaseModel):
    id: int = Field(description="The id of the vegetable.")
    name: str = Field(description="The name of the vegetable.")


class FilteredVegetableList(BaseModel):
    vegetables: List[FilteredVegetable] = Field(
        description="A list of vegetables that fulfill the users criteria."
    )


def filter_vegetable_by_criteria(
    user_criteria: str, vegetables: List[schemas.Vegetable]
) -> List[FilteredVegetable]:
    vegetable_list = ""

    for vegetable in vegetables:
        vegetable_list += f"ID: {vegetable.id}, Name:{vegetable.name}, Amount of Sunlight: {vegetable.amount_of_sunlight}, Watering frequency: {vegetable.watering_frequency},Estimated Harvest Time: {vegetable.estimated_harvest_time}\n"

    print(vegetable_list)

    parser = JsonOutputParser(pydantic_object=FilteredVegetableList)

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You are an expert vegetable garden assistant.
                A user will give you a requirement and a list of available vegetables.
                Your job is to analyze the user's requirement and return a list of vegetables that are a good fit.
                Base your answer *only* on the provided list of vegetables.
                If no vegetables in the list are a good fit, return an empty list.

                {format_instructions}""",
            ),
            (
                "human",
                """User requirement: "{criteria}"

                Available vegetables:
                {vegetable_list}""",
            ),
        ]
    )

    chain = prompt | GEMINI | parser
    response = chain.invoke(
        {
            "criteria": user_criteria,
            "vegetable_list": vegetable_list,
            "format_instructions": parser.get_format_instructions(),
        }
    )

    print(response)

    return response.get("vegetables", [])
