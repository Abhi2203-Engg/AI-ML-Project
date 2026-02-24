import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

# Create sample dataset
data = {
    "age": [20,25,30,35,40,45,50],
    "weight": [55,60,65,70,75,80,85],
    "height": [160,165,170,175,180,175,168],
    "activity_level": [1,2,2,3,3,1,2],
    "calories": [2000,2200,2400,2600,2800,2500,2300]
}

df = pd.DataFrame(data)

X = df[["age","weight","height","activity_level"]]
y = df["calories"]

model = LinearRegression()
model.fit(X,y)

pickle.dump(model, open("model.pkl","wb"))

print("Model trained and saved!")