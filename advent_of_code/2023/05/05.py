from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import get_puzzle_input

from typing import List
from functools import reduce
import re


@aoc_output(title="Day 5 - Lowest seed location")
def get_lowest_seed_location(lines: List[str]):     
    seeds = [int(v) for v in lines[0].split()[1:]]

    map_block_starts = [i for i, l in enumerate(lines) if l == '']
    map_block_ends = map_block_starts[1:] + [len(lines)]

    def _create_block_func(ranges):
        lambda_str = "lambda x: "
        for dest_start, source_start, length in ranges:
            lambda_str += f"{dest_start} + x - {source_start} if {source_start} <= x < {source_start + length} else "
        lambda_str += "x"
        dynamic_lambda = eval(lambda_str)
        return dynamic_lambda

    block_functions = []
    for idx, (start, end) in enumerate(zip(map_block_starts, map_block_ends)):
        block = lines[start+2:end]
        block = [[int(v) for v in l.split()] for l in block]
        block_functions.append(_create_block_func(block))

    locations = [
        reduce(lambda val, func: func(val), [seed] + block_functions)
        for seed in seeds
    ]
    return min(locations)

@aoc_output(title="Day 5 - Lowest seed ranges")
def get_lowest_seed_location_ranges(lines: List[str]):
    s = 0
    windows = []
    for i, line in enumerate(lines):
        l = line.strip()
        if i == 0:
            seeds = [int(x) for x in re.findall("\d+",l)]
            for i in range(0,len(seeds),2):
                windows.append((seeds[i],seeds[i]+seeds[i+1]-1))

    next_windows = windows
    new_windows = []
    for i, l in enumerate(lines[2:]):
        if l == '' or not(l[0].isdigit()):
            next_windows.extend(windows)
            windows = next_windows
            next_windows = []
        elif len(windows) > 0:
            dest_start, source_start, length = [int(x) for x in re.findall("\d+",l)]
            new_windows = []
            for w in windows:
                before = during = after = None
                source_end = source_start + length
                if w[0] < source_start:
                    before = (w[0],min(source_start, w[1]))
                    new_windows.append(before)
                if w[1] > source_end:
                    after = (max(w[0],source_end), w[1])
                    new_windows.append(after)
                if w[0] <= source_start <= w[1] or w[0] <= source_end <= w[1] or source_start <= w[0] <= source_end or source_start <= w[1] <= source_end:
                    during = (max(source_start, w[0]),min(source_end,w[1]))
                    during_length = during[1] - during[0]
                    offset = (max(source_start, w[0]))-source_start
                    during = (dest_start+offset, dest_start+during_length+offset)
                    next_windows.append(during)
            windows = new_windows

    next_windows.extend(windows)
    windows = next_windows

    mins = float('inf')
    for w in windows:
        mins = min(w[0],mins)
    return mins

if __name__ == "__main__":
    pi = get_puzzle_input(__file__)
    get_lowest_seed_location(pi)
    get_lowest_seed_location_ranges(pi)
    # get_lowest_seed_location_ranges_dev(pi)
