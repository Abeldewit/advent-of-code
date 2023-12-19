from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import get_puzzle_input, submit_solution

from typing import List
from dataclasses import dataclass
from collections import namedtuple
import re


def parse_rule_to_fn(rule: str):
    rule_name, rule_logic, _ = re.split(r'[\{\}]', rule)
    logic_parts = rule_logic.split(',')
    
    functions = []
    for part in logic_parts[:-1]:
        attribute, operator, condition, result = re.match(r'(\w+)([\>\<])(\d+)\:(\w+)', part).groups()
        functions.append(
            f"'{result}' if part['{attribute}'] {operator} {condition}"
        )
    # Creating functions from strings with eval 😭
    return rule_name.strip(), eval("lambda part: " + " else ".join(functions) + f" else '{logic_parts[-1]}'")


@aoc_output(title="Day 19 - Aplenty")
def part_1(lines: List[str]) -> int:
    rules, parts = (l.split('\n') for l in lines.split('\n\n'))
    parts = [
        {k: int(v) for k, v in dict(re.findall(r'(\w)\=(\d+)', p)).items()}
        for p in parts
    ]
    rules = dict([
        parse_rule_to_fn(r)
        for r in rules
    ])
    
    total_part_sum = 0
    for part in parts:
        result = 'in'
        while result not in ('A', 'R'):
            result = rules[result](part)
        if result == 'A':
            part_sum = sum(part.values())
            total_part_sum += part_sum
    return total_part_sum


@aoc_output(title="Day - ")
def part_2(lines: List[str]) -> int:
    return 0


if __name__ == "__main__":
    pi = get_puzzle_input(__file__, block=True, split_lines=False)

    # Part 1
    solution_1 = part_1(pi)
    submit_solution(__file__, solution=solution_1, part='a')
    
    # Part 2
    solution_2 = part_2(pi)
    # submit_solution(__file__, solution=solution_2, part='b')
