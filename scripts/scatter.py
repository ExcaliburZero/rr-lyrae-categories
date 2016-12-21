from __future__ import print_function
import matplotlib.pyplot as plt
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
    # Plot data
    xs = range(0, len(data))
    plt.scatter(xs, data)

    # Label graph
    plt.title(title)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)

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
