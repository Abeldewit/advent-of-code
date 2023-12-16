import string
from collections import defaultdict

from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import get_puzzle_input


@aoc_output("Day 3 - Part Numbers")
def get_part_numbers_sum(lines: list[str]) -> int:
    schema_height = len(lines) - 1
    schema_length = len(lines[0]) - 1

    def _get_nearest_symbols(
        self_x: int,
        self_y: int,
        self_l: int
    ) -> set[str]:
        x_0 = max(0, self_x - self_l)
        y_0 = max(0, self_y - 1)
        x_1 = min(schema_length, self_x + 1)
        y_1 = min(schema_height, self_y + 1)

        return set(
            lines[y_0][x_0:x_1 + 1] +
            lines[self_y][x_0:x_1 + 1] +
            lines[y_1][x_0:x_1 + 1]
        )

    special_characters = set([
        char for char in string.punctuation
        if char != '.'
    ])

    running_sum = 0
    for y, line in enumerate(lines):
        running_number = ''
        for x, char in enumerate(line):
            if char.isdigit():
                running_number += char
                if x == schema_length or not line[x+1].isdigit():
                    nearest_symbols = _get_nearest_symbols(
                        self_x=x, self_y=y, self_l=len(running_number)
                    )

                    if special_characters.intersection(nearest_symbols):
                        running_sum += int(running_number)

                    running_number = ''
    return running_sum


@aoc_output(title="Day 3 - Gear Ratio Sum")
def get_gear_ratio_sum(lines: list[str]) -> int:
    schema_height = len(lines) - 1
    schema_length = len(lines[0]) - 1

    def _find_gear_positions(
        self_x: int,
        self_y: int,
        self_l: int
    ) -> set[tuple[int, int]]:
        x_0 = max(0, self_x - self_l)
        y_0 = max(0, self_y - 1)
        x_1 = min(schema_length, self_x + 2)
        y_1 = min(schema_height, self_y + 2)

        return {
            (y, x) for y in range(y_0, y_1)
            for x in range(x_0, x_1) if lines[y][x] == "*"
        }

    gear_pos_num_map = defaultdict(list)

    for y, line in enumerate(lines):
        number_chunk = ""
        for x, char in enumerate(line):
            if char.isdigit():
                number_chunk += char

                if x == schema_length or not line[x + 1].isdigit():
                    for position in _find_gear_positions(
                        x, y, len(number_chunk)
                    ):
                        gear_pos_num_map[position].append(int(number_chunk))

                    number_chunk = ""

    return sum((v[0] * v[1] for v in gear_pos_num_map.values() if len(v) == 2))


if __name__ == "__main__":
    pi = get_puzzle_input(__file__)
    get_part_numbers_sum(pi)
    get_gear_ratio_sum(pi)
