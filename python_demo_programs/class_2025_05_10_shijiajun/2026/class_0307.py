'''
matplot lib math equation examples
trig functions
'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# # generate x values from -2pi to 2pi
# x = np.linspace(-2 * np.pi, 2 * np.pi, 400)
# y_sin = np.sin(x)
# y_cos = np.cos(x)
# y_tan = np.tan(x)
#
# plt.plot(x, y_sin, label='sin(x)')
# plt.plot(x, y_cos, label='cos(x)')
# plt.plot(x, y_tan, label='tan(x)')
#
# plt.xlabel('x')
# plt.ylabel('y')
# plt.ylim(-5, 5)
# plt.legend()
# plt.grid(True)
#
# plt.show()

x = np.linspace(0, 2*np.pi, 400)
y_sin = np.sin(x)
y_cos = np.cos(x)

angle = np.pi
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

sin_line, = ax.plot(x, y_sin, label='sin(x)')
cos_line, = ax.plot(x, y_cos, label='cos(x)')

sin_point, = ax.plot(angle, np.sin(angle), 'o')
cos_point, = ax.plot(angle, np.cos(angle), 'o')

ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1.5, 1.5)
ax.legend()

ax_slider = plt.axes((0.2, 0.1, 0.6, 0.03))
slider = Slider(ax_slider, 'Angle', 0, 2*np.pi, valinit=angle)

def update(val):
    a = slider.val
    sin_point.set_data([a], [np.sin(a)])
    cos_point.set_data([a], [np.cos(a)])
    fig.canvas.draw_idle()

slider.on_changed(update)

plt.show()
