from importlib.resources import files

from advent_of_code_2024.day_21 import get_data, part_1, part_2

DATA = [
    "029A",
    "980A",
    "179A",
    "456A",
    "379A",
]


def test_get_data():
    with (files("data.samples") / "day_21.txt").open() as input_file:
        data = get_data(input_file)

    assert data == DATA


def test_part_1():
    result = part_1(DATA)

    assert result == 126384


def test_part_2():
    result = part_2(DATA)

    assert result == 154115708116294
