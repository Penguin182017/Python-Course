from sklearn.linear_model import LinearRegression

X = [[150], [160], [170], [180], [190]]
y = [3.5, 4.0, 4.5, 5.0, 5.5]

model = LinearRegression()

model.fit(X, y)

prediction = model.predict([[200]])
print("Predicted Weight: ", prediction[0])

r2 = model.score(X, y)
print("R² Score:", r2)