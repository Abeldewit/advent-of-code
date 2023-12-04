from collections import defaultdict
from functools import reduce
from typing import List

from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import get_puzzle_input


@aoc_output(title="Day 2 - Possible games")
def get_possible_games(lines: List[str]):
    def _game_is_possible(single_game: str, bag_items: dict) -> int:
        game_id, games = single_game.split(':')
        game_id = game_id.replace('Game ', '')
        games = games.split(';')

        for game in games:
            cubes = [
                cube.strip().split(' ') for cube in game.split(',')
            ]
            for cube in cubes:
                if bag_items[cube[1]] < int(cube[0]):
                    return 0
        return int(game_id)

    # 12 red cubes, 13 green cubes, and 14 blue cubes
    bag_items = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    running_sum = 0
    for game in lines:
        running_sum += _game_is_possible(game, bag_items=bag_items)
    return running_sum


@aoc_output(title="Day 2 - Game Powers")
def get_game_powers(lines: List[str]) -> int:
    running_sum = 0
    for line in lines:
        game_id, games = line.split(':')
        game_id = game_id.replace('Game ', '')
        games = games.split(';')

        minimal_bag = defaultdict(lambda: None)
        for game in games:
            cubes = [
                cube.strip().split(' ') for cube in game.split(',')
            ]
            for cube in cubes:
                if minimal_bag[cube[1]]:
                    if minimal_bag[cube[1]] < int(cube[0]):
                        minimal_bag[cube[1]] = int(cube[0])
                else:
                    minimal_bag[cube[1]] = int(cube[0])
        power = reduce(lambda x, y: x*y, minimal_bag.values())
        running_sum += power
    return running_sum


if __name__ == "__main__":
    pi = get_puzzle_input(__file__)
    get_possible_games(pi)
    get_game_powers(pi)
