import matplotlib
matplotlib.use("TkAgg")

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


INIT_AMP = 1.0
INIT_FREQ = 1.0

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

def compute(amp, freq):
    y_sin = amp * np.sin(freq * x)
    y_cos = amp * np.cos(freq * x)
    y_tan = amp * np.tan(freq * x)
    y_tan = np.where(np.abs(y_tan) > 5, np.nan, y_tan)
    return y_sin, y_cos, y_tan


fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(bottom=0.25)

y_sin, y_cos, y_tan = compute(INIT_AMP, INIT_FREQ)
line_sin, = ax.plot(x, y_sin, color="steelblue", linewidth=2, label="sin(x)")
line_cos, = ax.plot(x, y_cos, color="coral",     linewidth=2, label="cos(x)")
line_tan, = ax.plot(x, y_tan, color="seagreen",  linewidth=2,
                    linestyle="--", label="tan(x)")
ax.axhline(0, color='gray', linewidth=0.8)
ax.axvline(0, color='gray', linewidth=0.8)
ax.set_ylim(-4, 4)
ax.set_xlabel("x (radians)", fontsize=13)
ax.set_ylabel("y", fontsize=13)
ax.legend(loc="upper right", fontsize=11)
title = ax.set_title(f"A = {INIT_AMP:.2f}  |  f = {INIT_FREQ:.2f}", fontsize=13)

ax_amp  = plt.axes([0.15, 0.13, 0.65, 0.03])
ax_freq = plt.axes([0.15, 0.07, 0.65, 0.03])
slider_amp  = Slider(ax_amp,  "Amplitude",  0.1, 3.0, valinit=INIT_AMP,  color="steelblue")
slider_freq = Slider(ax_freq, "Frequency",  0.5, 4.0, valinit=INIT_FREQ, color="coral")

def update(_):
    amp  = slider_amp.val
    freq = slider_freq.val
    y_sin, y_cos, y_tan = compute(amp, freq)
    line_sin.set_ydata(y_sin)
    line_cos.set_ydata(y_cos)
    line_tan.set_ydata(y_tan)
    title.set_text(f"A = {amp:.2f}  |  f = {freq:.2f}")
    fig.canvas.draw_idle()

slider_amp.on_changed(update)
slider_freq.on_changed(update)

plt.show()