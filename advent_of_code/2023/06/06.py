from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import get_puzzle_input

from typing import List
import numpy as np


@aoc_output(title="Day 6 - Boat Race")
def get_winning_games(lines: List[str]) -> int:
    times = list(map(int, lines[0].split()[1:]))
    distances = list(map(int, lines[1].split()[1:]))
    
    race_winning_times = []
    for time, record_dist in zip(times, distances):
        race_wins = np.sum(np.where((
            np.arange(time+1) *
            np.arange(time+1)[::-1]
        ) > record_dist, 1, 0))
        race_winning_times.append(race_wins)
    return np.prod(race_winning_times)


@aoc_output(title="Day 6 - One Big Race")
def get_large_race_wins(lines: List[str]) -> int:
    times = lines[0].split()
    distances = lines[1].split()
    new_times = int(''.join(times[1:]))
    new_dist = int(''.join(distances[1:]))
    return np.sum(np.where((
        np.arange(new_times+1) *
        np.arange(new_times+1)[::-1]
    ) > new_dist, 1, 0))


if __name__ == "__main__":
    pi = get_puzzle_input(__file__)
    get_winning_games(pi)
    get_large_race_wins(pi)
