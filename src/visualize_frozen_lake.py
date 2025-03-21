import matplotlib.pyplot as plt
import numpy as np
import time

def draw_grid(grid, path=None):
    """
    Draws the Frozen Lake grid.
    - grid: 2D numpy array where
        0 = safe cell, 1 = hole, 2 = start, 3 = goal.
    - path: List of (row, col) tuples representing the current path.
    """
    nrows, ncols = grid.shape
    fig, ax = plt.subplots()
    # Define colors: safe = light blue, hole = black, start = green, goal = red.
    colors = {0: 'lightblue', 1: 'black', 2: 'green', 3: 'red'}
    for i in range(nrows):
        for j in range(ncols):
            color = colors.get(grid[i, j], 'white')
            rect = plt.Rectangle((j, nrows - 1 - i), 1, 1, facecolor=color, edgecolor='gray')
            ax.add_patch(rect)
    # Draw the path if provided.
    if path:
        xs = [col + 0.5 for _, col in path]
        ys = [nrows - 1 - row + 0.5 for row, _ in path]
        ax.plot(xs, ys, marker='o', color='yellow', linewidth=2)
    ax.set_xlim(0, ncols)
    ax.set_ylim(0, nrows)
    ax.set_aspect('equal')
    ax.set_xticks(range(ncols))
    ax.set_yticks(range(nrows))
    plt.gca().invert_yaxis()
    plt.tight_layout()
    return fig, ax

def simulate_frozen_lake():
    # Define the Frozen Lake grid:
    # 0 = safe, 1 = hole, 2 = start, 3 = goal.
    grid = np.array([
        [2, 0, 0, 0],
        [0, 1, 0, 1],
        [0, 0, 0, 0],
        [1, 0, 1, 3]
    ])
    
    # Define a sequence of paths simulating algorithm exploration.
    path_sequence = [
        [(0, 0)],
        [(0, 0), (0, 1)],
        [(0, 0), (0, 1), (0, 2)],
        [(0, 0), (0, 1), (0, 2), (1, 2)],
        [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)],
        [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3)],
        [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (3, 3)]
    ]
    
    plt.ion()  # Turn on interactive mode.
    for path in path_sequence:
        plt.clf()  # Clear the figure.
        draw_grid(grid, path)
        plt.pause(0.7)  # Pause to allow the change to be visible.
    plt.ioff()  # Turn off interactive mode.
    plt.show()

if __name__ == '__main__':
    simulate_frozen_lake()
