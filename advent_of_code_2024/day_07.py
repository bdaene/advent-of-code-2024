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


def check(value, numbers, concat=False):
    if len(numbers) == 1:
        return numbers[-1] == value

    number = numbers[-1]
    if value < number:
        return False
    numbers = numbers[:-1]

    if check(value - number, numbers, concat):
        return True

    prev_value, r = divmod(value, number)
    if r == 0 and check(prev_value, numbers, concat):
        return True

    if concat and value != number:
        s_value, s_number = str(value), str(number)
        if s_value.endswith(s_number):
            prev_value = int(s_value.removesuffix(s_number))
            if check(prev_value, numbers, concat):
                return True

    return False


@timeit
def part_1(data):
    return sum(value for value, numbers in data if check(value, numbers))


@timeit
def part_2(data):
    return sum(value for value, numbers in data if check(value, numbers, True))


def main():
    setup_logging()
    with (files("data.inputs") / "day_07.txt").open() as input_file:
        data = get_data(input_file)
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
