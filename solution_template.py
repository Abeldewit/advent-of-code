from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import (
    get_puzzle_input,
    submit_solution,
    convert_to_numbers,
    create_array_from_lines,
)

from typing import List


@aoc_output(title="Day - ")
def part_1(lines: List[str]) -> int:
    pass


@aoc_output(title="Day - ")
def part_2(lines: List[str]) -> int:
    pass


if __name__ == "__main__":
    pi = get_puzzle_input(__file__, block=True)

    # Part 1
    solution_1 = part_1(pi)
    submit_solution(__file__, solution=solution_1, part='a')

    # Part 2
    solution_2 = part_2(pi)
    submit_solution(__file__, solution=solution_2, part='b')
