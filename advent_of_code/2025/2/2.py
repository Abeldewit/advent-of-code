from typing import List

from aocd.models import Puzzle
from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import get_puzzle_input, submit_solution
from tqdm import tqdm

PUZZLE = Puzzle(year=2025, day=2)


@aoc_output(title=f"Day 2/2025/a - {PUZZLE.title}")
def part_1(lines: List[str]) -> int:
    def is_double_repeat(s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        mid = len(s) // 2
        return s[:mid] == s[mid:]

    total = 0
    for line in lines:
        start, end = map(int, line.split("-"))
        for num in range(start, end + 1):
            if is_double_repeat(str(num)):
                total += num
    return total


@aoc_output(title=f"Day 2/2025/b - {PUZZLE.title}")
def part_2(lines: List[str]) -> int:
    def is_repeating_pattern(id_str: str) -> bool:
        length = len(id_str)
        # We only need to check patterns up to half the length of the string
        for i in range(1, length // 2 + 1):
            if length % i == 0:
                pattern = id_str[:i]
                if pattern * (length // i) == id_str:
                    return True
        return False

    total = 0
    for line in tqdm(lines):
        start, end = map(int, line.split("-"))
        for num in range(start, end + 1):
            if is_repeating_pattern(str(num)):
                total += num
    return total


if __name__ == "__main__":
    pi = get_puzzle_input(__file__, block=True)
    pi = pi.split(",")

    # Part 1
    solution_1 = part_1(pi)
    submit_solution(__file__, solution=solution_1, part="a")

    # Part 2
    solution_2 = part_2(pi)
    submit_solution(__file__, solution=solution_2, part="b")
