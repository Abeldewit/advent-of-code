from pathlib import Path
import string

char_scores = {
    char: score
    for score, char in
    enumerate(list(string.ascii_lowercase) + list(string.ascii_uppercase), start=1)
}

puzzle_input = Path(__file__).parent.joinpath('puzzle_input.txt')
with open(puzzle_input, 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    
rucksack_containers = [
    (set(rucksack[:int(len(rucksack)/2)]), set(rucksack[int(len(rucksack)/2):]))
    for rucksack in lines
]

common_container_items = [
    list(container[0].intersection(container[1]))[0]
    for container in rucksack_containers
]

print("Answer:", sum([char_scores[v] for v in common_container_items]))

rucksack_groups = [
    [
        set(rucksack) 
        for rucksack in
        lines[i:i+3]
    ]
    for i in range(0, len(lines), 3)
]

rucksack_group_bages = [list(r[0].intersection(r[1]).intersection(r[2]))[0] for r in rucksack_groups]
rucksack_group_prios = [char_scores[badge] for badge in rucksack_group_bages]

    
print("Answer", sum(rucksack_group_prios))