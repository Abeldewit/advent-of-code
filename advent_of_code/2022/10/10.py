from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import get_puzzle_input

from typing import List


@aoc_output(title="Day 10 - Signal Strength")
def get_singal_strength(lines: List[str]) -> int:
    idx = -1
    cycle_counter = 0
    cycles_to_go = 0
    register_history = [1]
    to_be_registered = None
    
    total_signal_strength = 0
    
    for new_line in lines:
        # At the start of the cycle, an instruction begins execution
        if 'addx' in new_line:
            to_be_registered = int(new_line.split()[1])
            cycles_to_go = 2
        elif 'noop' in new_line:
            cycles_to_go = 1
        
        for _ in range(cycles_to_go):
            cycle_counter += 1
            if (cycle_counter-20) %40 ==0:
                total_signal_strength += (
                    cycle_counter * sum(register_history)
                )
        if to_be_registered:
            register_history += [to_be_registered]
            to_be_registered = None

    return total_signal_strength
        


@aoc_output(title="Day 10 - CRT Screen")
def get_crt_image(lines: List[str]) -> int:
    cycle_counter = 1
    cycles_to_go = 0
    register_history = [1]
    to_be_registered = None
    
    crt_rows = [[' ']*40 for _ in range(6)]
    for new_line in lines:
        # At the start of the cycle, an instruction begins execution
        if 'addx' in new_line:
            to_be_registered = int(new_line.split()[1])
            cycles_to_go = 2
        elif 'noop' in new_line:
            cycles_to_go = 1
        # print(f"Start cycle {cycle_counter}: begin executing {new_line}")
        
        for i in range(cycles_to_go):
            pixel_pos = (cycle_counter-1) % 40
            # print(f"During cycle {cycle_counter}: CRT Draws pixel in position {pixel_pos}")
            sprite_pos = (sum(register_history)-1, sum(register_history)+1)
            if sprite_pos[0] <= pixel_pos <= sprite_pos[1]:
                crt_rows[cycle_counter//40][pixel_pos] = '#'
            # print(f"Current CRT row: {''.join(crt_rows[cycle_counter//40])}")
            cycle_counter += 1
            
        if to_be_registered:
            register_history += [to_be_registered]
            # print(f"End of cycle {cycle_counter}: finish executing addx {to_be_registered} (Register X is now {sum(register_history)})")
            to_be_registered = None

    letter_crt = '\n'.join([''.join(row) for row in crt_rows])

    return '\n' + letter_crt


if __name__ == "__main__":
    pi = get_puzzle_input(__file__)
    get_singal_strength(pi)
    get_crt_image(pi)