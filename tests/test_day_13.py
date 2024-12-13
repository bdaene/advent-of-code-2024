from importlib.resources import files

from advent_of_code_2024.day_13 import get_data, part_1, part_2

DATA = [
    ((94, 34), (22, 67), (8400, 5400)),
    ((26, 66), (67, 21), (12748, 12176)),
    ((17, 86), (84, 37), (7870, 6450)),
    ((69, 23), (27, 71), (18641, 10279)),
]


def test_get_data():
    with (files("data.samples") / "day_13.txt").open() as input_file:
        data = get_data(input_file)

    assert data == DATA


def test_part_1():
    result = part_1(DATA)

    assert result == 480


def test_part_2():
    result = part_2(DATA)

    assert result == 875318608908
