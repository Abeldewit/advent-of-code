from pathlib import Path
from aocd import get_data
from aocd.exceptions import PuzzleLockedError


def get_puzzle_input_from_file(python_file_path: str):
    puzzle_input = Path(python_file_path).parent.joinpath('puzzle_input.txt')
    with open(puzzle_input, 'r') as f:
        return f.read()
    
def get_puzzle_input(
    python_file_path: str,
    split_lines: bool = True,
    block: bool = False,
    save_to_file: bool = True
):
    puzzle_folder = Path(python_file_path).parent
    year, day = map(int, str(puzzle_folder).split('/')[-2:])
    
    if puzzle_folder.joinpath('puzzle_input.txt').exists():
        puzzle_data = get_puzzle_input_from_file(python_file_path)
    else:
        try:
            puzzle_data = get_data(
                day=day, year=year, block=block
            )
        except PuzzleLockedError as ple:
            return str(ple)
    
    if save_to_file:
        with open(puzzle_folder.joinpath('puzzle_input.txt'), 'w') as puzzle_file:
            puzzle_file.write(puzzle_data)
    
    if split_lines:
        return [line.strip() for line in puzzle_data.split('\n')]
    return puzzle_data
    
    


if __name__ == "__main__":
    get_puzzle_input_auto('2023', '06')
