from pathlib import Path
puzzle_input = Path(__file__).parent.joinpath('puzzle_input.txt')
with open(puzzle_input, 'r') as f:
    lines = [line.strip() for line in f.readlines()]

contain_counter = 0
overlap_counter = 0
for line in lines:
    bounds = [
        set(
            range(
                int(side.split('-')[0]),
                int(side.split('-')[1]) + 1
            )
        )
        for side in line.split(',')
    ]
    l_bounds = bounds[0] - bounds[1]
    r_bounds = bounds[1] - bounds[0]
    
    if not l_bounds or not r_bounds:
        contain_counter += 1
        
    if bounds[0].intersection(bounds[1]):
        overlap_counter += 1
        
print(contain_counter)
print(overlap_counter)