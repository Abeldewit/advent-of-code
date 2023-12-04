from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import get_puzzle_input
from typing import List
import numpy as np
import re


@aoc_output("Day 4 - Scratch cards")
def get_scratch_sum(lines: List[str]) -> int:
    total_points = 0
    for line in lines:
        numbers = line.split(':')[1].strip()
        winning_numbers = set(
            re.findall(
                r'\d+',
                numbers.split('|')[0]
            )
        )
        my_numbers = set(
            re.findall(
                r'\d+',
                numbers.split('|')[1]
            )
        )

        my_winning_numbers = winning_numbers.intersection(my_numbers)
        card_points = np.product(
            [1] + [2 for _ in range(len(my_winning_numbers)-1)]
        ) if len(my_winning_numbers) > 0 else 0
        total_points += card_points
    return total_points


@aoc_output("Day 4 - Card copies")
def get_copied_count(lines: List[str]) -> int:
    copy_counter = np.ones(len(lines))
    for line in lines:
        card, numbers = line.split(':')
        card_num = int(re.search(r'\d+', card).group()) - 1
        winning_numbers = set(
            re.findall(r'\d+', numbers.split('|')[0])
        )
        my_numbers = set(
            re.findall(r'\d+', numbers.split('|')[1])
        )
        num_matches = len(winning_numbers.intersection(my_numbers))
        copy_counter[card_num+1:card_num+num_matches+1] += 1 * copy_counter[card_num]
    return int(sum(copy_counter))


if __name__ == "__main__":
    pi = get_puzzle_input(__file__)
    get_scratch_sum(pi)

    get_copied_count(pi)
