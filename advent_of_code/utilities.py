from loguru import logger
from pathlib import Path
import re
from typing import List, Literal, Union
from aocd import get_data, submit
from aocd.exceptions import PuzzleLockedError
import numpy as np


def get_puzzle_input_from_file(python_file_path: str):
    puzzle_input = Path(python_file_path).parent.joinpath("puzzle_input.txt")
    with open(puzzle_input, "r") as f:
        return f.read()


def get_puzzle_input(
    python_file_path: str,
    block: bool = False,
    save_to_file: bool = True,
) -> str:
    # Retrieve the current folder and corresponding year and day
    puzzle_folder = Path(python_file_path).parent
    year, day = map(int, str(puzzle_folder).split("/")[-2:])

    # If the input already exists, we don't have to retrieve it from the site
    if puzzle_folder.joinpath("puzzle_input.txt").exists():
        logger.info("Puzzle data already present.")
        puzzle_data = get_puzzle_input_from_file(python_file_path)
    else:
        # Otherwise we use the aocd package to retrieve the P.I.
        try:
            logger.info("Retrieving puzzle input from AOC")
            puzzle_data = get_data(day=day, year=year, block=block)
        except PuzzleLockedError as ple:
            logger.error(ple)
            return str(ple)

    # Possibly save the file so we don't have to make requests every run
    if save_to_file:
        with open(puzzle_folder.joinpath("puzzle_input.txt"), "w") as puzzle_file:
            puzzle_file.write(puzzle_data)
        logger.info("Puzzle data saved sucessfully.")
    return puzzle_data


def get_puzzle_lines(python_file_path: str, block: bool = False, save_to_file: bool = True) -> List[str]:
    puzzle_data = get_puzzle_input(python_file_path=python_file_path, block=block, save_to_file=save_to_file)
    # For most exercises it's nice to split the input, but it can be omitted
    puzzle_data = [line.strip() for line in puzzle_data.split("\n")]
    logger.info("Split puzzle input on newline [\\n]")
    return puzzle_data


def create_array_from_lines(puzzle_data: List[str]) -> np.ndarray:
    if len(set(map(len, puzzle_data))) != 1:
        logger.warning("Could not create array from this puzzle input, returning lines")
    return np.array([[float(v) for v in line.split()] for line in puzzle_data])

def convert_to_numbers(puzzle_data: Union[str, List[str]], dtype = int) -> List[Union[float, List[float]]]:
    if isinstance(puzzle_data, str):
        number_match = re.findall(r"\d+", puzzle_data)
        if number_match:
            return list(map(dtype, number_match))
    
    return [
        list(map(dtype, re.findall("\d+", line)))
        for line in puzzle_data
    ]


def submit_solution(python_file_path: str, solution, part: Union[Literal['a'], Literal['b']] = 'a'):
    # Retrieve the current folder and corresponding year and day
    puzzle_folder = Path(python_file_path).parent
    year, day = map(int, str(puzzle_folder).split("/")[-2:])

    submit(answer=solution, year=year, day=day, part=part)
