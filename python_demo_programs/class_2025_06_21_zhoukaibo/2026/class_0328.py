import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2 * np.pi, 2 * np.pi, 500)

y_sin = np.sin(x)
y_cos = np.cos(x)
y_tan = np.tan(x)

y_tan = np.where(np.abs(y_tan) > 5, np.nan, y_tan)

plt.figure(figsize=(10, 6))
plt.plot(x, y_sin, label="sin(x)", color="steelblue", linewidth=2)
plt.plot(x, y_cos, label="cos(x)", color="coral", linewidth=2)
plt.plot(x, y_tan, label="tan(x)", color="seagreen", linewidth=2, linestyle="--")

plt.axhline(0, color="gray", linewidth=0.8, linestyle="-")
plt.axvline(0, color="gray", linewidth=0.8, linestyle="-")

plt.ylim(-3, 3)
plt.xlabel("x (radians)", fontsize=13)
plt.ylabel("y", fontsize=13)

plt.tight_layout()
plt.show()