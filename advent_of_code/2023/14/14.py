from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import get_puzzle_input, submit_solution

from typing import List
import numpy as np
from tqdm import tqdm
import itertools


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


def boulder_optim(grid, direction='N'):
    H, W = len(grid), len(grid[0])
    if direction == 'N':
        for x in range(W):
            dy = 0
            for y in range(H):
                ch = grid[y][x]
                if ch == '.':
                    dy += 1
                if ch == '#':
                    dy = 0
                elif ch == 'O':
                    grid[y][x] = '.'
                    grid[y-dy][x] = 'O'
    elif direction == 'S':
        for x in range(W):
            dy = 0
            for y in range(H-1, -1, -1):
                ch = grid[y][x]
                if ch == '.':
                    dy += 1
                elif ch == '#':
                    dy = 0
                elif ch == 'O':
                    grid[y][x] = '.'
                    grid[y+dy][x] = 'O'
    elif direction == 'E':
        for y in range(H):
            dx = 0
            for x in range(W-1, -1, -1):
                ch = grid[y][x]
                if ch == '.':
                    dx += 1
                elif ch == '#':
                    dx = 0
                elif ch == 'O':
                    grid[y][x] = '.'
                    grid[y][x+dx] = 'O'
    elif direction == 'W':
        for y in range(H):
            dx = 0
            for x in range(W):
                ch = grid[y][x]
                if ch == '.':
                    dx += 1
                elif ch == '#':
                    dx = 0
                elif ch == 'O':
                    grid[y][x] = '.'
                    grid[y][x-dx] = 'O'
    return grid


def count_load(rolled_grid) -> int:
    total = 0
    for i in range(rolled_grid.shape[0]):
        dist_to_south = rolled_grid.shape[0] - i
        total += sum(rolled_grid[i, :] == 'O') * dist_to_south
    return total


def make_boulder_grid(lines: List[str]) -> np.ndarray:
    return np.array([list(row) for row in lines])


def unique(grid):
    return hash(tuple([''.join(row) for row in grid]))


def weight(grid):
    return sum((len(grid)-y)*row.count('O') for y,row in enumerate(grid))


@aoc_output(title="Day - ")
def part_1(lines: List[str]) -> int:
    grid = make_boulder_grid(lines)
    rolled_grid = move_boulders(grid)
    return count_load(rolled_grid)

@aoc_output(title="Day - ")
def part_2(lines: List[str]) -> int:
    grid = [list(line) for line in lines]

    cycle_directions = ('N', 'W', 'S', 'E')

    cycles = 1000000000
    cycle_grid = grid

    seen = [0]
    scores = [0]

    pbar = tqdm(total=4*cycles)
    for i in itertools.count():
        for d in cycle_directions:
            cycle_grid = boulder_optim(grid, d)

        cur = unique(cycle_grid)
        scores.append(weight(grid))
        pbar.update(1)

        if cur in seen:
            break
        seen.append(cur)

    pat0 = seen.index(cur)
    cycle = len(seen) - pat0
    want = (1000000000 - pat0) % cycle + pat0

    return scores[want]


if __name__ == "__main__":
    pi = get_puzzle_input(__file__, block=True)

    # Part 1
    # solution_1 = part_1(pi)
    # submit_solution(__file__, solution=solution_1, part='a')

    # Part 2
    solution_2 = part_2(pi)
    submit_solution(__file__, solution=solution_2, part='b')
