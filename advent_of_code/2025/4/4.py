from typing import List

from aocd.models import Puzzle

from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import (
    get_puzzle_lines,
    submit_solution,
)

PUZZLE = Puzzle(year=2025, day=4)


@aoc_output(title=f"Day 4/2025/a - {PUZZLE.title}")
def part_1(lines: List[str]) -> int | None:
    paper_map = [list(line) for line in lines]
    width, height = len(paper_map[0]), len(paper_map)
    padded_paper_map = [
        *[list("." * (len(paper_map[0]) + 2))],
        *map(lambda x: [".", *x, "."], paper_map),
        *[list("." * (len(paper_map[0]) + 2))],
    ]

    def check_around_roll(y, x):
        c = 0
        for yi in range(y - 1, y + 2):
            for xi in range(x - 1, x + 2):
                if yi == y and xi == x:
                    continue
                if padded_paper_map[yi][xi] == "@":
                    c += 1
        return c < 4

    roll_counter = 0
    for y in range(1, height + 1):
        for x in range(1, width + 1):
            if padded_paper_map[y][x] == "@":
                if check_around_roll(y, x):
                    roll_counter += 1
    return roll_counter


@aoc_output(title=f"Day 4/2025/b - {PUZZLE.title}")
def part_2(lines: List[str]) -> int | None:
    paper_map = [list(line) for line in lines]
    width, height = len(paper_map[0]), len(paper_map)
    padded_paper_map = [
        *[list("." * (len(paper_map[0]) + 2))],
        *map(lambda x: [".", *x, "."], paper_map),
        *[list("." * (len(paper_map[0]) + 2))],
    ]

    def check_around_roll(y, x):
        c = 0
        for yi in range(y - 1, y + 2):
            for xi in range(x - 1, x + 2):
                if yi == y and xi == x:
                    continue
                if padded_paper_map[yi][xi] == "@":
                    c += 1
        return c < 4

    def check_roll_removal(roll_map):
        roll_counter = 0
        roll_locations = []
        for y in range(1, height + 1):
            for x in range(1, width + 1):
                if padded_paper_map[y][x] == "@":
                    if check_around_roll(y, x):
                        roll_counter += 1
                        roll_locations.append((y, x))
        new_map = [
            [
                field if (yi, xi) not in roll_locations else "x"
                for xi, field in enumerate(line)
            ]
            for yi, line in enumerate(roll_map)
        ]
        return new_map, len(roll_locations)

    removal = True
    roll_counter = 0
    while removal:
        nm, rc = check_roll_removal(padded_paper_map)
        if rc == 0:
            removal = False
            break
        roll_counter += rc
        padded_paper_map = nm

    return roll_counter


if __name__ == "__main__":
    # pi = get_puzzle_input(__file__, block=True)
    pi = get_puzzle_lines(__file__, block=True)

    part_2(PUZZLE.examples[0][0].split("\n"))
    # Part 1
    # solution_1 = part_1(pi)
    # submit_solution(__file__, solution=solution_1, part="a")

    # Part 2
    solution_2 = part_2(pi)
    submit_solution(__file__, solution=solution_2, part="b")
