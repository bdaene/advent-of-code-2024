from importlib.resources import files
from typing import Any

from advent_of_code_2024.utils import timeit, setup_logging


@timeit
def get_data(input_file):
    return [tuple(map(int, line.strip().split(","))) for line in input_file]


def get_nb_steps(corrupted, size):
    steps = 0
    to_visit = [(0, 0)]
    visited = [[None for col in range(size)] for row in range(size)]
    while to_visit:
        steps += 1
        to_visit_ = []
        for row, col in to_visit:
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                row_, col_ = row + dr, col + dc
                if 0 <= row_ < size and 0 <= col_ < size:
                    if corrupted[row_][col_] or visited[row_][col_]:
                        continue
                    to_visit_.append((row_, col_))
                    visited[row_][col_] = steps
                    if row_ == size - 1 and col_ == size - 1:
                        return steps
        to_visit = to_visit_


@timeit
def part_1(data, size=70, nb_bytes=1024):
    size += 1
    corrupted = [[False for col in range(size)] for row in range(size)]
    for x, y in data[:nb_bytes]:
        corrupted[y][x] = True

    # print()
    # print("\n".join("".join("#" if cell else "." for cell in line) for line in corrupted))

    return get_nb_steps(corrupted, size)


class Obstacles:
    def __init__(self):
        self.obstacles: dict[Any, int] = {}
        self.parents: list[int] = []
        self.size: list[int] = []
        self.borders: list[Any] = []

    def add_obstacle(self, obstacle, borders):
        if obstacle in self.obstacles:
            return

        obstacle_id = len(self.obstacles)
        self.obstacles[obstacle] = obstacle_id
        self.parents.append(obstacle_id)
        self.size.append(1)
        self.borders.append(borders)

    def __contains__(self, obstacle) -> bool:
        return obstacle in self.obstacles

    def find(self, obstacle) -> int:
        obstacle_id = self.obstacles[obstacle]
        parent_id = obstacle_id
        while self.parents[parent_id] != parent_id:
            parent_id = self.parents[parent_id]
        while obstacle_id != parent_id:
            self.parents[obstacle_id], obstacle_id = parent_id, self.parents[obstacle_id]
        return parent_id

    def union(self, obstacle_a, obstacle_b):
        parent_a = self.find(obstacle_a)
        parent_b = self.find(obstacle_b)

        if parent_a == parent_b:
            return

        if self.size[parent_a] < self.size[parent_b]:
            parent_a, parent_b = parent_b, parent_a

        self.size[parent_a] += self.size[parent_b]
        self.borders[parent_a] |= self.borders[parent_b]
        self.parents[parent_b] = parent_a


@timeit
def part_2(data, size=70):
    obstacles = Obstacles()

    for x, y in data:
        obstacle = (x, y)
        borders = 0b0001 * (x == 0) + 0b0010 * (y == 0) + 0b0100 * (x == size) + 0b1000 * (y == size)
        obstacles.add_obstacle(obstacle, borders)
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                obstacle_ = (x + dx, y + dy)
                if obstacle_ in obstacles:
                    obstacles.union(obstacle, obstacle_)
        parent_borders = obstacles.borders[obstacles.find(obstacle)]
        if parent_borders & 0b1001 and parent_borders & 0b0110:
            return obstacle


def main():
    setup_logging()
    with (files("data.inputs") / "day_18.txt").open() as input_file:
        data = get_data(input_file)
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
