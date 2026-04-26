from operator import invert

import numpy as np
import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# fig = plt.figure(figsize=(8, 6))
# ax = fig.add_subplot(111, projection='3d')
# point, = ax.plot([], [], [], 'o', color = 'orange', markersize=15)
#
# ax.set_xlim(-5, 5)
# ax.set_ylim(-5, 5)
# ax.set_zlim(0, 10)
# ax.set_title("Bouncing Ball")
#
# drop_height = 10
# bounce_factor = 0.7
# gravity = 9.8
#
# def get_z(t):
#     h = drop_height
#     while True:
#         fall_time = np.sqrt(2*h / gravity)
#         bounce_duration = 2 * fall_time
#         if t < bounce_duration:
#             mid = bounce_duration / 2
#             z = h - gravity / 2 * (t - mid) ** 2
#             return max(z, 0)
#         t -= bounce_duration
#         h *= bounce_factor
#         if h < 0.01:
#             return 0
#
# def update(frame):
#     t = frame * 0.05
#     x = 3 * np.sin(t)
#     y = 3 * np.cos(t)
#     z = get_z(t)
#     point.set_data([x], [y])
#     point.set_3d_properties([z])
#
# ani = FuncAnimation(fig, update, frames=300, interval=30)
# plt.show()



# x = np.linspace(-5, 5, 40)
# y = np.linspace(-5, 5, 40)
# X, Y = np.meshgrid(x, y)
# Z = np.sin(np.sqrt(X**2 + Y**2))
#
# fig = plt.figure(figsize=(8, 6))
# ax = fig.add_subplot(111, projection='3d')
# ax.plot_surface(X, Y, Z, cmap='viridis')
# ax.set_title('Rotating Surface')
#
# def update(frame):
#     ax.view_init(elev=30, azim=frame)
#
# ani = FuncAnimation(fig, update, frames=range(0, 360, 2), interval=50)
# plt.show()

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
line, = ax.plot([], [], [], color='purple', linewidth=2)

t_full = np.linspace(0, 4 * np.pi, 300)
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(0, 4 * np.pi)
ax.set_title('Growing Helix')

def update(frame):
    t = t_full[:frame]
    line.set_data(np.cos(t), np.sin(t))
    line.set_3d_properties(t)

ani = FuncAnimation(fig, update, frames=range(1, 300), interval=30)
plt.show()