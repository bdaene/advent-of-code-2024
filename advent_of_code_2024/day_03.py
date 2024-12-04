import re
from importlib.resources import files

from advent_of_code_2024.utils import timeit, setup_logging


@timeit
def get_data(input_file):
    return input_file.read()


MUL_PATTERN = re.compile(r'mul\((\d+),(\d+)\)')


@timeit
def part_1(data):
    return sum(int(a) * int(b) for a, b in MUL_PATTERN.findall(data))


@timeit
def part_2(data):
    data = re.sub(r"don't\(\).*?do\(\)", "", data, flags=re.DOTALL)
    return sum(int(a) * int(b) for a, b in MUL_PATTERN.findall(data))


def main():
    setup_logging()
    with (files("data.inputs") / "day_03.txt").open() as input_file:
        data = get_data(input_file)
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
