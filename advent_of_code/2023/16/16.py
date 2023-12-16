from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import get_puzzle_input

from typing import List, Tuple
import multiprocessing
import sys
sys.setrecursionlimit(10000)


directions = {
    'N': (-1, 0),
    'E': (0, 1),
    'S': (1, 0),
    'W': (0, -1),
}


def make_next_pos(pos, direction: str):
    d = directions[direction]
    return (pos[0]+d[0], pos[1]+d[1])


def print_grid_pos(lines, pos):
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if pos[0] == y and pos[1] == x:
                print('*', end=' ')
            else:
                print(lines[y][x], end=' ')
        print('')
    print()


def beamfill(lines, direction: str, prev_pos: Tuple[int], history):
    pos = make_next_pos(prev_pos, direction)

    if (
        pos[0] < 0 or
        pos[1] < 0 or
        pos[0] >= len(lines[0]) or
        pos[1] >= len(lines)
    ):
        # Outside of the grid
        return None
    if ((pos, direction) in history):
        # Already walked this path
        return None

    current = lines[pos[0]][pos[1]]
    history.append((pos, direction))

    if current == '.':
        beamfill(lines, direction, pos, history)
    elif current == '|':
        # Check direction
        if direction in ('N', 'S'):
            beamfill(lines, direction, pos, history)
        else:
            beamfill(lines, 'N', pos, history)
            beamfill(lines, 'S', pos, history)
    elif current == '-':
        # Check direction
        if direction in ('E', 'W'):
            beamfill(lines, direction, pos, history)
        else:
            beamfill(lines, 'W', pos, history)
            beamfill(lines, 'E', pos, history)
            
    elif current == '/':
        if direction == 'E':
            beamfill(lines, 'N', pos, history)
        elif direction == 'N':
            beamfill(lines, 'E', pos, history)
        elif direction == 'W':
            beamfill(lines, 'S', pos, history)
        elif direction == 'S':
            beamfill(lines, 'W', pos, history)
    elif current == '\\':
        if direction == 'E':
            beamfill(lines, 'S', pos, history)
        elif direction == 'S':
            beamfill(lines, 'E', pos, history)
        elif direction == 'W':
            beamfill(lines, 'N', pos, history)
        elif direction == 'N':
            beamfill(lines, 'W', pos, history)


def calculate_energize(lines, start, start_dir) -> int:
    history = []
    beamfill(lines, start_dir, start, history)
    return len(set([h[0] for h in history]))


@aoc_output(title="Day 16 - Laser Beams")
def part_1(lines: List[str]) -> int:
    return calculate_energize(lines, (0, -1), 'E')


@aoc_output(title="Day 16 - All the beams!")
def part_2(lines: List[str]) -> int:
    W, H = len(lines[0]), len(lines)
    start_positions = []
    for i in (0, 1):
        for j in range(H):
            start_positions.append(
                (
                    lines,
                    (j, (-1 if i == 0 else W)),
                    ('E' if i == 0 else 'W')
                )
            )
        for j in range(W):
            start_positions.append(
                (
                    lines,
                    ((-1 if i == 0 else H), j),
                    ('S' if i == 0 else 'N')
                )
            )

    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
        result = pool.starmap(calculate_energize, start_positions)

    return max(result)


if __name__ == "__main__":
    pi = get_puzzle_input(__file__, block=True)

    # Part 1
    solution_1 = part_1(pi)

    # Part 2
    solution_2 = part_2(pi)
