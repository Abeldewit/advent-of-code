from collections import defaultdict
from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import (
    get_puzzle_input,
    submit_solution,
)

from typing import Counter, List


def stone_logic(stone: int):
    if stone == 0:
        return (1,)
    if (stone_len:=len(str(stone))) % 2 == 0:
        s1, s2 = str(stone)[:stone_len//2], str(stone)[stone_len//2:]
        return (int(s1), int(s2))
    else:
        return (stone*2024,)
    

def stone_splitting(stones, blinks: int = 25):
    stones = Counter(int(num) for num in stones.split())
    
    for _ in range(blinks):
        new_stones = defaultdict(int)
        for stone, count in stones.items():
            for child in stone_logic(stone):
                new_stones[child] += count
        
        stones = new_stones
    return sum(stones.values())


@aoc_output(title="Day 11 - Splitting Stones")
def part_1(lines: List[str]) -> int:
    return stone_splitting(lines, blinks=25)
    # Leaving this here as my solution to part 1
    # stones = list(map(int, lines.split(" ")))
    # for _ in tqdm(range(blinks)):
    #     stones = list(chain(*[stone_logic(s) for s in stones]))
    # return len(stones)


@aoc_output(title="Day 11 - 3x blinks!")
def part_2(lines: List[str]) -> int:
    return stone_splitting(lines, blinks=75)


if __name__ == "__main__":
    pi = get_puzzle_input(__file__, block=True, split_lines=False)

    # Part 1
    solution_1 = part_1(pi)
    submit_solution(__file__, solution=solution_1, part='a')

    # Part 2
    solution_2 = part_2(pi)
    submit_solution(__file__, solution=solution_2, part='b')
