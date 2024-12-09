from importlib.resources import files

from advent_of_code_2024.day_09 import get_data, part_1, part_2

DATA = [2, 3, 3, 3, 1, 3, 3, 1, 2, 1, 4, 1, 4, 1, 3, 1, 4, 0, 2]


def test_get_data():
    with (files("data.samples") / "day_09.txt").open() as input_file:
        data = get_data(input_file)

    assert data == DATA


def test_part_1():
    result = part_1(DATA)

    assert result == 1928


def test_part_2():
    result = part_2(DATA)

    assert result == 2858
