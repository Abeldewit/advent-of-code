from collections import defaultdict
from copy import copy
import numpy as np
from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import get_puzzle_input

from typing import Callable, List
import re

@aoc_output(title="Day - ")
def part_1(lines: str) -> int:
    monkey_list = [
        [
            part.strip() 
            for part in line.split('\n')]
        for line in lines.split('\n\n')
    ]
    
    def _make_operation(operation: str):
        return lambda old: eval(
            operation
            .replace('new = ', '')
            .replace('old', '{old}')
            .format(old=old)
        )

    def _make_throw_func(test, true_throw, false_throw):
        return lambda x: (
            true_throw
            if x % test == 0
            else false_throw
        )

    monkey_hands = {}
    monkey_funcs = {}
    monkey_counter = defaultdict(lambda: 0)
    # Set up of the monkeys
    for monkey in monkey_list:
        number = int(monkey[0].split()[-1].replace(':', ''))
        start_items = list(map(int, re.findall(r'\d+', monkey[1])))
        operation = monkey[2].replace("Operation: ", '')
        test = int(re.search(r'divisible by (\d+)', monkey[3]).group(1))
        true_throw = int(
            re.search(r'throw to monkey (\d+)', monkey[4]).group(1)
        )
        false_throw = int(
            re.search(r'throw to monkey (\d+)', monkey[5]).group(1)
        )

        ops_func = _make_operation(operation)
        throw_func = _make_throw_func(test, true_throw, false_throw)

        monkey_hands[number] = start_items
        monkey_funcs[number] = {
            'inspect': ops_func,
            'throw': throw_func
        }

    for round_num in range(20):
        for (this_monkey, hands), funcs in zip(
            monkey_hands.items(),
            monkey_funcs.values()
        ):
            for wl in hands:
                worry_level = int(
                    np.floor(
                        funcs['inspect'](wl) / 3
                    )
                )
                monkey_counter[this_monkey] += 1
                throw_monkey = funcs['throw'](worry_level)

                monkey_hands[throw_monkey] += [worry_level]
                monkey_hands[this_monkey] = monkey_hands[this_monkey][1:]
                pass

    monkey_business = np.prod(sorted(monkey_counter.values())[-2:])
    return monkey_business


@aoc_output(title="Day - ")
def part_2(lines: str) -> int:
    pass



if __name__ == "__main__":
    pi = get_puzzle_input(__file__, single_line=True)
    part_1(pi)
    part_2(pi)
