import numpy as np
import matplotlib.pyplot as plt

# x = np.linspace(-5, 5, 50)
# y = np.linspace(-5, 5, 50)
# X, Y = np.meshgrid(x, y)
# Z = np.sin(np.sqrt(X**2 + Y**2))
#
# fig = plt.figure(figsize=(10, 7))
# ax = fig.add_subplot(111, projection='3d')
# ax.plot_surface(X, Y, Z, cmap='viridis')
# ax.set_title('Surface: sin(sqrt(x^2 + y^2))')
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# plt.show()

np.random.seed(42)
hours_studied = np.random.uniform(1, 10, 100)
hours_slept = np.random.uniform(4, 10, 100)
grade = 40 + 3 * hours_studied + 2 * hours_slept + np.random.normal(0, 5, 100)

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(hours_studied, hours_slept, grade, c=grade, cmap='coolwarm', s=40)
ax.set_xlabel("Hours Studied")
ax.set_ylabel("Hours Slept")
ax.set_zlabel("Grade")
ax.set_title("Student Performance (3D)")
plt.colorbar(sc, label="Grade")
plt.show()