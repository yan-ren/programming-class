from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plot

digits= load_digits()
X, y = digits.data, digits.target

fig, axes = plot.subplots(1, 5, figsize=(10, 3))
for i, ax in enumerate(axes):
    ax.imshow(digits.images[i], cmap='gray')
    ax.set_title(f"Label: {y[i]}")
    ax.axis('off')
plot.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, predictions) * 100:.1f}%")

# Pick one image from test set and predict
sample_index = 1
sample_image = X_test[sample_index]
actual_label = y_test[sample_index]
predicted_label = model.predict([sample_image])[0]

plot.figure(figsize=(3, 3))
plot.imshow(sample_image.reshape(8, 8), cmap='gray')
plot.axis('off')
plot.show()

print(f'model predicted {predicted_label}')