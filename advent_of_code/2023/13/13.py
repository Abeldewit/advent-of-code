from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import get_puzzle_input
from typing import List


def find_mirror_line(m, diff_allowance: int = 0) -> int:
    mirror_lines = 0
    for i in range(len(m)):
        diff_count = 0
        for row_1, row_2 in zip(m[i-1::-1], m[i:]):
            for col_1, col_2 in zip(row_1, row_2):
                if col_1 != col_2:
                    diff_count += 1
        if diff_count == diff_allowance:
            mirror_lines += 100 * i
            break

    rot_m = [*zip(*m)]
    for j in range(len(rot_m)):
        diff_count = 0
        for row_1, row_2 in zip(rot_m[j-1::-1], rot_m[j:]):
            for col_1, col_2 in zip(row_1, row_2):
                if col_1 != col_2:
                    diff_count += 1
        if diff_count == diff_allowance:
            mirror_lines += j
            break
    return mirror_lines


@aoc_output(title="Day 13 - Mirrors")
def part_1(lines: List[str]) -> int:
    maps = list(map(str.splitlines, lines.split('\n\n')))
    return sum(find_mirror_line(m) for m in maps)


@aoc_output(title="Day 13 - Smudged Mirrors")
def part_2(lines: List[str]) -> int:
    maps = list(map(str.splitlines, lines.split('\n\n')))
    return sum(find_mirror_line(m, 1) for m in maps)


if __name__ == "__main__":
    pi = get_puzzle_input(__file__, split_lines=False)

    # Part 1
    solution_1 = part_1(pi)

    # Part 2
    solution_2 = part_2(pi)
