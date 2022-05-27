import dataset
import math
import plotting
import numpy as np


def calcMean(vals):
    """
    It takes a list of numbers and returns the average of those numbers
    
    :param vals: a list of numbers
    :return: The mean of the values in the list.
    """
    return sum(vals)/len(vals)


def sd(vals, mean):
    """
    > The function takes a list of values and returns the standard deviation of those values
    
    :param vals: the list of values
    :return: The standard deviation of the values in the list.
    """
    mots = sum([i**2 for i in vals])/len(vals)
    sotm = mean**2

    return math.sqrt(mots - sotm)


def calcSlope(sdx, sdy, correlation):
    """
    The slope of the regression line is the standard deviation of the dependent variable divided by the
    standard deviation of the independent variable, multiplied by the correlation between the two
    variables
    
    :param sdx: standard deviation of x
    :param sdy: standard deviation of y
    :param correlation: The correlation between the two variables
    :return: The slope of the regression line
    """
    return (sdy/sdx) * correlation


def main():
    x, y = dataset.genDataset(n=350)

    correlation = np.corrcoef(np.array(x), np.array(y))[1,0]

    meanx = calcMean(x)
    meany = calcMean(y)
    
    sdx = sd(x, meanx)
    sdy = sd(y, meany)
    slope = calcSlope(sdx, sdy, correlation)
    yintercept = meany - (slope * meanx)

    plotting.plotPoints(x, y, correlation)
    plotting.plotLine(slope, yintercept, slope)

    # print(f"Mean x:  {meanx}")
    # print(f"Mean y:  {meany}")
    # print(f"SD of x: {sdx}")
    # print(f"SD of y: {sdy}")
    # print(f"Slope:   {slope}")
    # print(f"Y-Inter: {yintercept}")

if __name__ == "__main__":
    for i in range(5):
        main()
    
    
    plotting.show()