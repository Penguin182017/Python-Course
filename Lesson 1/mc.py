import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "Flipper": [160, 170, 178, 183, 190, 198],
    "Weight": [2.5, 3.0, 3.6, 4.1, 4.8, 5.3]
}

df = pd.DataFrame(data)

X = df[["Flipper"]]
y = df["Weight"]

model = LinearRegression()

model.fit(X, y)

prediction = model.predict([[200]])

print("Predicted weight:", prediction[0])