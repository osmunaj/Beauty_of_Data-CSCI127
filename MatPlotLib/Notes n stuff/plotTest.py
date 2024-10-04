import matplotlib.pyplot as plt
import numpy as np

def plot_line(x1, y1, x2, y2):
    x = [x1, x2]
    y = [y1, y2]
    plt.plot(x, y)



def main(graphMin, graphMax):
    plt.xlim(graphMin, graphMax)
    plt.ylim(graphMin, graphMax)
    plot_line(graphMin, graphMin, graphMax, graphMax)
    plt.show()

main(-100, 100)