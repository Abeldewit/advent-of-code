from pathlib import Path
from collections import defaultdict

if __name__ == "__main__":
    this_folder = Path(__file__).parent
    with open(this_folder.joinpath('puzzle_input.txt'), 'r') as f:
        lines = f.readlines()
        
    clean_lines = [l.strip() for l in lines]
    elf_dict = defaultdict(list)
    elf_num = 0
    for elf_calories in clean_lines:
        if elf_calories == '':
            elf_num += 1
            continue
        elf_dict[elf_num].append(int(elf_calories))
        
    elf_sums = {
        elf: sum(values) for elf, values in elf_dict.items()
    }
    
    sorted_elves = sorted(elf_sums.items(), key=lambda x: x[1], reverse=True)
    top_1_elf = sorted_elves[0]
    top_3_elves = sorted_elves[:3]
    top_3_elves_sum = sum([elf[1] for elf in top_3_elves])
    
    print('done')
    
    
    
    