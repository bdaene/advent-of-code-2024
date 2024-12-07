import operator
from functools import cache
from importlib.resources import files

from advent_of_code_2024.utils import timeit, setup_logging


@timeit
def get_data(input_file):
    data = []
    for line in input_file:
        value, equation = line.strip().split(": ")
        equation = tuple(map(int, equation.split(" ")))
        data.append((int(value), equation))
    return data


@cache
def get_values(numbers, operators):
    if len(numbers) == 1:
        return {numbers[-1]}
    value = numbers[-1]
    numbers = numbers[:-1]
    values = get_values(numbers, operators)
    new_values = set()
    for op in operators:
        new_values |= {op(v, value) for v in values}
    return new_values


@timeit
def part_1(data):
    return sum(
        value
        for value, numbers in data
        if value in get_values(numbers, (operator.add, operator.mul))
    )


@timeit
def part_2(data):
    def concat(a, b):
        return int(str(a) + str(b))

    return sum(
        value
        for value, numbers in data
        if value in get_values(numbers, (operator.add, operator.mul, concat))
    )


def main():
    setup_logging()
    with (files("data.inputs") / "day_07.txt").open() as input_file:
        data = get_data(input_file)
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
