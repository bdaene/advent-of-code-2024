from importlib.resources import files
from itertools import pairwise

from advent_of_code_2024.utils import timeit, setup_logging


@timeit
def get_data(input_file):
    return [list(map(int, line.split())) for line in input_file]


def is_safe(report):
    if all(1 <= b - a <= 3 for a, b in pairwise(report)):
        return True
    if all(1 <= a - b <= 3 for a, b in pairwise(report)):
        return True
    return False


@timeit
def part_1(data):
    return sum(is_safe(report) for report in data)


@timeit
def part_2(data):
    count = 0
    for report in data:
        if any(is_safe(report[:i] + report[i + 1 :]) for i in range(len(report))):
            count += 1

    return count


def main():
    setup_logging()
    with (files("data.inputs") / "day_02.txt").open() as input_file:
        data = get_data(input_file)
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
