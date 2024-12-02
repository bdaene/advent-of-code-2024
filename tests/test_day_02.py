from importlib.resources import files

from advent_of_code_2024.day_02 import get_data, part_1, part_2

DATA = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9],
]


def test_get_data():
    with (files("data.samples") / "day_02.txt").open() as input_file:
        data = get_data(input_file)

    assert data == DATA


def test_part_1():
    result = part_1(DATA)

    assert result == 2


def test_part_2():
    result = part_2(DATA)

    assert result == 4
