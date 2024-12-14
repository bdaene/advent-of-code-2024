from importlib.resources import files

from advent_of_code_2024.day_14 import get_data, part_1, part_2

DATA = [
    ((0, 4), (3, -3)),
    ((6, 3), (-1, -3)),
    ((10, 3), (-1, 2)),
    ((2, 0), (2, -1)),
    ((0, 0), (1, 3)),
    ((3, 0), (-2, -2)),
    ((7, 6), (-1, -3)),
    ((3, 0), (-1, -2)),
    ((9, 3), (2, 3)),
    ((7, 3), (-1, 2)),
    ((2, 4), (2, -3)),
    ((9, 5), (-3, -3)),
]


def test_get_data():
    with (files("data.samples") / "day_14.txt").open() as input_file:
        data = get_data(input_file)

    assert data == DATA


def test_part_1():
    result = part_1(DATA, tiles=(11, 7))

    assert result == 12


def test_part_2():
    result = part_2(DATA, tiles=(11, 7))

    assert result == 38
