from typing import List

from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import get_puzzle_input, submit_solution


@aoc_output(title="Day - ")
def part_1(lines: List[str]) -> int:
    dial_num = 50
    zero_counter = 0
    for line in lines:
        if not line:
            continue
        turn = int(line[1:])
        if line[0] == "L":
            turn *= -1
        dial_num = (dial_num + turn) % 100

        if dial_num == 0:
            zero_counter += 1
    return zero_counter


@aoc_output(title="Day - ")
def part_2(lines: List[str]) -> int:
    dial_num = 50
    zero_counter = 0
    for line in lines:
        if not line:
            continue
        if line[0] == "L":
            left = True
        else:
            left = False

        for _ in range(int(line[1:])):
            dial_num = (dial_num + (1 if not left else -1)) % 100
            if dial_num == 0:
                zero_counter += 1
    return zero_counter


if __name__ == "__main__":
    pi = get_puzzle_input(__file__, block=True)

    # Part 1
    solution_1 = part_1(pi)
    submit_solution(__file__, solution=solution_1, part="a")

    # Part 2
    solution_2 = part_2(pi)
    submit_solution(__file__, solution=solution_2, part="b")
