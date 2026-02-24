# utils.py

def get_workout(goal):
    if goal == "Weight Loss":
        return {
            "Monday": "30 min Cardio + Abs workout",
            "Tuesday": "HIIT (20 mins) + Stretching",
            "Wednesday": "Brisk Walking (40 mins)",
            "Thursday": "Lower Body Strength Training",
            "Friday": "Full Body Cardio",
            "Saturday": "Yoga + Core Workout",
            "Sunday": "Rest Day"
        }

    elif goal == "Muscle Gain":
        return {
            "Monday": "Chest + Triceps",
            "Tuesday": "Back + Biceps",
            "Wednesday": "Leg Day",
            "Thursday": "Shoulders",
            "Friday": "Arms + Abs",
            "Saturday": "Full Body Strength",
            "Sunday": "Rest Day"
        }

    else:  # Maintenance
        return {
            "Monday": "Light Cardio (20 mins)",
            "Tuesday": "Full Body Workout",
            "Wednesday": "Yoga",
            "Thursday": "Core Strength",
            "Friday": "Light Jogging",
            "Saturday": "Stretching",
            "Sunday": "Rest Day"
        }


def get_diet(goal):
    if goal == "Weight Loss":
        return {
            "Breakfast": "Oats + Fruits + Green Tea",
            "Lunch": "2 Chapati + Dal + Sabzi + Salad",
            "Snack": "Nuts / Sprouts",
            "Dinner": "Grilled Paneer / Chicken + Vegetables"
        }

    elif goal == "Muscle Gain":
        return {
            "Breakfast": "Eggs / Paneer + Peanut Butter Toast + Milk",
            "Lunch": "Rice + Dal + Chicken / Paneer + Salad",
            "Snack": "Protein Shake + Banana",
            "Dinner": "Chapati + Sabzi + Curd"
        }

    else:  # Maintenance
        return {
            "Breakfast": "Poha / Upma + Tea",
            "Lunch": "Balanced Indian Thali",
            "Snack": "Fruits",
            "Dinner": "Light Chapati + Sabzi"
        }