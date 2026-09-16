from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4], [5],
     [6], [7], [8], [9], [10]]

y = [2, 4, 5, 8, 9,
     12, 13, 15, 18, 20]

model = LinearRegression()

model.fit(X, y)

print("Training R²:", model.score(X, y))