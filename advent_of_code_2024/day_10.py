from collections import defaultdict
from importlib.resources import files

from advent_of_code_2024.utils import timeit, setup_logging


@timeit
def get_data(input_file):
    return [list(map(int, line.strip())) for line in input_file]


def get_score(grid, head):
    assert grid[head[0]][head[1]] == 0
    m, n = len(grid), len(grid[0])
    to_visit = {head}
    for height in range(1, 10):
        to_visit_ = set()
        for row, col in to_visit:
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                row_, col_ = row + dr, col + dc
                if 0 <= row_ < m and 0 <= col_ < n and grid[row_][col_] == height:
                    to_visit_.add((row_, col_))
        to_visit = to_visit_
    return len(to_visit)


@timeit
def part_1(data):
    total = 0
    for row, line in enumerate(data):
        for col, cell in enumerate(line):
            if cell == 0:
                total += get_score(data, (row, col))

    return total


def get_rating(grid, head):
    assert grid[head[0]][head[1]] == 0
    m, n = len(grid), len(grid[0])
    to_visit = {head: 1}
    for height in range(1, 10):
        to_visit_ = defaultdict(int)
        for (row, col), rating in to_visit.items():
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                row_, col_ = row + dr, col + dc
                if 0 <= row_ < m and 0 <= col_ < n and grid[row_][col_] == height:
                    to_visit_[(row_, col_)] += rating
        to_visit = to_visit_
    return sum(to_visit.values())

@timeit
def part_2(data):
    total = 0
    for row, line in enumerate(data):
        for col, cell in enumerate(line):
            if cell == 0:
                total += get_rating(data, (row, col))

    return total


def main():
    setup_logging()
    with (files("data.inputs") / "day_10.txt").open() as input_file:
        data = get_data(input_file)
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
