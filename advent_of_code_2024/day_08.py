from collections import defaultdict
from importlib.resources import files

from advent_of_code_2024.utils import timeit, setup_logging


@timeit
def get_data(input_file):
    return [line.strip() for line in input_file]


@timeit
def part_1(data):
    antennas = defaultdict(list)
    anti_nodes = set()
    for row, line in enumerate(data):
        for col, cell in enumerate(line):
            if cell != ".":
                for row_, col_ in antennas[cell]:
                    anti_nodes.add((2 * row - row_, 2 * col - col_))
                    anti_nodes.add((2 * row_ - row, 2 * col_ - col))
                antennas[cell].append((row, col))

    m, n = len(data), len(data[0])
    return sum(0 <= row < m and 0 <= col < n for row, col in anti_nodes)


@timeit
def part_2(data):
    m, n = len(data), len(data[0])
    mn = max(m, n)
    antennas = defaultdict(list)
    anti_nodes = set()
    for row, line in enumerate(data):
        for col, cell in enumerate(line):
            if cell != ".":
                for row_, col_ in antennas[cell]:
                    for k in range(-mn, mn + 1):
                        anti_nodes.add((row + k * (row_ - row), col + k * (col_ - col)))
                antennas[cell].append((row, col))

    return sum(0 <= row < m and 0 <= col < n for row, col in anti_nodes)


def main():
    setup_logging()
    with (files("data.inputs") / "day_08.txt").open() as input_file:
        data = get_data(input_file)
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
