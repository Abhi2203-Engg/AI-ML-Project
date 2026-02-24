import pickle
import numpy as np
import os

if not os.path.exists("model.pkl"):
    print("ERROR: model.pkl not found. Run train_model.py first.")
    exit()

model = pickle.load(open("model.pkl","rb"))

def predict_calories(age, weight, height, activity):
    input_data = np.array([[age, weight, height, activity]])
    prediction = model.predict(input_data)
    return round(prediction[0],2)
