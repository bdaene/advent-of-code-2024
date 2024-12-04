from importlib.resources import files

from advent_of_code_2024.day_03 import get_data, part_1, part_2

DATA = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def test_get_data():
    with (files("data.samples") / "day_03.txt").open() as input_file:
        data = get_data(input_file)

    assert data == DATA


def test_part_1():
    result = part_1(DATA)

    assert result == 161


def test_part_2():
    result = part_2(DATA)

    assert result == 48
