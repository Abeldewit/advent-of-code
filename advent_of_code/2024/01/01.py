from collections import Counter
import numpy as np
from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import (
    get_puzzle_input,
    submit_solution,
    convert_to_numbers,
    create_array_from_lines,
)

from typing import List


@aoc_output(title="Day - 1 p1")
def part_1(lines: List[str]) -> int:
    lines = [line.replace("\n", "") for line in lines]
    split_lines = [line.split("   ") for line in lines]
    left_lines = sorted([int(v[0]) for v in split_lines])
    right_lines = sorted([int(v[1]) for v in split_lines])
    return np.sum(np.abs(np.array(left_lines) - np.array(right_lines)))


@aoc_output(title="Day - 1 p2")
def part_2(lines: List[str]) -> int:
    split_lines = [line.split("   ") for line in lines]
    left_lines = sorted([int(v[0]) for v in split_lines])
    right_lines = sorted([int(v[1]) for v in split_lines])
    right_counts = Counter(right_lines)
    similarities = 0
    for num in left_lines:
        if num in right_counts:
            similarities += (num * right_counts[num])
    return similarities


if __name__ == "__main__":
    pi = get_puzzle_input(__file__, block=True)

    # Part 1
    solution_1 = part_1(pi)
    # submit_solution(__file__, solution=solution_1, part='a')

    # Part 2
    solution_2 = part_2(pi)
    submit_solution(__file__, solution=solution_2, part='b')
