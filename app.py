import streamlit as st
from model import predict_calories
from utils import get_workout, get_diet

st.set_page_config(page_title="AI Fitness Planner", page_icon="💪")

st.title("💪 Personalized Workout & Diet Planner for Students")
st.write("AI-based system generating student-friendly fitness plans")

# ----------------------
# User Inputs
# ----------------------

age = st.number_input("Age", min_value=15, max_value=60, step=1)
weight = st.number_input("Weight (kg)", min_value=30.0, max_value=150.0, step=0.5)
height = st.number_input("Height (cm)", min_value=100.0, max_value=220.0, step=0.5)

activity = st.selectbox(
    "Activity Level",
    {
        1: "Sedentary",
        2: "Lightly Active",
        3: "Moderately Active",
        4: "Very Active",
        5: "Super Active"
    }
)

goal = st.selectbox(
    "Fitness Goal",
    ["Weight Loss", "Muscle Gain", "Maintain Fitness"]
)

culture = st.selectbox(
    "Diet Preference",
    ["Indian Vegetarian", "Indian Non-Vegetarian", "Jain", "Vegan"]
)

budget = st.selectbox(
    "Budget Level",
    ["Low Budget", "Medium Budget", "High Budget"]
)

resource = st.selectbox(
    "Available Resources",
    ["Home Workout", "Gym Access", "Hostel Limited Space"]
)

# ----------------------
# Generate Plan
# ----------------------

if st.button("Generate My Plan"):

    calories = predict_calories(age, weight, height, activity)

    workout = get_workout(goal, resource)
    diet = get_diet(goal, culture, budget)

    st.success("Here is Your Personalized Plan 🎯")

    st.subheader("🔥 Daily Calorie Requirement")
    st.write(f"{calories} kcal/day")

    st.subheader("🏋 Workout Plan")
    st.write(workout)

    st.subheader("🥗 Diet Plan")
    st.write(diet)

