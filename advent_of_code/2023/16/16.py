from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import get_puzzle_input, submit_solution

from typing import List
from functools import lru_cache
from collections import deque
import multiprocessing
from tqdm import tqdm
import os

directions = {
    'N': (-1, 0),
    'E': (0, 1),
    'S': (1, 0),
    'W': (0, -1),
}


@lru_cache(maxsize=None)
def make_next_pos(pos, direction: str):
    d = directions[direction]
    return (pos[0]+d[0], pos[1]+d[1])


def print_grid_pos(lines, pos):
    os.system('clear')
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if pos[0] == y and pos[1] == x:
                print('*', end=' ')
            else:
                print(lines[y][x], end=' ')
        print('')
    print()


@aoc_output(title="Day - ")
def part_1(lines: List[str]) -> int:

    start = (0, -1)
    history = []
    paths_to_walk = deque()
    paths_to_walk.append((start, 'E'))
    while paths_to_walk:
        pos, direction = paths_to_walk.pop()
        while True:
            pos = make_next_pos(pos, direction)
            if (
                pos[0] < 0 or
                pos[1] < 0 or
                pos[0] >= len(lines[0]) or
                pos[1] >= len(lines)
            ):
                # Outside of the grid
                break
            if ((pos, direction) in history):
                # Already walked this path
                break
            
            current = lines[pos[0]][pos[1]]
            # print_grid_pos(lines, pos)
            history.append((pos, direction))
            
            if current == '.':
                continue
            elif current == '|':
                # Check direction
                if direction in ('N', 'S'):
                    continue
                else:
                    paths_to_walk.append((pos, 'S'))
                    paths_to_walk.append((pos, 'N'))
                    break
            elif current == '-':
                # Check direction
                if direction in ('E', 'W'):
                    continue
                else:
                    paths_to_walk.append((pos, 'E'))
                    paths_to_walk.append((pos, 'W'))
                    break
            
            elif current == '/':
                if direction == 'E':
                    # beamfill('N', pos)
                    direction = 'N'
                elif direction == 'N':
                    # beamfill('E', pos)
                    direction = 'E'
                elif direction == 'W':
                    # beamfill('S', pos)
                    direction = 'S'
                elif direction == 'S':
                    # beamfill('W', pos)
                    direction = 'W'
            elif current == '\\':
                if direction == 'E':
                    # beamfill('S', pos)
                    direction = 'S'
                elif direction == 'S':
                    # beamfill('E', pos)
                    direction = 'E'
                elif direction == 'W':
                    # beamfill('N', pos)
                    direction = 'N'
                elif direction == 'N':
                    # beamfill('W', pos)
                    direction = 'W'
    return len(set([h[0] for h in history]))


def calculate_energize(lines, start_queue):
    history = []
    paths_to_walk = deque()
    paths_to_walk.append(start_queue)
    while paths_to_walk:
        pos, direction = paths_to_walk.pop()
        while True:
            pos = make_next_pos(pos, direction)
            if (
                pos[0] < 0 or
                pos[1] < 0 or
                pos[0] >= len(lines[0]) or
                pos[1] >= len(lines)
            ):
                # Outside of the grid
                break
            if ((pos, direction) in history):
                # Already walked this path
                break
            
            current = lines[pos[0]][pos[1]]
            # print_grid_pos(lines, pos)
            history.append((pos, direction))
            
            if current == '.':
                continue
            elif current == '|':
                # Check direction
                if direction in ('N', 'S'):
                    continue
                else:
                    paths_to_walk.append((pos, 'S'))
                    paths_to_walk.append((pos, 'N'))
                    break
            elif current == '-':
                # Check direction
                if direction in ('E', 'W'):
                    continue
                else:
                    paths_to_walk.append((pos, 'E'))
                    paths_to_walk.append((pos, 'W'))
                    break
            
            elif current == '/':
                if direction == 'E':
                    # beamfill('N', pos)
                    direction = 'N'
                elif direction == 'N':
                    # beamfill('E', pos)
                    direction = 'E'
                elif direction == 'W':
                    # beamfill('S', pos)
                    direction = 'S'
                elif direction == 'S':
                    # beamfill('W', pos)
                    direction = 'W'
            elif current == '\\':
                if direction == 'E':
                    # beamfill('S', pos)
                    direction = 'S'
                elif direction == 'S':
                    # beamfill('E', pos)
                    direction = 'E'
                elif direction == 'W':
                    # beamfill('N', pos)
                    direction = 'N'
                elif direction == 'N':
                    # beamfill('W', pos)
                    direction = 'W'

    return len(set([h[0] for h in history]))


@aoc_output(title="Day - ")
def part_2(lines: List[str]) -> int:
    W, H = len(lines[0]), len(lines)
    start_positions = []
    for i in (0, 1):
        for j in range(H):
            start_positions.append(
                (
                    lines,
                    (
                        (j, (-1 if i == 0 else W+1)),
                        ('E' if i == 0 else 'W')
                    )
                )
            )
        for j in range(W):
            start_positions.append(
                (
                    lines,
                    (
                        ((-1 if i == 0 else H+1), j),
                        ('S' if i == 0 else 'N')
                    )
                )
            )
            
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        result = pool.starmap(calculate_energize, tqdm(start_positions))
    return max(result)


if __name__ == "__main__":
    pi = get_puzzle_input(__file__, block=True)

    # Part 1
    # solution_1 = part_1(pi)
    # submit_solution(__file__, solution=solution_1, part='a')

    # Part 2
    solution_2 = part_2(pi)
    # submit_solution(__file__, solution=solution_2, part='b')
