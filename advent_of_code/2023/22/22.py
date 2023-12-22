from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import get_puzzle_input, submit_solution

from typing import List
from collections import namedtuple
from itertools import combinations


Brick = namedtuple('Brick', ['id', 'cells', 'minZ'])


def create_bricks(lines: List[str]) -> List[Brick]:
    bricks = []
    for i, line in enumerate(lines):
        begin, end = (tuple(map(int, p.split(','))) for p in line.split('~'))
        cells, minZ = [], 1 << 16
        for x in range(min(begin[0], end[0]), max(begin[0], end[0])+1):
            for y in range(min(begin[1], end[1]), max(begin[1], end[1])+1):
                for z in range(min(begin[2], end[2]), max(begin[2], end[2])+1):
                    cells.append((x, y, z))
                    minZ = min(minZ, z)
        bricks.append(Brick(i, cells, minZ))
    return sorted(bricks, key=lambda b: b.minZ)


def lower_brick(b):
    return Brick(b.id, [(x, y, z-1) for x, y, z in b.cells], b.minZ-1)


def can_lower(occupied, b):
    return (
        b.minZ > 1 and not occupied & set((x, y, z-1) for x, y, z in b.cells)
    )


def apply_gravity(bricks):
    final_bricks = {}
    occupied = set()
    for b in bricks:
        while can_lower(occupied, b):
            b = lower_brick(b)
        occupied |= set(x for x in b.cells)
        final_bricks[b.id] = b
    return final_bricks


@aoc_output(title="Day - ")
def part_1(lines: List[str]) -> int:
    bricks = create_bricks(lines)
    fallen_bricks = apply_gravity(bricks)

    can_be_destroyed = 0
    for less_one in combinations(fallen_bricks.values(), len(fallen_bricks)-1):
        temp = apply_gravity(less_one)
        can_be_destroyed += all(
            tp.minZ == fallen_bricks[id].minZ for id, tp in temp.items()
        )
    return can_be_destroyed


@aoc_output(title="Day - ")
def part_2(lines: List[str]) -> int:
    pass


if __name__ == "__main__":
    pi = get_puzzle_input(__file__, block=True)

    # Part 1
    solution_1 = part_1(pi)
    submit_solution(__file__, solution=solution_1, part='a')

    # Part 2
    # solution_2 = part_2(pi)
    # submit_solution(__file__, solution=solution_2, part='b')
