import random
from constants import LENGTH, NOISE_LEVEL


def genDataset(n=10):
    """
    It generates a random line, then generates random points on that line, then adds noise to the y
    coordinates of those points
    
    :param n: number of points to generate, defaults to 10 (optional)
    :return: A tuple of two lists.
    """
    noiseLevel = NOISE_LEVEL * random.randint(75, 250) / 100
    noiseLevel = round(noiseLevel)

    slope = random.randint(-500, 500) / 100
    intercept = random.randint(-(LENGTH*300), round(LENGTH*300)) / 50

    print(f"y = {slope}x + {intercept}")

    # random points on the line
    x = [random.randint(100, LENGTH * 100) / 100 for i in range(n)]
    y = [calcY(slope, intercept, i) for i in x]

    # scatter y coordinates
    y = [noise(i, noiseLevel=noiseLevel) for i in y]

    return x, y


def noise(v, noiseLevel=20):
    """
    It takes a value and adds a random number between -noiseLevel and noiseLevel to it
    
    :param v: the value to be noised
    :param noiseLevel: The amount of noise to add to the data, defaults to 20 (optional)
    :return: the value of v + x.
    """
    x = random.randint(-noiseLevel * 100, noiseLevel * 100) / 100
    return v + x


def calcY(slope, intercept, x):
    """
    > It takes the slope and intercept of a line and an x value and returns the corresponding y value
    
    :param slope: the slope of the line
    :param intercept: The y-intercept of the line
    :param x: The x-coordinate of the point to calculate the y-coordinate for
    :return: The y value of the line
    """
    # y = mx + c
    return (slope * x) + intercept