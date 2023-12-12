from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import get_puzzle_input

from typing import List, Tuple
from functools import lru_cache


def create_input_split(lines: List[str]) -> List[Tuple[str]]:
    return [
        (
            line.split()[0],
            tuple(map(int, line.split()[1].split(',')))
        )
        for line in lines
    ]


@lru_cache(maxsize=None)
def solve_line(line, remaining_numbers):
    if len(line) == 0:
        return 1 if len(remaining_numbers) == 0 else 0
    if line.startswith('.'):
        return solve_line(line.strip('.'), remaining_numbers)
    if line.startswith('?'):
        return (
            solve_line(line.replace('?', '.', 1), remaining_numbers) +
            solve_line(line.replace('?', '#', 1), remaining_numbers)
        )
    if line.startswith('#'):
        if len(remaining_numbers) == 0:
            return 0
        if len(line) < remaining_numbers[0]:
            return 0
        if any(c == '.' for c in line[0:remaining_numbers[0]]):
            return 0
        if len(remaining_numbers) > 1:
            if (len(line) < remaining_numbers[0] + 1) or\
                    (line[remaining_numbers[0]] == '#'):
                return 0

            return solve_line(
                line[remaining_numbers[0] + 1:],
                remaining_numbers[1:]
            )

        else:
            return solve_line(
                line[remaining_numbers[0]:],
                remaining_numbers[1:]
            )
    raise Exception("None of the options have been reached!")


@aoc_output(title="Day - ")
def part_1(lines: List[Tuple[str]]) -> int:
    return sum([
        solve_line(line[0], line[1])
        for line in lines
    ])


@aoc_output(title="Day - ")
def part_2(lines: List[str]) -> int:
    return sum([
        solve_line(
            '?'.join([line[0] for _ in range(5)]),
            line[1]*5
        )
        for line in lines
    ])


if __name__ == "__main__":
    pi = get_puzzle_input(__file__, block=True)
    split_pi = create_input_split(pi)

    # Part 1
    solution_1 = part_1(split_pi)

    # Part 2
    solution_2 = part_2(split_pi)
