import numpy as np

class FrozenLake:
    def __init__(self, grid=None):
        # Grid values: 0 = safe, 1 = hole, 2 = start, 3 = goal.
        if grid is None:
            self.grid = np.array([
                [2, 0, 0, 0],
                [0, 1, 0, 1],
                [0, 0, 0, 0],
                [1, 0, 1, 3]
            ])
        else:
            self.grid = grid
        self.nrows, self.ncols = self.grid.shape
        self.start = self._find_cell(2)
        self.goal = self._find_cell(3)

    def _find_cell(self, value):
        positions = np.argwhere(self.grid == value)
        return tuple(positions[0]) if len(positions) > 0 else None

    def in_bounds(self, pos):
        r, c = pos
        return 0 <= r < self.nrows and 0 <= c < self.ncols

    def is_hole(self, pos):
        r, c = pos
        return self.grid[r][c] == 1

    def is_goal(self, pos):
        return pos == self.goal

    def neighbors(self, pos):
        # Four directions: up, down, left, right.
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        result = []
        for dr, dc in directions:
            new_pos = (pos[0] + dr, pos[1] + dc)
            if self.in_bounds(new_pos) and not self.is_hole(new_pos):
                result.append(new_pos)
        return result

    def heuristic(self, pos):
        # Manhattan distance heuristic
        return abs(pos[0] - self.goal[0]) + abs(pos[1] - self.goal[1])
