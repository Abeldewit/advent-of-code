from pathlib import Path
from collections import defaultdict
from functools import reduce

puzzle_input = Path(__file__).parent.joinpath('puzzle_input.txt')
with open(puzzle_input, 'r') as f:
    lines = [line.strip() for line in f.readlines()]

# 12 red cubes, 13 green cubes, and 14 blue cubes
bag_items = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def game_is_possible(single_game: str, bag_items: dict) -> int:
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


def get_game_power(single_game: str) -> int:
    game_id, games = single_game.split(':')
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
    return reduce(lambda x,y: x*y, minimal_bag.values())


possible_game_ids = list(
    map(lambda x: game_is_possible(single_game=x, bag_items=bag_items), lines)
)
print(f"Number of possible games: {sum(possible_game_ids)}")

game_powers = list(
    map(get_game_power, lines)
)
print(f"Sum of game powers: {sum(game_powers)}")