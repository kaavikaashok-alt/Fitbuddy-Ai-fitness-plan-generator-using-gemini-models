# FitBuddy – AI Fitness Plan Generator

FitBuddy is an AI-powered fitness plan generator that creates safe and general fitness plans using Gemini AI.

## Features

- Personalized fitness plan generation
- User-friendly Streamlit interface
- FastAPI backend
- Gemini AI integration
- Fitness goal and level selection
- Days-per-week customization
- General safety and recovery guidance

## Technologies Used

- Python
- FastAPI
- Streamlit
- Google Gemini API
- Pydantic
- Requests
- python-dotenv

## How It Works

1. User enters their basic fitness details.
2. Streamlit sends the details to the FastAPI backend.
3. FastAPI sends a prompt to Gemini AI.
4. Gemini generates a general fitness plan.
5. The plan is displayed in the Streamlit interface.

## Project Structure

```text
FitBuddy/
│
├── app.py
├── main.py
├── requirements.txt
├── .gitignore
├── .env
└── venv/