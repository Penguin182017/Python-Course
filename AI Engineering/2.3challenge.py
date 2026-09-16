from sklearn.linear_model import LinearRegression

X = [
    [150, 35, 2],
    [160, 38, 3],
    [170, 40, 4],
    [180, 43, 5],
    [190, 45, 6]
]

y = [3.5, 4.0, 4.5, 5.0, 5.5]

model = LinearRegression()

model.fit(X, y)

prediction = model.predict([[200, 48, 7]])
print("Prediction:", prediction[0])

prediction = model.predict([[200, 60, 7]])
print("Prediction:", prediction[0])

print("Coefficients:", model.coef_)
