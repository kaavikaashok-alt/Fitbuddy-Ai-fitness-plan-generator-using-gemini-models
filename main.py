import os
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai

load_dotenv()

app = FastAPI()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

class FitnessRequest(BaseModel):
    name: str
    age: int
    goal: str
    fitness_level: str
    days_per_week: int

@app.get("/")
def home():
    return {"message": "FitBuddy API is running"}

@app.post("/generate")
def generate_plan(request: FitnessRequest):

    prompt = f"""
    Create a safe and general fitness plan for:

    Name: {request.name}
    Age: {request.age}
    Goal: {request.goal}
    Fitness Level: {request.fitness_level}
    Days Per Week: {request.days_per_week}

    Include:
    1. Warm-up
    2. Exercise plan
    3. Rest and recovery
    4. Cool-down
    5. General safety tips

    Keep the plan suitable for the person's fitness level.
    Avoid extreme dieting, calorie restriction, or unsafe exercises.
    Mention that this is general fitness information and not medical advice.
    """

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    return {
        "name": request.name,
        "fitness_plan": response.text
    }