from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import get_puzzle_input, submit_solution

from typing import List, Tuple
import numpy as np
from collections import deque
from tqdm import tqdm


def expand_galaxy(galaxy_map):
    height, width = galaxy_map.shape
    row_expansion = []
    col_expansion = []

    for y in range(height):
        row = galaxy_map[y, :]
        if all([v == '.' for v in row]):
            row_expansion.append(y)
    for x in range(width):
        row = galaxy_map[:, x]
        if all([v == '.' for v in row]):
            col_expansion.append(x)

    for c, row in enumerate(row_expansion):
        new_row = np.array(['*' for _ in range(galaxy_map[row+c, :].shape[0])])
        galaxy_map = np.insert(galaxy_map, row+c, new_row, axis=0)
    for c, col in enumerate(col_expansion):
        new_col = np.array(['*' for _ in range(galaxy_map[:, col+c].shape[0])])
        galaxy_map = np.insert(galaxy_map, col+c, new_col, axis=1)
    return galaxy_map


def get_empty_y_count(grid, id1, id2):
    cnt = 0
    for i in range(id1, id2, 1):
        if grid[i][0] == '*':
            cnt += 1
    return cnt


def get_empty_x_count(grid, id1, id2):
    cnt = 0
    for i in range(id1, id2, 1):
        if grid[0][i] == '*':
            cnt += 1
    return cnt


def get_distance(grid, star1, star2, star_dist):
    empty_y_count = get_empty_y_count(
        grid, min(star1[1], star2[1]), max(star1[1], star2[1])
    )
    empty_x_count = get_empty_x_count(
        grid, min(star1[2], star2[2]), max(star1[2], star2[2])
    )
    y_dist = abs(star1[1]-star2[1]) + empty_y_count*(star_dist-1)
    x_dist = abs(star1[2]-star2[2]) + empty_x_count*(star_dist-1)
    return x_dist + y_dist


@aoc_output(title="Day - ")
def part_1(lines: List[str]) -> int:
    galaxy_map = np.array([[char for char in line] for line in lines])
    exp_map = expand_galaxy(galaxy_map)

    loc_i, loc_j = np.where(exp_map == '#')
    star_list = []
    for idx, (i, j) in enumerate(zip(loc_i, loc_j)):
        star_list.append((idx+1, i, j))

    result_sum = 0
    for i in range(len(star_list)-1):
        for j in range(i+1, len(star_list), 1):
            result_sum += get_distance(exp_map, star_list[i], star_list[j], 2)

    return result_sum


@aoc_output(title="Day - ")
def part_2(lines: List[str]) -> int:
    galaxy_map = np.array([[char for char in line] for line in lines])
    exp_map = expand_galaxy(galaxy_map)

    loc_i, loc_j = np.where(exp_map == '#')
    star_list = []
    for idx, (i, j) in enumerate(zip(loc_i, loc_j)):
        star_list.append((idx+1, i, j))

    result_sum = 0
    for i in range(len(star_list)-1):
        for j in range(i+1, len(star_list), 1):
            result_sum += get_distance(exp_map, star_list[i], star_list[j], 1000000-1)

    return result_sum



if __name__ == "__main__":
    pi = get_puzzle_input(__file__, block=True)

    # Part 1
    solution_1 = part_1(pi)
    # if (input('Submit part a (Y/N): ') == 'Y'):
    #     submit_solution(__file__, solution=solution_1, part='a')

    # Part 2
    solution_2 = part_2(pi)
    if (input('Submit part b (Y/N): ') == 'Y'):
        submit_solution(__file__, solution=solution_2, part='b')
