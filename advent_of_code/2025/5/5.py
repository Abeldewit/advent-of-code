from typing import List, Tuple

from aocd.models import Puzzle

from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import get_puzzle_input, submit_solution 


PUZZLE = Puzzle(year=2025, day=5)


@aoc_output(title=f"Day 5/2025/a - {PUZZLE.title}")
def part_1(fresh_produce: List[str], available_ids: List[str]) -> int | None:
    ranges = []
    for line in fresh_produce:
        start, end = tuple(map(int, line.split("-")))
        ranges.append((start, end))
    
    return sum([
        any([(i, r) for r in ranges if (i >= r[0] and i <= r[1])])
        for i in map(int, available_ids)
    ])


@aoc_output(title=f"Day 5/2025/b - {PUZZLE.title}")
def part_2(fresh_produce: List[str], available_ids: List[str]) -> int | None:
    ranges = []
    for line in fresh_produce:
        start, end = map(int, line.split("-"))
        ranges.append((start, end))
        
    ranges.sort()
    # Find overlapping ranges first
    merged = []
    current_start, current_end = ranges[0]

    for s, e in ranges[1:]:
        if s <= current_end + 1:   # Overlaps or touches
            current_end = max(current_end, e)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = s, e

    merged.append((current_start, current_end))

    # Count total size of merged ranges
    return sum(e - s + 1 for s, e in merged)


def split_input(pi: str) -> Tuple[List[str], List[str]]:
    p1, p2 = pi.split("\n\n")
    return p1.split("\n"), p2.split("\n")

if __name__ == "__main__":
    pi = get_puzzle_input(__file__, block=True)
    fresh_produce, available_ids = split_input(pi)


    # # Part 1
    solution_1 = part_1(fresh_produce, available_ids)
    submit_solution(__file__, solution=solution_1, part="a")

    # Part 2
    solution_2 = part_2(fresh_produce, available_ids)
    submit_solution(__file__, solution=solution_2, part="b")
