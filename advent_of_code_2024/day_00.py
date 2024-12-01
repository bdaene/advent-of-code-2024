from importlib.resources import files

from advent_of_code_2024.utils import timeit, setup_logging


@timeit
def get_data(input_file):
    return [line.strip() for line in input_file]


@timeit
def part_1(data):
    return len(data)


@timeit
def part_2(data):
    return len(data)


def main():
    setup_logging()
    with (files("data.inputs") / "day_00.txt").open() as input_file:
        data = get_data(input_file)
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
