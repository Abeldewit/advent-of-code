import numpy as np
from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import (
    get_puzzle_input,
    submit_solution,
    convert_to_numbers,
    create_array_from_lines,
)

from typing import List


def is_safe(arr):
    diff = np.diff(arr)
    abs_diff = np.abs(np.diff(arr))
    
    same_sign = False
    in_bounds = False
    if np.all(np.sign(diff) == np.sign(diff[0])):
        same_sign = True
        
    if len(np.where((abs_diff >= 1) & (abs_diff <= 3))[0]) == len(abs_diff):
        in_bounds = True

    return same_sign and in_bounds



@aoc_output(title="Day - ")
def part_1(lines: List[str]) -> int:
    result = sum([is_safe(line) for line in lines])
    return result


@aoc_output(title="Day - ")
def part_2(lines: List[str]) -> int:
    safe_count = 0
    for line in lines:
        if is_safe(line):
            safe_count += 1
            continue
        
        for i in range(len(line)):
            new_arr = line[:i] + line[i+1:]
            sub_safe = is_safe(new_arr)
            if sub_safe:
                safe_count+=1
                break
    return safe_count


if __name__ == "__main__":
    pi = get_puzzle_input(__file__, block=True)
    pi = convert_to_numbers(pi)

    # Part 1
    solution_1 = part_1(pi)
    submit_solution(__file__, solution=solution_1, part='a')

    # Part 2
    solution_2 = part_2(pi)
    submit_solution(__file__, solution=solution_2, part='b')
