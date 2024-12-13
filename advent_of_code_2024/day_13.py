import re
from functools import partial
from importlib.resources import files

from advent_of_code_2024.utils import timeit, setup_logging


BUTTON_PATTERN = re.compile(r"Button [AB]: X\+(\d+), Y\+(\d+)")
PRIZE_PATTERN = re.compile(r"Prize: X=(\d+), Y=(\d+)")


@timeit
def get_data(input_file):
    machines = []
    while True:
        x, y = BUTTON_PATTERN.fullmatch(input_file.readline().strip()).groups()
        a_button = (int(x), int(y))
        x, y = BUTTON_PATTERN.fullmatch(input_file.readline().strip()).groups()
        b_button = (int(x), int(y))
        x, y = PRIZE_PATTERN.fullmatch(input_file.readline().strip()).groups()
        prize = (int(x), int(y))
        machines.append((a_button, b_button, prize))
        if not input_file.readline():
            break

    return machines


def count_tokens(machine, offset=0):
    (xa, ya), (xb, yb), (xp, yp) = machine
    xp, yp = xp + offset, yp + offset
    d = xa * yb - xb * ya
    dpb = xb * yp - xp * yb
    dpa = xa * yp - xp * ya
    if dpa % d != 0 or dpb % d != 0:
        return 0
    a, b = dpb // -d, dpa // d
    return 3 * a + b


@timeit
def part_1(data):
    return sum(map(count_tokens, data))


@timeit
def part_2(data):
    count_tokens_2 = partial(count_tokens, offset=10000000000000)
    return sum(map(count_tokens_2, data))


def main():
    setup_logging()
    with (files("data.inputs") / "day_13.txt").open() as input_file:
        data = get_data(input_file)
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
