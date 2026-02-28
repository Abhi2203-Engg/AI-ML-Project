def get_workout(goal):
    if goal == "Weight Loss":
        return "Cardio (30 mins), HIIT, Abs workout"
    elif goal == "Muscle Gain":
        return "Strength training, Push-Pull-Legs split"
    else:
        return "Light cardio, Full body workout"

def get_diet(goal):
    if goal == "Weight Loss":
        return "High protein, Low carb diet"
    elif goal == "Muscle Gain":
        return "High protein, Calorie surplus diet"
    else:
        return "Balanced diet with proteins & carbs"

