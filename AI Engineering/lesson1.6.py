from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Data
X = [[1], [2], [3], [4], [5],
     [6], [7], [8], [9], [10]]

y = [42, 50, 58, 65, 73,
     79, 84, 90, 94, 98]

#split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#Create the model
model = LinearRegression()

#train
model.fit(X_train, y_train)

#Test pridiction
prediction = model.predict([[6]])

print("Predicted Score: ", prediction[0])

