import matplotlib.pyplot as plt

x_values = []
y_values = []

# y = x^2
for x in range(-10, 11):
    x_values.append(x)
    y_values.append(x ** 2)

plt.plot(x_values, y_values)
plt.title('Quadratic: y = x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
