from typing import List

from aocd.models import Puzzle

from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import get_puzzle_lines, submit_solution

PUZZLE = Puzzle(year=2025, day=1)


@aoc_output(title=f"Day 1/2025/a - {PUZZLE.title}")
def part_1(lines: List[str]) -> int:
    """Turn a dial with numbers 0-99 and count whenever its at zero.

    Using the modulo operator (which also works with negatives) we can
    calculate where the dial will stop with simple subtraction/addition
    based on turning left or right.

    Args:
        lines: A list of lines containing the direction and number of clicks.

    Returns:
        The total amount of stops at zero.
    """
    dial_num = 50
    zero_counter = 0
    for line in lines:
        if not line:
            continue
        print(line)
        turn = int(line[1:])
        if line[0] == "L":
            turn *= -1
        dial_num = (dial_num + turn) % 100

        # Count whenever the dial stops at exactly zero
        if dial_num == 0:
            zero_counter += 1
    return zero_counter


@aoc_output(title=f"Day 1/2025/b - {PUZZLE.title}")
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

        # Compared to part 1, we need to do every 'click' and count whenever it passes zero
        for _ in range(int(line[1:])):
            dial_num = (dial_num + (1 if not left else -1)) % 100
            if dial_num == 0:
                zero_counter += 1
    return zero_counter


if __name__ == "__main__":
    pi = get_puzzle_lines(__file__, block=True)

    # Part 1
    solution_1 = part_1(pi)
    submit_solution(__file__, solution=solution_1, part="a")

    # Part 2
    solution_2 = part_2(pi)
    submit_solution(__file__, solution=solution_2, part="b")
