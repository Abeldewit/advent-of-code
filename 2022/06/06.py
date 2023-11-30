from pathlib import Path
puzzle_input = Path(__file__).parent.joinpath('puzzle_input.txt')
with open(puzzle_input, 'r') as f:
    lines = [line.strip() for line in f.readlines()]

line = lines[0]

def finder(comm_line, distinct=4):
    for idx in range(distinct, len(comm_line)):
        window = comm_line[idx-distinct:idx]
        if len(set(window)) == distinct:
            print(f"Marker found at idx {idx}")
            return idx
        
print(finder(line, 4))
print(finder(line, 14))