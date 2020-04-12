import argparse

import matplotlib.pyplot as plt


def count_trapped_water(elevation_map):
    """
    Counts the number of water units that will be trapped given the elevation map.
    Returns a list where each value corresponds to the number of water units
    that will be trapped in that index of the elevation map.
    """
    msg = 'Elevation map must contain all non-negative integers'
    assert all(map(lambda x: type(x) is int and x >= 0, elevation_map)), msg
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


def visualize_trapped_water(elevation_map):
    """
    Plot the elevation map and units of water.
    Returns None.
    """
    predicted = count_trapped_water(elevation_map)
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
    plt.title('Trapped Rain Water: {} Units of Water'.format(sum(predicted)), fontsize=14)
    plt.legend(bbox_to_anchor=(1,1), loc="upper left")
    plt.grid()
    plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Acquire elevation map.')
    parser.add_argument('elevation_map', nargs='+', type=int,
        help='Elevation map provided as space separated int values, e.g. 1 0 2 3 1 2')
    args = parser.parse_args()
    visualize_trapped_water(args.elevation_map)
