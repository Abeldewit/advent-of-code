from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import get_puzzle_input

from typing import List


def diff_recursion(diff_list: List[int]):
    if all(_ == 0 for _ in diff_list):
        return 0
    else:
        f = diff_recursion([b-a for a, b in zip(diff_list, diff_list[1:])])
        return diff_list[-1] + f


@aoc_output(title="Day 9 - History After")
def part_1(lines: List[str]) -> int:
    history_numbers = [list(map(int, r.split())) for r in lines]
    return sum(diff_recursion(h) for h in history_numbers)


@aoc_output(title="Day 9 - History Before")
def part_2(lines: List[str]) -> int:
    history_numbers = [list(map(int, r.split())) for r in lines]
    return sum(diff_recursion(h[::-1]) for h in history_numbers)


if __name__ == "__main__":
    pi = get_puzzle_input(__file__)

    # Part 1
    solution_1 = part_1(pi)

    # Part 2
    solution_2 = part_2(pi)
