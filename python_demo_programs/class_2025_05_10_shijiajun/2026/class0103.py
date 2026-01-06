import math

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
# x = [1, 2, 3, 4, 5]
a = 1
b = 2
c = 3
y = a*x ** 2 + b * x + c

print(y)
plt.plot(x, y)
plt.show()

# x = np.arange(0, 10)
#
# plt.plot(x, math.sqrt(1 - x**2), label='y = x')
# plt.plot(x, x**2, label='y = x^2')
# plt.plot(x, x**3, label='y = x^3')

# plt.legend()
# plt.show()

# x = np.linspace(-1, 1, 400)
# y = np.sqrt(1 - x**2)
# y2 = -np.sqrt(1 - x**2)
# plt.plot(x, y, label='upper')
# plt.plot(x, y2, label='lower')
#
# plt.axis("equal")
# plt.legend()
# plt.show()

# r = 5
# theta = np.linspace(0, 2 * np.pi, 200)
# x = r * np.cos(theta)
# y = r * np.sin(theta)
#
# plt.plot(x, y)
# plt.axis('equal')
# plt.title('circle')
# plt.show()