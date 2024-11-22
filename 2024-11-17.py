import matplotlib.pyplot as plt
import statistics as st
import pandas as pd

# exercise 1
# t = [0, 1, 2, 3, 4, 5] # time in seconds
# x = [3.1738, 4.1605, 6.0860, 7.6511, 8.9429, 11.6408] # position in metres
#
# # 3. Calculate and print statistics
# average_x = st.mean(x)
# std_dev_x = st.stdev(x)
#
# print(f"Mean of x: {average_x:.4f}")
# print(f"Standard deviation of x: {std_dev_x:.4f}")
#
# m, b = st.linear_regression(t, x)
# # best_x = [m*time + b for time in t] # list comprehension
#
# best_x = []
# for time in t:
#     best_x.append(m*time + b)
#
# plt.scatter(t, x)
# plt.plot(t, best_x, color='red')
# plt.legend()
# plt.show()

# exercise 2
df = pd.read_csv('anscombe.csv')

for i in range(1, 5):
    x = df[f'x{i}']
    y = df[f'y{i}']

    mean_y = st.mean(y)
    std_dev_y = st.stdev(y)

    print(f'Dataset {i} - mean of y: {mean_y:.2f}, std dev of y: {std_dev_y:.2f}')

# line of best fit and plot the data
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# using loops
for i in range(1, 5):
    # i = 1 -> (0, 0)
    # i = 2 -> (0, 1)
    # i = 3 -> (1, 0)
    # i = 4 -> (1, 1)
    ax = axs[(i-1)//2, (i-1)%2]
    x = df[f'x{i}']
    y = df[f'y{i}']

    m, b = st.linear_regression(x, y)
    best_y = m * x + b

    ax.scatter(x, y)
    ax.plot(x, best_y, color='red')
    ax.text(min(x)+0.5, max(y)-1, f'm{m:.2f} b:{b:.2f}')
    ax.set_xlabel(f'x{i}')
    ax.set_ylabel(f'y{i}')

# not using loops
x1 = df['x1']
y1 = df['y1']

m1, b1 = st.linear_regression(x1, y1)
best_y1 = m1 * x1 + b1
axs[0, 0].scatter(x1, y1)
axs[0, 0].plot(x1, best_y1, color='red')
axs[0, 0].text(min(x1)+0.5, 10, f"m:{m1:.2f} b:{b1:.2f}")
axs[0, 0].set_xlabel('x1')
axs[0, 0].set_ylabel('y1')

x2 = df['x2']
y2 = df['y2']
m2, b2 = st.linear_regression(x2, y2)
best_y2 = m2 * x2 + b2
axs[0, 1].scatter(x2, y2)
axs[0, 1].plot(x2, best_y2, color='red')
axs[0, 1].text(min(x2)+0.5, max(y2) - 1, f'm:{m2:.2f} b:{b2:.2f}')
axs[0, 1].set_xlabel('x2')
axs[0, 1].set_ylabel('y2')

x3 = df['x3']
y3 = df['y3']
m3, b3 = st.linear_regression(x3, y3)
best_y3 = m3 * x3 + b3
axs[1, 0].scatter(x3, y3)
axs[1, 0].plot(x3, best_y3, color='red')
axs[1, 0].text(min(x3)+0.5, max(y3) - 1, f'm:{m3:.2f} b:{b3:.2f}')
axs[1, 0].set_xlabel('x3')
axs[1, 0].set_ylabel('y3')

x4 = df['x4']
y4 = df['y4']
m4, b4 = st.linear_regression(x4, y4)
best_y4 = m4 * x4 + b4
axs[1, 1].scatter(x4, y4)
axs[1, 1].plot(x4, best_y4, color='red')
axs[1, 1].text(min(x4)+0.5, max(y4) - 1, f'm:{m4:.2f} b:{b4:.2f}')
axs[1, 1].set_xlabel('x4')
axs[1, 1].set_ylabel('y4')

plt.tight_layout()
plt.show()