from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import get_puzzle_input, submit_solution

from typing import List
import numpy as np


def move_boulders(grid, direction=(-1, 0)):
    current_grid, prev_grid = grid.copy(), np.zeros(grid.shape)

    while not np.all(current_grid == prev_grid):
        prev_grid = current_grid.copy()
        for i, row in enumerate(current_grid):
            for j, ch in enumerate(row):
                roll_pos = np.array((i, j)) + direction
                if roll_pos[0] < 0 or roll_pos[1] < 0 or roll_pos[0] >= grid.shape[0] or roll_pos[1] >= grid.shape[1]:
                    continue

                if ch == 'O' and current_grid[*roll_pos] == '.':
                    current_grid[i, j] = '.'
                    current_grid[*roll_pos] = 'O'
    return current_grid

def count_load(rolled_grid) -> int:
    total = 0
    for i in range(rolled_grid.shape[0]):
        dist_to_south = rolled_grid.shape[0] - i
        total += sum(rolled_grid[i, :] == 'O') * dist_to_south
    return total


def make_boulder_grid(lines: List[str]) -> np.ndarray:
    return np.array([list(row) for row in lines])


@aoc_output(title="Day - ")
def part_1(lines: List[str]) -> int:
    grid = make_boulder_grid(lines)
    rolled_grid = move_boulders(grid)
    return count_load(rolled_grid)


@aoc_output(title="Day - ")
def part_2(lines: List[str]) -> int:
    grid = make_boulder_grid(lines)

    cycle_directions = [
        (-1, 0),  # North
        (0, -1),  # West
        (1, 0),  # South
        (0, 1)  # East
    ]

    cycles = 1000000000
    cycle_grid = grid.copy()
    for c in range(cycles):
        for d in cycle_directions:
            cycle_grid = move_boulders(cycle_grid, direction=d).copy()
        print(c)

    return count_load(cycle_grid)


if __name__ == "__main__":
    pi = get_puzzle_input(__file__, block=True)

    # Part 1
    # solution_1 = part_1(pi)
    # submit_solution(__file__, solution=solution_1, part='a')

    # Part 2
    solution_2 = part_2(pi)
    submit_solution(__file__, solution=solution_2, part='b')
