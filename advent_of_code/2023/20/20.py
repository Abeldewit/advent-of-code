from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import get_puzzle_input, submit_solution

from typing import List
from dataclasses import dataclass, field
from collections import deque


PROCESS_QUEUE = deque()


@dataclass
class Module:
    name: str
    mod_type: str
    dest: List['Module'] = field(default_factory=list)
    state: int = 0
    memory: List['Module'] = field(default_factory=dict)
    low_count: int = 0
    high_count: int = 0

    def receive_pulse(self, pulse: int, source: str):
        global PROCESS_QUEUE
        print(f"{source} -{'high' if pulse else 'low'}-> {self.name}")

        if self.mod_type == '%':
            # If a flip-flop module receives a high pulse, it is ignored
            # and nothing happens.
            # However, if a flip-flop module receives a low pulse, it flips
            # between on and off.
            # If it was off, it turns on and sends a high pulse.
            # If it was on, it turns off and sends a low pulse.
            if pulse == 0:
                self.state = (self.state+1) % 2
                self.send_to_dest(self.state)
                return
        elif self.mod_type == '&':
            # When a pulse is received, the conjunction module first updates
            # its memory for that input.
            # Then, if it remembers high pulses for all inputs, it sends a low
            # pulse; otherwise, it sends a high pulse.
            if source in self.memory:
                # Update memory
                self.memory[source] = pulse
                if all(v == 1 for v in self.memory.values()):
                    self.send_to_dest(0)
                    return
                self.send_to_dest(1)
                return
            else:
                raise ValueError("Input not in memory")
        elif self.mod_type == 'b':
            # When it receives a pulse, it sends the same pulse to all of its
            # destination modules.
            self.send_to_dest(pulse)
            return

    def send_to_dest(self, new_pulse: int):
        global PROCESS_QUEUE
        for mod in self.dest:
            if new_pulse == 0:
                self.low_count += 1
            if new_pulse == 1:
                self.high_count += 1

            PROCESS_QUEUE.appendleft((mod, new_pulse, self.name))
            # mod.receive_pulse(new_pulse, source=self.name)


def setup_modules(lines: List[str]):
    module_dict = {}
    conjunctions = []
    for line in lines:
        mod_type = line[0]
        mod_name, destinations = line.split(' -> ')
        if mod_name != 'broadcaster':
            mod_name = mod_name[1:]
        else:
            mod_type = 'b'
        destinations = [d.strip() for d in destinations.split(',')]
        _new_module = Module(name=mod_name, mod_type=mod_type)
        module_dict[mod_name] = (_new_module, destinations)
        if mod_type == '&':
            conjunctions.append(_new_module)

    for module, destinations in module_dict.values():
        for d in destinations:
            if d in module_dict.keys():
                module.dest.append(module_dict[d][0])

                if module_dict[d][0] in conjunctions:
                    module_dict[d][0].memory[module.name] = 0
            else:
                module.dest.append(Module(name=d, mod_type='OUTPUT'))
    return {k: v[0] for k, v in module_dict.items()}


@aoc_output(title="Day - ")
def part_1(lines: List[str]) -> int:
    global PROCESS_QUEUE
    module_dict = setup_modules(lines)
    # Now we start pushing the button repeatedly
    for i in range(1000):
        print(f"--- Button press {i+1} --- ")
        module_dict['broadcaster'].receive_pulse(0, source='button')
        while PROCESS_QUEUE:
            next_step = PROCESS_QUEUE.pop()
            next_step[0].receive_pulse(next_step[1], next_step[2])

    # 1000 extra for the 'input button'
    lc = sum([m.low_count for m in module_dict.values()]) + 1000
    hc = sum([m.high_count for m in module_dict.values()])
    return lc * hc


@aoc_output(title="Day - ")
def part_2(lines: List[str]) -> int:
    return 0


if __name__ == "__main__":
    pi = get_puzzle_input(__file__, block=True)

    # Part 1
    solution_1 = part_1(pi)
    submit_solution(__file__, solution=solution_1, part='a')

    # Part 2
    # solution_2 = part_2(pi)
    # submit_solution(__file__, solution=solution_2, part='b')
