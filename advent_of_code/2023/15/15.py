from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import get_puzzle_input

from typing import List
import re
from collections import defaultdict, deque


def string_hasher(string: str) -> int:
    current_value = 0
    for char in list(string):
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value


@aoc_output(title="Day 15 - ASCII Hash")
def part_1(lines: List[str]) -> int:
    strs = lines.split(',')
    total_hashes = []
    for s in strs:
        total_hashes.append(
            string_hasher(s)
        )
    return sum(total_hashes)


@aoc_output(title="Day 15 - Focal strength")
def part_2(lines: List[str]) -> int:
    parts = lines.split(',')
    label_op_pattern = re.compile(r'(\w+)([\-\=]\d?)')

    hash_map = defaultdict(deque)
    for p in parts:
        label, operation = re.match(label_op_pattern, p).groups()
        box_hash = string_hasher(label)
        labels = [v[0] for v in hash_map[box_hash]]
        if operation.startswith('='):
            focal_length = int(operation[1])
            if label in labels:
                hash_map[box_hash][labels.index(label)] = (label, focal_length)
            else:
                hash_map[box_hash].append((label, focal_length))
        else:
            # Pop the label from this box
            if box_hash in hash_map:
                if label in labels:
                    del hash_map[box_hash][labels.index(label)]

    # Calculate focal strength
    total_focal_strength = 0
    for k, v in hash_map.items():
        for c, lens in enumerate(v):
            total_focal_strength += (k+1)*(c+1) * lens[1]

    return total_focal_strength


if __name__ == "__main__":
    pi = get_puzzle_input(__file__, block=True, split_lines=False)

    # Part 1
    solution_1 = part_1(pi)

    # Part 2
    solution_2 = part_2(pi)
