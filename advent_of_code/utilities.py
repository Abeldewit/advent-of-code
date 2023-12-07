from pathlib import Path
from aocd import get_data, submit
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
    # Retrieve the current folder and corresponding year and day
    puzzle_folder = Path(python_file_path).parent
    year, day = map(int, str(puzzle_folder).split('/')[-2:])
    
    # If the input already exists, we don't have to retrieve it from the site
    if puzzle_folder.joinpath('puzzle_input.txt').exists():
        puzzle_data = get_puzzle_input_from_file(python_file_path)
    else:
        # Otherwise we use the aocd package to retrieve the P.I.
        try:
            puzzle_data = get_data(
                day=day, year=year, block=block
            )
        except PuzzleLockedError as ple:
            return str(ple)
    
    # Possibly save the file so we don't have to make requests every run
    if save_to_file:
        with open(puzzle_folder.joinpath('puzzle_input.txt'), 'w') as puzzle_file:
            puzzle_file.write(puzzle_data)
    
    # For most exercises it's nice to split the input, but it can be omitted
    if split_lines:
        return [line.strip() for line in puzzle_data.split('\n')]
    return puzzle_data

def submit_solution(python_file_path: str, solution, part: str = None):
    # Retrieve the current folder and corresponding year and day
    puzzle_folder = Path(python_file_path).parent
    year, day = map(int, str(puzzle_folder).split('/')[-2:])
    
    submit(
        answer=solution,
        year=year,
        day=day,
        part=part
    )
