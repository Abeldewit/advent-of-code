from pathlib import Path
import string
import numpy as np

puzzle_input = Path(__file__).parent.joinpath('puzzle_input.txt')
with open(puzzle_input, 'r') as f:
    lines = [line.strip() for line in f.readlines()]


nummap = [
    'one', 'two', 'three',
    'four', 'five', 'six',
    'seven', 'eight', 'nine',
]


def find_indexes(string_to_search: str, search_terms: list) -> int:
    # Iterate through the string to find occurrences of the search term
    indexes = []
    for num in search_terms:
        index = 0
        while index < len(string_to_search):
            index = string_to_search.find(num, index)
            if index == -1:
                break
            indexes.append((index, num))
            index += len(num)
    return indexes


def find_first_last(line: str, digit_only=True):
    digit_idx = find_indexes(line, list(string.digits))
    num_idx = find_indexes(line, nummap) if not digit_only else []

    indexes = sorted(digit_idx + num_idx, key=lambda x: x[0])
    first_num = indexes[0][1]
    last_num = indexes[-1][1]

    first_num = first_num if len(first_num) == 1 else nummap.index(first_num) + 1
    last_num = last_num if len(last_num) == 1 else nummap.index(last_num) + 1

    return int(f"{first_num}{last_num}")


part_1 = [find_first_last(l) for l in lines]
part_2 = [find_first_last(l, digit_only=False) for l in lines]

print(f"Part 1: {sum(part_1)}")
print(f"Part 2: {sum(part_2)}")
