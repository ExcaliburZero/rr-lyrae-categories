from __future__ import print_function
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import sys

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
        error("python scatter.py TITLE X_AXIS Y_AXIS OUTPUT_FILE")
        sys.exit(1)

    # Get data
    data_strings = get_stdin()
    data = process_floats(data_strings)

    # Create graph
    create_graph(data, title, x_axis, y_axis, output_file)

def create_graph(data, title, x_axis, y_axis, output_file):
    # Setup graph dimensions
    left, width = 0.1, 0.65
    bottom, height = 0.1, 0.8
    bottom_h = left_h = left + width + 0.02

    rect_scatter = [left, bottom, width, height]
    rect_histy = [left_h, bottom, 0.2, height]

    plt.figure(1, figsize=(10, 8))

    # Create scatter graph
    axScatter = plt.axes(rect_scatter)

    plt.title(title)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)

    # Create histogram
    axHisty = plt.axes(rect_histy)

    nullfmt = ticker.NullFormatter()
    axHisty.yaxis.set_major_formatter(nullfmt)
    axHisty.xaxis.set_major_formatter(nullfmt)

    # Plot scatter data
    points = len(data)
    xs = range(0, points)
    axScatter.scatter(xs, data)

    # Plot histogram data
    start = 0
    end = 1.2 + 0.000000001
    interval = 0.025
    bins = np.arange(start, end, interval)
    axHisty.hist(data, bins=bins, orientation='horizontal')

    # Set graph limits
    offset = points / 50
    axScatter.set_xlim(0 - offset, points + offset)
    axScatter.set_ylim(start, end)

    axHisty.set_ylim(axScatter.get_ylim())

    # Save graph to file
    plt.savefig(output_file)

def process_floats(lines):
    return [float(line) for line in lines]

def get_stdin():
    return sys.stdin.read().split("\n")[0:-1]

def error(message):
    print(message, file=sys.stderr)

if __name__ == '__main__':
    main()
