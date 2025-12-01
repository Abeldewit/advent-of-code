from typing import List

from aocd.models import Puzzle

from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import (
    convert_to_numbers,
    create_array_from_lines,
    get_puzzle_input,
    get_puzzle_lines,
    submit_solution,
)

PUZZLE = Puzzle(year={YEAR}, day={DAY})


@aoc_output(title=f"Day {DAY}/{YEAR}/a - {PUZZLE.title}")
def part_1(lines: List[str]) -> int | None:
    pass


@aoc_output(title=f"Day {DAY}/{YEAR}/b - {PUZZLE.title}")
def part_2(lines: List[str]) -> int | None:
    pass


if __name__ == "__main__":
    # pi = get_puzzle_input(__file__, block=True)
    pi = get_puzzle_lines(__file__, block=True)

    # Part 1
    solution_1 = part_1(pi)
    submit_solution(__file__, solution=solution_1, part="a")

    # Part 2
    solution_2 = part_2(pi)
    submit_solution(__file__, solution=solution_2, part="b")
