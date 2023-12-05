from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import get_puzzle_input

from pathlib import Path
import numpy as np
from typing import List


@aoc_output(title="Day 8 - Treetop Tree House")
def get_visible_trees(lines: List[str]) -> int:
    boom_grid = np.array([list(l.strip()) for l in lines]).astype(int)
    skirt_count = np.sum((boom_grid.shape, boom_grid.shape)) - 4

    def is_visible(grid, x, y):
        self_height = grid[x, y]

        horizontal = grid[x, :]
        vertical = grid[:, y]
        
        left = horizontal[:y]
        right = horizontal[y+1:]
        top = vertical[:x]
        bottom = vertical[x+1:]

        vis_top = len(np.where(top >= self_height)[0]) == 0
        vis_bottom = len(np.where(bottom >= self_height)[0]) == 0
        vis_left = len(np.where(left >= self_height)[0]) == 0
        vis_right = len(np.where(right >= self_height)[0]) == 0

        visible = any((vis_left, vis_right, vis_top, vis_bottom))
        if visible:
            return 1
        return 0

    visible_count = 0
    for y in range(1, boom_grid.shape[1]-1):
        for x in range(1, boom_grid.shape[0]-1):
            visible_count += is_visible(boom_grid, y, x)
    return visible_count


@aoc_output(title='Day 8 - Scenic scores')
def get_scenic_score(lines: List[str]) -> int:
    def _scenic_score(grid, x, y):
        self_height = grid[x, y]

        horizontal = grid[x, :]
        vertical = grid[:, y]

        left = horizontal[:y]
        right = horizontal[y+1:]
        top = vertical[:x]
        bottom = vertical[x+1:]

        scores = []
        for direction in (top[::-1], left[::-1], bottom, right):
            # if edge, make zero
            if len(direction) == 0:
                return 0
            
            dir_score = 0
            for tree in direction:
                dir_score += 1
                if tree >= self_height:
                    break
            if dir_score == 0:
                dir_score = 1
            scores.append(dir_score)
        return np.prod(scores)
        
    boom_grid = np.array([list(l.strip()) for l in lines]).astype(int)
    scenic_scores = np.zeros(boom_grid.shape)
    for x in range(len(lines[0])):
        for y in range(len(lines)):
            scenic_scores[x, y] = _scenic_score(boom_grid, x, y)
    return int(np.max(scenic_scores))


if __name__ == "__main__":
    pi = get_puzzle_input(__file__)
    get_visible_trees(pi)
    get_scenic_score(pi)