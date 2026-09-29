import streamlit as st
import requests

st.set_page_config(
    page_title="FitBuddy",
    page_icon="💪",
    layout="centered"
)

st.title("💪 FitBuddy")
st.subheader("AI Fitness Plan Generator")
st.write("Create a personalized general fitness plan using Gemini AI.")

st.divider()

name = st.text_input("Name", placeholder="Enter your name")

age = st.number_input(
    "Age",
    min_value=13,
    max_value=100,
    value=18
)

goal = st.selectbox(
    "Fitness Goal",
    [
        "Improve general fitness",
        "Build strength",
        "Improve endurance",
        "Improve flexibility"
    ]
)

fitness_level = st.selectbox(
    "Fitness Level",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

days_per_week = st.slider(
    "Days per Week",
    min_value=1,
    max_value=7,
    value=3
)

st.divider()

if st.button("✨ Generate Fitness Plan", type="primary", use_container_width=True):

    if not name:
        st.warning("Please enter your name.")

    else:

        data = {
            "name": name,
            "age": age,
            "goal": goal,
            "fitness_level": fitness_level,
            "days_per_week": days_per_week
        }

        try:

            with st.spinner("Generating your fitness plan..."):

                response = requests.post(
                    "http://127.0.0.1:8000/generate",
                    json=data
                )

            if response.status_code == 200:

                result = response.json()

                st.success("Fitness plan generated successfully!")

                st.subheader("📋 Your Fitness Plan")

                st.write(result["fitness_plan"])

            else:

                st.error(
                    f"Error generating plan: {response.status_code}"
                )

        except Exception as e:

            st.error("Could not connect to the FastAPI backend.")

            st.write(str(e))