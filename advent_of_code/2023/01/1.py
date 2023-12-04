import string
from typing import List

from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import get_puzzle_input


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


@aoc_output(title="Day 1 - Calibration Values")
def get_calibration_values(lines: List[str]) -> int:
    running_sum = 0
    for line in lines:
        digit_idx = find_indexes(line, list(string.digits))

        indexes = sorted(digit_idx, key=lambda x: x[0])
        first_num = indexes[0][1]
        last_num = indexes[-1][1]
        running_sum += int(f"{first_num}{last_num}")
    return running_sum


@aoc_output(title="Day 1 - Spelled calibration")
def get_spelled_numbers(lines: List[str]) -> int:
    nummap = ['one', 'two', 'three', 'four', 'five',
              'six', 'seven', 'eight', 'nine']
    running_sum = 0
    for line in lines:
        digit_idx = find_indexes(line, list(string.digits))
        num_idx = find_indexes(line, nummap)

        indexes = sorted(digit_idx + num_idx, key=lambda x: x[0])
        first_num = indexes[0][1]
        last_num = indexes[-1][1]

        first_num = (
            first_num 
            if len(first_num) == 1 
            else nummap.index(first_num) + 1
        )
        last_num = (
            last_num 
            if len(last_num) == 1 
            else nummap.index(last_num) + 1
        )
        running_sum += int(f"{first_num}{last_num}")
    return running_sum


if __name__ == "__main__":
    pi = get_puzzle_input(__file__)
    get_calibration_values(pi)
    get_spelled_numbers(pi)
