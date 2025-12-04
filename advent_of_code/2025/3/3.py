from typing import List

from aocd.models import Puzzle

from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import (
    get_puzzle_lines,
    submit_solution,
)

PUZZLE = Puzzle(year=2025, day=3)


@aoc_output(title=f"Day 3/2025/a - {PUZZLE.title}")
def part_1(lines: List[str]) -> int | None:
    joltages = []
    for bank in lines:
        nums = list(map(int, bank))
        largest_first = max(nums[:-1])
        largest_index = nums.index(largest_first)
        largest_after = max(nums[largest_index + 1 :])
        total_joltage = int(f"{largest_first}{largest_after}")
        joltages.append(total_joltage)
    return sum(joltages)


@aoc_output(title=f"Day 3/2025/b - {PUZZLE.title}")
def part_2(lines: List[str]) -> int | None:
    def find_largest_joltage(nums: List[int], bn: int = 12) -> int:
        buildup, idx = "", 0
        for i in range(bn):
            end_idx = -(bn - i) + 1
            largest = max(nums[idx : end_idx if end_idx != 0 else None])
            largest_idx = nums[idx:].index(largest) + 1 + idx
            buildup += str(largest)
            idx = largest_idx
        return int(buildup)

    joltages = []
    for bank in lines:
        nums = list(map(int, bank))
        lj = find_largest_joltage(nums)
        joltages.append(lj)
    return sum(joltages)


if __name__ == "__main__":
    # pi = get_puzzle_input(__file__, block=True)
    pi = get_puzzle_lines(__file__, block=True)

    part_2(PUZZLE.examples[0][0].split("\n"))

    # Part 1
    solution_1 = part_1(pi)
    submit_solution(__file__, solution=solution_1, part="a")

    # Part 2
    solution_2 = part_2(pi)
    submit_solution(__file__, solution=solution_2, part="b")
