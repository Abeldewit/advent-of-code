from pathlib import Path


def get_puzzle_input(python_file_path: str):
    puzzle_input = Path(python_file_path).parent.joinpath('puzzle_input.txt')
    with open(puzzle_input, 'r') as f:
        return [line.strip() for line in f.readlines()]