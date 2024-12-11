from importlib.resources import files

from advent_of_code_2024.day_11 import get_data, part_1, part_2

DATA = [125, 17]


def test_get_data():
    with (files("data.samples") / "day_11.txt").open() as input_file:
        data = get_data(input_file)

    assert data == DATA


def test_part_1():
    result = part_1(DATA)

    assert result == 55312


def test_part_2():
    result = part_2(DATA)

    assert result == 3
