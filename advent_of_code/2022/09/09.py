from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import get_puzzle_input

from typing import List
import numpy as np
import time
import os
clear = lambda: os.system('clear')

SHOW_GRID = False

@aoc_output(title="Day - ")
def part_1(lines: List[str]) -> int:
    grid_size = 700
    grid = np.zeros((grid_size, grid_size, 3))
    
    # Set Head and Tail position
    grid[int(grid_size/2), int(grid_size/2), 0] = 1
    grid[int(grid_size/2), int(grid_size/2), 1] = 1
    
    def _repr_grid(grid):
        if not SHOW_GRID:
            return
        clear()
        for row in grid:
            for col in row:
                if col[0] == 0 and col[1] == 0:
                    print('.', end='')
                elif col[0] == 1:
                    print('H', end='')
                elif col[1] == 1:
                    print('T', end='')
            print()
        print()
        
    def _tail_adjacent(grid):
        head_pos = [v[0] for v in np.nonzero(grid[:, :, 0])]
        mask = grid[head_pos[0]-1:head_pos[0]+2, head_pos[1]-1:head_pos[1]+2, :]
        if np.sum(mask[:, :, 1]) > 0:
            return True
        return False
    
    def _adjust_tail(grid):
        head_pos = [v[0] for v in np.nonzero(grid[:, :, 0])]
        tail_pos = [v[0] for v in np.nonzero(grid[:, :, 1])]
        new_pos = tail_pos
        mask = grid[head_pos[0]-2:head_pos[0]+3, head_pos[1]-2:head_pos[1]+3, :]
        tail_mask = mask[:, :, 1]
        
        diag = False
        if np.sum(tail_mask[:, 2]) > 0:
            # Vertical
            up_or_down = 1 if np.nonzero(tail_mask[:, 2])[0][0] < 2 else -1
            new_pos = (tail_pos[0]+up_or_down, tail_pos[1])
        elif np.sum(tail_mask[2, :]) > 0:
            # Horiztonal
            left_or_right = 1 if np.nonzero(tail_mask[2, :])[0][0] < 2 else -1
            new_pos = (tail_pos[0], tail_pos[1]+left_or_right)
        else:
            # Diagonal
            diag = True
            row_above, row_below = tail_mask[1, :], tail_mask[3, :]
            col_left, col_right = tail_mask[:, 1], tail_mask[:, 3]
            if np.sum(row_above) > 0:
                new_pos = (tail_pos[0]+1, tail_pos[1])
            elif np.sum(row_below) > 0:
                new_pos = (tail_pos[0]-1, tail_pos[1])
            elif np.sum(col_left) > 0:
                new_pos = (tail_pos[0], tail_pos[1]+1)
            elif np.sum(col_right) > 0:
                new_pos = (tail_pos[0], tail_pos[1]-1)
        grid[tail_pos[0], tail_pos[1], 1] = 0
        grid[new_pos[0], new_pos[1], 1] = 1
        if diag: _adjust_tail(grid)
        return False
    
    def _update_pos_grid(grid):
        tail_pos = np.nonzero(grid[:, :, 1])
        grid[*tail_pos, 2] = 1
    
    def _move_head(grid, instruction):
        move_dir, amount = instruction.split(' ')
        directions = {
            'U': (-1, 0),
            'R': (0, 1),
            'L': (0, -1),
            'D': (1, 0)
        }
        move = directions[move_dir]
        for _ in range(int(amount)):
            head_pos = np.nonzero(grid[:, :, 0])
            grid[head_pos[0], head_pos[1], 0] = 0
            grid[
                head_pos[0] + move[0],
                head_pos[1] + move[1],
                0
            ] = 1
            _repr_grid(grid)
            adj = _tail_adjacent(grid)
            if not adj:
                _adjust_tail(grid)
                _repr_grid(grid)
                _update_pos_grid(grid)
            
            if SHOW_GRID: time.sleep(.2)
    
    _repr_grid(grid)
    _update_pos_grid(grid)
    for i, line in enumerate(lines):
        _move_head(grid, line)
        
    pos_grid = grid[:, :, 2]
    return np.sum(pos_grid)


@aoc_output(title="Day - ")
def part_2(lines: List[str]) -> int:
    pass


if __name__ == "__main__":
    pi = get_puzzle_input(__file__)
    part_1(pi)