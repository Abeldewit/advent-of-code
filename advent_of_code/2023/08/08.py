from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import get_puzzle_input

from typing import Callable, Dict, Iterable, List, Tuple
import re
import numpy as np
import math


def _instr_gen(instructions):
    idx = -1
    while True:
        if idx == len(instructions)-1:
            idx = -1
        idx += 1
        yield instructions[idx]


def find_node_steps(
    start_node: str, node_dict: Dict[str, Tuple[str, str]],
    instructions: Iterable[int], end_condition: Callable
):
    current_node = start_node
    instruct = _instr_gen(instructions)
    step_counter = 0
    while end_condition(current_node):
        left_or_right = next(instruct)
        new_node = node_dict[current_node][left_or_right]
        current_node = new_node
        step_counter += 1
    return step_counter


def create_node_dict(lines: List[str]):
    node_dict = {}
    for line in lines:
        node_dict.update({
            re.search(r'(\w{3}) =', line).group(1):
            re.findall(r'\((\w{3}), (\w{3})\)', line)[0]
        })
    return node_dict


@aoc_output(title="Day 8 - Node steps")
def find_single_node_steps(lines: List[str]) -> int:
    instruct_pattern = lines[0]
    binary_instr = list(
        np.where(np.array(list(instruct_pattern)) == 'R', 1, 0)
    )

    start_node = 'AAA'
    node_dict = create_node_dict(lines[2:])

    return find_node_steps(
        start_node=start_node,
        node_dict=node_dict,
        instructions=binary_instr,
        end_condition=lambda x: x != 'ZZZ'
    )


@aoc_output(title="Day 8 - Ghost Nodes")
def find_ghost_nodes(lines: List[str]) -> int:
    instruct_pattern = lines[0]
    binary_instr = list(
        np.where(np.array(list(instruct_pattern)) == 'R', 1, 0)
    )

    node_dict = create_node_dict(lines[2:])
    start_nodes = [
        node for node in node_dict.keys()
        if node.endswith('A')
    ]

    step_per_node = [
        find_node_steps(
            start_node=node, 
            node_dict=node_dict,
            instructions=binary_instr,
            end_condition=lambda x: not x.endswith('Z')
        )
        for node in start_nodes
    ]

    return math.lcm(*step_per_node)


if __name__ == "__main__":
    pi = get_puzzle_input(__file__, block=True)

    # Part 1
    solution_1 = find_single_node_steps(pi)

    # Part 2
    solution_2 = find_ghost_nodes(pi)
