import argparse

import matplotlib.pyplot as plt
import numpy as np


def _get_row_count(row):
    """
    Helper function for row-by-row count function (i.e. axis == 0).
    Counts the number of water units for a given row.
    Returns an integer representing the number of water units in that row.
    """
    indexes = np.argwhere(row == 1)
    count = 0
    if len(indexes) > 1:
        # we know that two points separated by at least one zero will collect water
        # since the separation indicates a decrease in height in that position
        for i in range(len(indexes)-1):
            count += indexes[i+1][0] - indexes[i][0] - 1

    return count


def count_trapped_water(elevation_map, axis=1):
    """
    Counts the number of water units that will be trapped given the elevation map.
    Returns a list where each value corresponds to the number of water units
    that will be trapped in that index of the elevation map given the axis.
    """
    msg = 'Elevation map must contain all non-negative integers'
    assert all(map(lambda x: type(x) is int and x >= 0, elevation_map)), msg

    if axis == 0:
        # start off with all zeroes
        grid = np.zeros((len(elevation_map), max(elevation_map)))
        # mark indexes as 1 up to and including the height
        for index in range(len(elevation_map)):
            grid[index, :elevation_map[index]] = 1
        if grid.shape[1]:
            water_units = np.apply_along_axis(_get_row_count, axis=0, arr=grid)
        else:
            water_units = []

    if axis == 1:
        leader = elevation_map[0]
        water_units = []
        for index in range(1, len(elevation_map)-1):
            height = elevation_map[index]
            max_height_remainder = max(elevation_map[index+1:])
            # if the greatest subsequent height is less than the current height
            # then water units will all subsequently be a difference between
            # that greatest subsequent height and the height being measured
            if max_height_remainder < height:
                leader = max_height_remainder
                water_units.append(0)
                continue
            if height > leader:
                leader = height
                water_units.append(0)
            else:
                water_units.append(leader - height)
        # add 0 to both ends of list to account for first and last units
        water_units = [0] + water_units + [0]

    return water_units


def visualize_trapped_water(elevation_map, axis=1):
    """
    Plot the elevation map and units of water.
    Returns None.
    """
    predicted = count_trapped_water(elevation_map, axis)
    # combine predicted trapped water counts with elevation map counts to produce
    # plotting coordinates for trapped water
    predicted_plot = [x+y for x,y in zip(predicted, elevation_map)]
    plt.figure(figsize=(len(elevation_map)+1, max(elevation_map)+1))
    # NOTE: align='edge' is necessary otherwise bars will be centered
    plt.bar(range(len(elevation_map)), predicted_plot, width=1.0, align='edge', facecolor='blue', label='water')
    plt.bar(range(len(elevation_map)), elevation_map, width=1.0, align='edge', facecolor='black', label='structure')
    plt.xticks(range(len(elevation_map)), ['' for _ in range(len(elevation_map))])
    plt.yticks(range(max(elevation_map)), ['' for _ in range(max(elevation_map))])
    plt.xlim([0, len(elevation_map)]) # constrain width of plot
    plt.ylim([0, max(elevation_map)]) # constrain height of plot
    plt.title('Trapped Rain Water: {:,} Units of Water'.format(sum(predicted)), fontsize=14)
    plt.legend(bbox_to_anchor=(1,1), loc="upper left")
    plt.grid()
    plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Acquire elevation map.')
    parser.add_argument('-e', '--elevation_map', nargs='+', type=int, required=True,
        help='Elevation map provided as space separated int values, e.g. 1 0 2 3 1 2')
    parser.add_argument('-a', '--axis', choices=(0,1), default=1, type=int,
        help='Axis to apply function to (options: 0,1; default: 1).')
    parser.add_argument('-p', '--plot', action='store_true',
        help='Whether to visualize the trapped water. If provided, the function axis used is 1.')
    args = parser.parse_args()
    if args.plot:
        # to do visualization, the axis must be 1 (which is set as default)
        visualize_trapped_water(args.elevation_map)
    else:
        print('Number of Water Units: {:,}'.format(sum(count_trapped_water(args.elevation_map,
                                                                           axis=args.axis))))
