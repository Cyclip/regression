import matplotlib.pyplot as plt
import numpy as np
from constants import LENGTH


def plotPoints(x, y, correlation):
    """
    It takes a list of points and plots them
    
    :param points: a list of tuples, each tuple is a point (x, y)
    """
    plt.scatter(
        np.array(x), 
        np.array(y),
        s=8,
        label=f"Correlation: {correlation:.2f}"
    )


def plotLine(m, c, slope):
    x = np.array([0, LENGTH])
    y = np.array([c, (m * LENGTH) + c])
    plt.plot(
        x,
        y,
        label=f"Slope: {slope:.2f}"
    )


def show():
    plt.title("Linear regression model")
    # shrink box
                    
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=5)
    plt.show()
