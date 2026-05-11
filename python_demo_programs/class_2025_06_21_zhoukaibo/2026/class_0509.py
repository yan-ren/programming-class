import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('black')
ax.set_xlim(-2, 2); ax.set_ylim(-2, 2); ax.set_zlim(-2, 2)
ax.set_title("Comet with Trail")

trail, = ax.plot([], [], [], color='cyan', linewidth=2, alpha=0.6)
head,  = ax.plot([], [], [], 'o', color='white', markersize=10)

xs, ys, zs = [], [], []
TRAIL_LEN = 40

def update(frame):
    t = frame * 0.05
    x = 1.5 * np.sin(t)
    y = 1.5 * np.sin(2 * t)        # figure-eight in the xy plane
    z = 1.5 * np.cos(t)

    xs.append(x); ys.append(y); zs.append(z)
    if len(xs) > TRAIL_LEN:
        xs.pop(0); ys.pop(0); zs.pop(0)

    trail.set_data(xs, ys)
    trail.set_3d_properties(zs)
    head.set_data([x], [y])
    head.set_3d_properties([z])

ani = FuncAnimation(fig, update, frames=600, interval=30)
plt.show()