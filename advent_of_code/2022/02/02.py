from pathlib import Path
from typing import Tuple

shape_dict_first_col = {
    'A': 1,  # Rock
    'B': 2,  # Paper
    'C': 3,  # Scissor
}

shape_dict_second_col = {
    'X': 1,  # Rock
    'Y': 2,  # Paper
    'Z': 3,  # Scissor
}

win_matrix = [
    [3, 6, 0],
    [0, 3, 6],
    [6, 0, 3]
]

outcome_dict = {
    'Lose': 0,
    'Draw': 3,
    'Win': 6
}

def calculate_match(opponent: str, yourself: str) -> Tuple[int, int]:
    op_num = shape_dict_first_col[opponent]
    my_num = shape_dict_second_col[yourself]
    
    outcome = win_matrix[op_num-1][my_num-1]
    return outcome, my_num

outcome_strategy = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

def calculate_move(opponent: str, outcome: str) -> Tuple[int, int]:
    op_num = shape_dict_first_col[opponent]
    my_num = win_matrix[op_num-1].index(outcome_strategy[outcome]) + 1

    return outcome_strategy[outcome], my_num

if __name__ == "__main__":
    this_folder = Path(__file__).parent
    with open(this_folder.joinpath('puzzle_input.txt'), 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    scores = []
    for line in lines:
        outcome, my_move = calculate_match(line.split()[0], line.split()[1])
        scores.append(outcome + my_move)
        
    print("Total score", sum(scores))
    print('-- Part 2 --')
    second_scores = []
    for line in lines:
        outcome, my_move = calculate_move(line.split()[0], line.split()[1])
        second_scores.append(outcome + my_move)
        
    print("Total score", sum(second_scores))
    