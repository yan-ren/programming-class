'''
AI -> machine learning -> deep learning

two main types of machine learning problem
- classification - prediction a category
e.g.
what digit is this? (0-9)
is this email spam or not

- regression - predict a number
e.g.
what will the temperature be tomorrow?
what will this house sell for?
'''
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# fake data: hours studied vs exam score
hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
scores = np.array([52, 58, 65, 70, 75, 82, 85, 90, 92, 98])

X_train, X_test, y_train, y_test = train_test_split(hours, scores, test_size=0.2, random_state=42)
# Train
# Hint: look at decision tree from last class
model = LinearRegression()
model.fit(X_train, y_train)

predict = model.predict(X_test)

plt.scatter(hours, scores, color='blue', label='Actual data')
plt.plot(hours, model.predict(hours), color='red', label='Best fit line')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.title('Linear Regression')
plt.legend()
plt.show()

# predict a new value
new_hours = [[7.5]]
print(f'Predicted score for 7.5 hours: {model.predict(new_hours)[0]:.1f}')
