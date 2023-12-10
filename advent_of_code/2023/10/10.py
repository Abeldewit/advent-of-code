from dataclasses import dataclass
from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import get_puzzle_input, submit_solution

from typing import List
import numpy as np
from tqdm import tqdm

directions = {
    '|': ((-1, 0), (1, 0)),
    'L': ((-1, 0), (0, 1)),
    '-': ((0, -1), (0, 1)),
    'F': ((0, 1), (1, 0)),
    'J': ((-1, 0), (0, -1)),
    '7': ((0, -1), (1, 0)),
    '.': ((0, 0), (0, 0)),
    'S': ((-1, 0), (1, 0), (0, -1), (0, 1))
}

GRID = None


@dataclass
class Node:
    pipe_type: str
    position: tuple
    neighbors: list = None

    def __post_init__(self):
        self.neighbors = [
            tuple(v)
            for v in
            np.array(directions[self.pipe_type]) + self.position
        ]

    def __contains__(self, other):
        if not isinstance(other, Node):
            return False
        return other.position in self.neighbors

    def get_next(self, history):
        next_option = [v for v in self.neighbors if v not in history]
        if next_option:
            return next_option[0]
        else:
            return None


@aoc_output(title="Day 10 - Path walk")
def part_1(lines: List[str]) -> int:
    global GRID
    GRID = np.array([list(line) for line in lines])
    start = tuple([v[0] for v in np.where(GRID == 'S')])

    node_list = []
    for y in range(GRID.shape[0]):
        row_list = []
        for x in range(GRID.shape[1]):
            row_list.append(
                Node(pipe_type=GRID[y, x], position=(y, x))
            )
        node_list.append(row_list)
    node_list = np.array(node_list)

    def _get_node(x, y):
        return node_list[x][y]

    start_node = _get_node(*start)  # node_list[start[0]][start[1]]
    print(start_node)
    start_neighbors = start_node.neighbors

    connect_start_nodes = [
        _get_node(*n)
        for n in start_neighbors
        if start_node in _get_node(*n)
    ]

    for start_neighbor in connect_start_nodes:
        current_node = start_neighbor
        history = [start_node.position, current_node.position]
        step_count = 1
        while True:
            next_node = current_node.get_next(history)
            if next_node is None:
                if start_node in current_node:
                    return int(len(history)/2)
                break
            current_node = _get_node(*next_node)
            history.append(current_node.position)
            step_count += 1


@aoc_output(title="Day 10 - Insides")
def part_2(lines: List[str]) -> int:
    if not GRID:
        global GRID
        GRID = np.array([list(line) for line in lines])
    start = tuple([v[0] for v in np.where(GRID == 'S')])

    node_list = []
    for y in range(GRID.shape[0]):
        row_list = []
        for x in range(GRID.shape[1]):
            row_list.append(
                Node(pipe_type=GRID[y, x], position=(y, x))
            )
        node_list.append(row_list)
    node_list = np.array(node_list)

    def _get_node(x, y):
        return node_list[x][y]

    start_node = _get_node(*start)  # node_list[start[0]][start[1]]
    print(start_node)
    start_neighbors = start_node.neighbors

    connect_start_nodes = [
        _get_node(*n)
        for n in start_neighbors
        if start_node in _get_node(*n)
    ]

    current_node = connect_start_nodes[0]
    history = [start_node.position, current_node.position]
    pbar = tqdm(total=13432, desc='Walking')
    while True:
        next_node = current_node.get_next(history)
        if next_node is None:
            break
        current_node = _get_node(*next_node)
        history.append(current_node.position)
        pbar.update(1)

    # Profesionally stolen from:
    # https://stackoverflow.com/questions/36399381/whats-the-fastest-way-of-checking-if-a-point-is-inside-a-polygon-in-python
    def _ray_tracing(x, y, poly):
        n = len(poly)
        inside = False
        p2x = .0
        p2y = .0
        xints = .0
        p1x, p1y = poly[0]
        for i in range(n+1):
            p2x, p2y = poly[i % n]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                        if p1x == p2x or x <= xints:
                            inside = not inside
            p1x, p1y = p2x, p2y
        return inside

    polygon = np.array(history)
    points = []
    for y in range(GRID.shape[0]):
        for x in range(GRID.shape[1]):
            if (y, x) not in history:
                points.append((y, x))
    inside1 = [
        _ray_tracing(point[0], point[1], polygon)
        for point in tqdm(points, desc="Ray tracing")
    ]
    return sum(inside1)


if __name__ == "__main__":
    pi = get_puzzle_input(__file__, block=True)

    # Part 1
    # solution_1 = part_1(pi)
    # if (input('Submit part a (Y/N): ') == 'Y'):
    #     submit_solution(__file__, solution=solution_1, part='a')

    # Part 2
    solution_2 = part_2(pi)
    if (input('Submit part b (Y/N): ') == 'Y'):
        submit_solution(__file__, solution=solution_2, part='b')
