import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics as st

# df = pd.read_csv('anscombe.csv')
#
# x_cols = ['x1', 'x2', 'x3', 'x4']
# y_cols = ['y1', 'y2', 'y3', 'y4']
#
# for col in x_cols:
#     mean_val = st.mean(df[col])
#     stdev_val = st.stdev(df[col])
#     print(f'For colum {col}: mean = {mean_val:.2f}, stdev = {stdev_val:.2f}')
#
# for col in y_cols:
#     mean_val = st.mean(df[col])
#     stdev_val = st.stdev(df[col])
#     print(f'For colum {col}: mean = {mean_val:.2f}, stdev = {stdev_val:.2f}')
#
# plt.figure(figsize=(10, 8))
#
# for i in range(4):
#     x = df[x_cols[i]]
#     y = df[y_cols[i]]
#
#     m, b = st.linear_regression(x, y)
#     best_y = m * x + b
#     plt.subplot(2, 2, i + 1)
#     plt.scatter(x, y)
#     plt.plot(x, best_y, color='red')
#     plt.xlabel(x_cols[i])
#     plt.ylabel(y_cols[i])
#
#     plt.text(min(x) + 0.5, 10, f'm:{m:.2f} b:{b:.2f}')
#
# plt.tight_layout()
# plt.show()

from math import factorial

def taylor_sin(x, n_terms):
    y = np.zeros_like(x)
    for n in range(n_terms):
        sign =  (-1) ** n
        term = x** (2*n + 1) / factorial(2*n + 1)
        y += sign * term

    return y


n_terms = int(input("Enter number of Taylor series terms: "))

x = np.linspace(-4*np.pi, 4*np.pi, 100)

plt.figure(figsize=(10, 6))
plt.plot(x, taylor_sin(x, n_terms), label=f'{n_terms} terms (order {2*n_terms - 1})')

# plt.figure(figsize=(10, 6))
#
# orders = [1, 3, 5, 7, 9]
# for order in orders:
#     n_terms = (order + 1) // 2
#     plt.plot(x, taylor_sin(x, n_terms), label=f'Order {order}')

plt.ylim(-2, 2)
plt.axhline(0, color='gray', lw=1)
plt.axvline(0, color='gray', lw=1)
plt.title('Taylor Polynomial Approximations of sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
