from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X = [[1], [2], [3], [4], [5],
     [6], [7], [8], [9], [10]]

y = [2, 4, 5, 8, 9,
     12, 13, 15, 18, 20]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

train_r2 = model.score(X_train, y_train)
test_r2 = model.score(X_test, y_test)

print("Training R²:", train_r2)
print("Testing R²:", test_r2)