from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X = [[150], [160], [170], [180], [190],
     [200], [210], [220], [230], [240]]

y = [3.5, 4.0, 4.5, 5.0, 5.5,
     6.0, 6.5, 7.0, 7.5, 8.0]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

r2 = model.score(X_test, y_test)
print("Test R² Score:", r2)

prediction = model.predict([[250]])
print("Predicted Weight:", prediction[0])