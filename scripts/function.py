import math
import matplotlib.pyplot as plt
import numpy as np
import sys

def f(x, mu, row):
    return (1 / math.sqrt(2 * (row ** 2) * math.pi)) * (math.e ** (- (((x - mu) ** 2) / (2 * (row ** 2)))))

def g(x, mu, row):
    return f(x, mu, row) / f(mu, mu, row)

def main():
    # Get graph info
    if len(sys.argv) == 5:
        title = sys.argv[1]
        x_axis = sys.argv[2]
        y_axis = sys.argv[3]
        output_file = sys.argv[4]
    else:
        error("Invalid number of arguments. Requires title, x-axis, y-axis, and output file.")
        error("")
        error("python function.py TITLE X_AXIS Y_AXIS OUTPUT_FILE")
        sys.exit(1)

    # Get data
    mu = float(raw_input("Mean: "))
    row = float(raw_input("Standard Deviation: "))

    # Create graph
    create_graph(mu, row, title, x_axis, y_axis, output_file)

def create_graph(mu, row, title, x_axis, y_axis, output_file):
    # Generate the (x, y) data
    start = 0
    end = 1
    interval = 0.005
    xs = np.arange(start, end + interval, interval)
    results = [g(x, mu, row) for x in xs]

    # Plot the data
    plt.plot(xs, results)
    plt.title(title)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)

    # Save the graph
    plt.savefig(output_file)

if __name__ == '__main__':
    main()
