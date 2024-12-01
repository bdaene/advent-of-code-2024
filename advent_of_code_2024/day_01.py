from collections import Counter
from importlib.resources import files

from advent_of_code_2024.utils import timeit, setup_logging


@timeit
def get_data(input_file):
    data = [[], []]
    for line in input_file:
        for i, value in enumerate(line.split()):
            data[i].append(int(value))
    return data


@timeit
def part_1(data):
    a, b = data
    a, b = sorted(a), sorted(b)
    return sum(abs(a_ - b_) for a_, b_ in zip(a, b))


@timeit
def part_2(data):
    count = Counter(data[1])
    return sum(a * count[a] for a in data[0])


def main():
    setup_logging()
    with (files("data.inputs") / "day_01.txt").open() as input_file:
        data = get_data(input_file)
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
