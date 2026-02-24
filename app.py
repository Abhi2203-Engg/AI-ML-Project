import streamlit as st
from model import predict_calories
from utils import get_workout, get_diet

st.set_page_config(page_title="AI Fitness Planner", page_icon="💪")

st.title("💪 Personalized Workout & Diet Planner")
st.write("Enter your details to get AI-based fitness plan")

# User Inputs
age = st.number_input("Age", min_value=10, max_value=100, step=1)
weight = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0, step=0.5)
height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, step=0.5)

activity = st.selectbox(
    "Activity Level",
    [1, 2, 3, 4, 5],
    format_func=lambda x: {
        1: "Sedentary",
        2: "Lightly Active",
        3: "Moderately Active",
        4: "Very Active",
        5: "Super Active"
    }[x]
)

goal = st.selectbox(
    "Fitness Goal",
    ["Weight Loss", "Muscle Gain", "Maintain Weight"]
)

if st.button("Generate Plan 🚀"):

    calories = predict_calories(age, weight, height, activity)
    workout = get_workout(goal)
    diet = get_diet(goal)

    st.success("Here is your personalized plan!")

    st.subheader("🔥 Daily Calories Needed")
    st.write(f"{calories} kcal")

    st.subheader("🏋️ Recommended Workout")
    st.write(workout)

    st.subheader("🥗 Recommended Diet Plan")
    st.write(diet)