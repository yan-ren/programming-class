from sklearn.datasets import load_iris
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# iris = load_iris()
# X, y = iris.data, iris.target
digits = load_digits()
X, y = digits.data, digits.target
fig, axes = plt.subplots(1, 5, figsize=(10, 3))
for i, ax in enumerate(axes):
    ax.imshow(digits.images[i], cmap='gray')
    ax.set_title(f'Label: {y[i]}')
    ax.axis('off')
plt.show()

#[5.1 3.5 1.4 0.2] sepal length, sepal width, petal length, petal width
# 0: setosa
# 1: versicolor
# 2: virginica
# print(X)
# print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(f'Accuracy: {accuracy_score(y_test, predictions) * 100:.1f}%')

# new_flower = [[5.1, 3.5, 1.4, 0.2]]
# result = model.predict(new_flower)
# print(f'Predicted flower: {iris.target_names[result[0]]}')

# Pick one image from test set and predict
sample_index = 0
sample_image = X_test[sample_index]
predicted_label = model.predict([sample_image])[0]

plt.figure(figsize=(3, 3))
plt.imshow(sample_image.reshape(8, 8), cmap='gray')
plt.show()
print(f'Model predicted {predicted_label}')

