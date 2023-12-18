
from dataclasses import dataclass
from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import get_puzzle_input, submit_solution

from typing import List, Tuple
import numpy as np
from shapely import Polygon, Point as P


@dataclass
class Point:
    pos: np.ndarray
    color: str


# 0 means R, 1 means D, 2 means L, and 3 means U
directions = {
    'R': np.array((0, 1)),
    'D': np.array((1, 0)),
    'L': np.array((0, -1)),
    'U': np.array((-1, 0)),
}


@aoc_output(title="Day 18 - Lava Trench")
def part_1(lines: List[str]) -> int:
    start = np.array((0, 0))

    start_point = Point(start, None)
    all_points = [start_point]

    current_pos = start
    for p in lines:
        d, dist, color = p.split()
        current_pos += directions[d] * int(dist)
        _new_point = Point(current_pos.copy(), color)
        all_points.append(_new_point)

    trench_length = np.sum([np.sum(np.abs((p1.pos - p2.pos))) for p1, p2 in zip(all_points, all_points[1:]+[all_points[0]])])
    min_x = min([p.pos[0] for p in all_points])
    max_x = max([p.pos[0] for p in all_points])
    min_y = min([p.pos[1] for p in all_points])
    max_y = max([p.pos[1] for p in all_points])

    geom = Polygon([P(p.pos) for p in all_points])
    interiors = np.sum(
        np.apply_along_axis(
            lambda x: geom.contains(P(x)),
            axis=0,
            arr=np.mgrid[min_x:max_x+1, min_y:max_y+1]
            )
    )
    return trench_length + interiors


@aoc_output(title="Day - ")
def part_2(lines: List[str]) -> int:
    start = np.array((0, 0))

    start_point = Point(start, None)
    all_points = [start_point]

    def _convert_hex(hex_string) -> Tuple[int, np.ndarray]:
        
        dist_hex, dir_hex = hex_string[1:-1], int(hex_string[-1])
        return (int(dist_hex, 16), list(directions.keys())[dir_hex])

    current_pos = start
    for p in lines:
        _, _, color = p.split()
        dist, d = _convert_hex(color[1:-1])
        current_pos += directions[d] * int(dist)
        _new_point = Point(current_pos.copy(), color)
        all_points.append(_new_point)

    trench_length = np.sum([np.sum(np.abs((p1.pos - p2.pos))) for p1, p2 in zip(all_points, all_points[1:]+[all_points[0]])])
    min_x = min([p.pos[0] for p in all_points])
    max_x = max([p.pos[0] for p in all_points])
    min_y = min([p.pos[1] for p in all_points])
    max_y = max([p.pos[1] for p in all_points])

    geom = Polygon([P(p.pos) for p in all_points])
    interiors = np.sum(
        np.apply_along_axis(
            lambda x: geom.contains(P(x)),
            axis=0,
            arr=np.mgrid[min_x:max_x+1, min_y:max_y+1]
            )
    )
    return trench_length + interiors


if __name__ == "__main__":
    pi = get_puzzle_input(__file__, block=True)

    # Part 1
    # solution_1 = part_1(pi)
    # submit_solution(__file__, solution=solution_1, part='a')

    # Part 2
    solution_2 = part_2(pi)
    # submit_solution(__file__, solution=solution_2, part='b')
