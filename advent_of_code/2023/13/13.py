from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import get_puzzle_input, submit_solution

from typing import List


@aoc_output(title="Day 13 - Mirrors")
def part_1(lines: List[str]) -> int:
    maps = list(map(str.splitlines, lines.split('\n\n')))

    total_count = 0
    for m in maps:
        vertical, horizontal = 0, 0
        for i in range(len(m)):
            diff_count = 0
            for row_1, row_2 in zip(m[i-1::-1], m[i:]):
                for col_1, col_2 in zip(row_1, row_2):
                    if col_1 != col_2:
                        diff_count += 1
            if diff_count == 0:
                vertical = i
                break
        if vertical != 0:
            total_count += 100 * vertical
            continue

        rot_m = [*zip(*m)]
        for j in range(len(rot_m)):
            diff_count = 0
            for row_1, row_2 in zip(rot_m[j-1::-1], rot_m[j:]):
                for col_1, col_2 in zip(row_1, row_2):
                    if col_1 != col_2:
                        diff_count += 1
            if diff_count == 0:
                horizontal = j
                break
        total_count += horizontal

    return total_count


@aoc_output(title="Day 13 - Smudged Mirrors")
def part_2(lines: List[str]) -> int:
    maps = list(map(str.splitlines, lines.split('\n\n')))

    total_count = 0
    for m in maps:
        vertical, horizontal = 0, 0
        for i in range(len(m)):
            diff_count = 0
            for row_1, row_2 in zip(m[i-1::-1], m[i:]):
                for col_1, col_2 in zip(row_1, row_2):
                    if col_1 != col_2:
                        diff_count += 1
            if diff_count == 1:
                vertical = i
                break
        if vertical != 0:
            total_count += 100 * vertical
            continue

        rot_m = [*zip(*m)]
        for j in range(len(rot_m)):
            diff_count = 0
            for row_1, row_2 in zip(rot_m[j-1::-1], rot_m[j:]):
                for col_1, col_2 in zip(row_1, row_2):
                    if col_1 != col_2:
                        diff_count += 1
            if diff_count == 1:
                horizontal = j
                break
        total_count += horizontal
    return total_count


if __name__ == "__main__":
    pi = get_puzzle_input(__file__, split_lines=False)

    # Part 1
    solution_1 = part_1(pi)
    submit_solution(__file__, solution=solution_1, part='a')

    # Part 2
    solution_2 = part_2(pi)
    submit_solution(__file__, solution=solution_2, part='b')
