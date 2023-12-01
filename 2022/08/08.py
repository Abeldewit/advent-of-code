from pathlib import Path
import numpy as np

with open(Path(__file__).parent.joinpath('puzzle_input.txt'), 'r') as f:
    lines = f.readlines()

boom_grid = np.array([list(l.strip()) for l in lines]).astype(int)
skirt_count = np.sum((boom_grid.shape, boom_grid.shape)) - 4


def is_visible(grid, x, y):
    self_height = grid[x, y]

    horizontal = grid[x, :]
    vertical = grid[:, y]
    
    left = horizontal[:y]
    right = horizontal[y+1:]
    top = vertical[:x]
    bottom = vertical[x+1:]

    vis_top = len(np.where(top >= self_height)[0]) == 0
    vis_bottom = len(np.where(bottom >= self_height)[0]) == 0
    vis_left = len(np.where(left >= self_height)[0]) == 0
    vis_right = len(np.where(right >= self_height)[0]) == 0

    visible = any((vis_left, vis_right, vis_top, vis_bottom))
    if visible:
        return 1
    return 0


def scenic_score(grid, x, y):
    self_height = grid[x, y]

    horizontal = grid[x, :]
    vertical = grid[:, y]

    left = horizontal[:y]
    right = horizontal[y+1:]
    top = vertical[:x]
    bottom = vertical[x+1:]

    scores = []
    for direction in (left[::-1], right, top[::-1], bottom):
        dir_score = 0
        for tree in direction:
            if tree < self_height:
                dir_score += 1
                continue
            break
        if dir_score == 0:
            dir_score = 1
        scores.append(dir_score)
    print(f"x:{x}, y:{y}, score: {np.product(scores)}")
    return np.product(scores)


visible_count = 0
for y in range(1, boom_grid.shape[1]-1):
    for x in range(1, boom_grid.shape[0]-1):
        visible_count += is_visible(boom_grid, y, x)
        scenic_score(boom_grid, y, x)
        
print(f"Edges: {skirt_count}, High trees: {visible_count}\tTotal: {skirt_count+visible_count}")

