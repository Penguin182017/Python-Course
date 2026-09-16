from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4], [5]]
y = [50, 60, 70, 80, 90]

model = LinearRegression()

model.fit(X, y)

prediction = model.predict([[6]])

print(prediction)