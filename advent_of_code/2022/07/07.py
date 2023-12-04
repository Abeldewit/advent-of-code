from pathlib import Path
from collections import defaultdict
from functools import reduce
import operator

puzzle_input = Path(__file__).parent.joinpath('puzzle_input.txt')
with open(puzzle_input, 'r') as f:
    lines = [line.strip() for line in f.readlines()]


infinit_defaultdict = lambda: defaultdict(infinit_defaultdict)
# file_system = infinit_defaultdict()


def get_from_dict(data_dict, mapping):
    return reduce(operator.getitem, mapping, data_dict)

def set_in_dict(data_dict, mapping, value):
    if isinstance(get_from_dict(data_dict, mapping[:-1])[mapping[-1]], defaultdict):
        get_from_dict(data_dict, mapping[:-1])[mapping[-1]] = value
    else:
        get_from_dict(data_dict, mapping[:-1])[mapping[-1]] += value
    
file_system = []
current_directory = None
for line in lines:
    if line.startswith('$'):
        if 'cd' in line:
            change_directory_to = line.split()[2]
            if change_directory_to == '..':
                current_directory.pop()
            elif change_directory_to == '/':
                current_directory = ['/']
            else:
                current_directory.append(change_directory_to)
    else:
        # Reading ls output
        if line.startswith('dir'):
            pass
            # set_in_dict(file_system, current_directory, 0)
            # file_system.append((current_directory + [line.split()[1]], None))
        else:
            file_system.append(
                ('/'.join(current_directory[1:] + [line.split()[1]]), line.split()[0])
            )
            # set_in_dict(
            #     data_dict=file_system,
            #     mapping=current_directory + [line.split()[1]],
            #     value=line.split()[0]
            # )
            # file_system.append((current_directory, (line.split())))
            

print('done scanning')

def calculate_dir_size(dir_list):
    files_in_dir = [int(file[1]) for file in dir_list if len(file[0].split('/')) == 1]
    dirs_in_dir = set([file[0].split('/')[0] for file in dir_list if len(file[0].split('/')) > 1])
    
    folders = []
    for folder in dirs_in_dir:
        print(folder)
        folders.append(
            calculate_dir_size([
                (f[0].replace(folder+'/', ''), f[1]) for f in dir_list if f[0].startswith(folder)])
        )
    
    file_sum = sum(files_in_dir) + sum(folders)
    print(dir_list)
    return file_sum


calculate_dir_size(file_system)