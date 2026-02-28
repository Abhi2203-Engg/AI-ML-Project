def get_workout(goal, resource):

    if goal == "Weight Loss":
        return f"{resource} Cardio + HIIT 4-5 days/week"
    
    elif goal == "Muscle Gain":
        return f"{resource} Strength Training 5 days/week"
    
    else:
        return f"{resource} Light cardio + yoga 3-4 days/week"


def get_diet(goal, culture, budget):

    base = f"{culture} | {budget}\n"

    if goal == "Weight Loss":
        return base + "High protein, low carb meals with vegetables and pulses."
    
    elif goal == "Muscle Gain":
        return base + "High protein diet with paneer/chicken, rice, dal."
    
    else:
        return base + "Balanced diet with roti, sabzi, fruits, and milk."
