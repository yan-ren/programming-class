'''
For this project, you are provided with the mathematics.csv file containing a dataset that includes
values of x and their corresponding y values based on the equation y = x^2. Additionally, a
logarithm_noisy.csv dataset has been provided, which contains logarithmic values with added white
noise. Your task is to analyze this data and create various visualizations following these instructions:
1. Scatter Plot: (20%)
- Create a scatter plot to visualize the relationship between x and y, where y = x^2.
- Ensure that the axes are labeled and the plot has an appropriate title.
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

math_df = pd.read_csv("mathematics.csv")
log_noisy_df = pd.read_csv("logarithm_noisy.csv")

def scatter_plot():
    plt.figure(figsize=(8, 6))
    plt.scatter(math_df['x'], math_df['y'], color='blue')
    plt.title('Scatter Plot of y = x^2')
    plt.xlabel('x')
    plt.ylabel('y = x^2')
    plt.grid(True)
    plt.savefig('scatter_x_squared.png')
    plt.show()

# scatter_plot()
def logarithmic_regression():
    x = log_noisy_df['x']
    log_x = np.log(x)
    y = log_noisy_df['y_noisy']
    # fit linear regression y = a * log(x) + b
    a, b = np.polyfit(log_x, y, 1)
    x_fit = np.linspace(x.min(), x.max(), 300)
    y_fit = a * np.log(x_fit) + b

    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color='blue')
    plt.plot(x_fit, y_fit, color='red')
    plt.title('Logarithmic Regression Fit')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig('logarithmic_regression.png')
    plt.show()

# logarithmic_regression()
'''
3. Square Root Regression: (20%)
- Fit a square root regression model to the data.
- Plot the best-fit square root curve.
- Ensure the plot clearly shows both the data points and the regression line.
'''
def square_root_regression():
    x = log_noisy_df['x']
    sqrt_x = np.sqrt(x)
    y = log_noisy_df['y_noisy']

    a, b = np.polyfit(sqrt_x, y, 1)
    x_fit = np.linspace(x.min(), x.max(), 300)
    y_fit = a * np.sqrt(x_fit) + b

    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color='blue')
    plt.plot(x_fit, y_fit, color='green')
    plt.title('Square Regression Regression Fit')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig('square_root_regression.png')
    plt.show()

# square_root_regression()
'''
4. Additional Complexity: (20%)
- Calculate a new y value based on the equation y = x^3 and add it to the dataset.
- Create a 3D plot visualizing the relationship between x, y(x^2), and y(x^3).
'''
def three_dimension_plot():
    math_df = pd.read_csv('mathematics.csv')
    math_df['y_cubed'] = math_df['x'] ** 3

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(math_df['x'], math_df['y'], math_df['y_cubed'])
    ax.set_title('3D Plot')
    ax.set_xlabel('x')
    ax.set_ylabel('y = x^2')
    ax.set_zlabel('y = x^3')
    plt.savefig('3d_plot.png')
    plt.show()

# three_dimension_plot()

'''
5. Animation: (20%)
- Create an animated plot for y = x^2, where the plot progressively adds data points to simulate the
evolution of the graph over time.
- The animation should be saved as a GIF.
'''
def y_squared_animation():
    df = pd.read_csv('mathematics.csv')
    fig, ax = plt.subplots()

    ax.set_xlim(df['x'].min(), df['x'].max())
    ax.set_ylim(df['y'].min() - 100, df['y'].max())
    ax.set_xlabel('x')
    ax.set_ylabel('y = x^2')

    def update(frame):
        ax.clear()
        ax.set_xlim(df['x'].min(), df['x'].max())
        ax.set_ylim(df['y'].min() - 100, df['y'].max())
        ax.set_xlabel('x')
        ax.set_ylabel('y = x^2')
        ax.set_title('Progressive Plot of y = x^2')
        ax.scatter(df['x'][:frame], df['y'][:frame], color='blue')

    ani = animation.FuncAnimation(fig, update, frames=len(df)+1, interval=100, repeat=False)

    ani.save('animation.gif')
    plt.close(fig)

y_squared_animation()










