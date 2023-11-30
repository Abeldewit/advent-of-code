from pathlib import Path
from collections import defaultdict
from itertools import islice

puzzle_input = Path(__file__).parent.joinpath('puzzle_input.txt')
with open(puzzle_input, 'r') as f:
    lines = [line for line in f.readlines()]

def window_iter(seq, window=4):
    seq_len = len(seq)
    for idx in range(0, seq_len, window):
        crate_place = seq[idx:idx+window].strip()
        if not crate_place:
            yield None
        else:
            yield crate_place[1:-1]

def create_crate_stacks(): 
    crate_dict = defaultdict(list)
    for row in crate_config[::-1][1:]:
        crates = window_iter(row)
        for column, crate in enumerate(crates, start=1):
            if crate:
                crate_dict[column].append(crate)
    return crate_dict

#** Moving crates **#
def move_crates_9000(stacks, from_stack, to_stack, amount):
    for _ in range(amount):
        stacks[to_stack].append(
            stacks[from_stack].pop()
        )
        
def move_crates_9001(stacks, from_stack, to_stack, amount):
    picked_crates = stacks[from_stack][-amount:]
    stacks[from_stack] = stacks[from_stack][:-amount]
    stacks[to_stack].extend(picked_crates)

def parse_moves(move_lines):
    return [
        (
            int(line.split()[3].strip()),
            int(line.split()[5].strip()),
            int(line.split()[1].strip()),
        )
        for line in move_lines
    ]
    
#** Get top crates **#
def get_top_crates(stacks):
    stack_nums, crates = '', ''
    for k, v in stacks.items():
        stack_nums += str(k)
        crates += v[-1]
    print(crates)
    print(stack_nums)
    
def print_stacks_nice(stacks):
    max_height = max([len(v) for v in stacks.values()])
    stack_strings = ['' for _ in range(max_height)]
    for idx in range(max_height):
        for k, v in stacks.items():
            if len(v) > idx:
                stack_strings[idx] += f'[{v[idx]}] '
            else:
                stack_strings[idx] += '    '
    
    for ststr in stack_strings[::-1]:
        print(ststr)
    
    
# Part 1 #
crate_config_lines = [i for i, line in enumerate(lines) if not line.startswith('move')]
crate_config_start = min(crate_config_lines)
crate_config_end = max(crate_config_lines)
crate_config = lines[crate_config_start:crate_config_end]

# crate_stacks = create_crate_stacks()
# move_lines = lines[crate_config_end+1:]
# moves = parse_moves(move_lines)
# for move in moves:
#     move_crates_9000(crate_stacks, *move)
# get_top_crates(crate_stacks)

crate_stacks = create_crate_stacks()
move_lines = lines[crate_config_end+1:]
moves = parse_moves(move_lines)

print_stacks_nice(crate_stacks)
print()
for move in moves:
    move_crates_9001(crate_stacks, *move)
    print_stacks_nice(crate_stacks)
    print(f"Move {move[2]} from {move[0]} to {move[1]}")
get_top_crates(crate_stacks)

            
print('done')