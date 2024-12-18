from importlib.resources import files

from advent_of_code_2024.day_18 import get_data, part_1, part_2

DATA = [
    (5, 4),
    (4, 2),
    (4, 5),
    (3, 0),
    (2, 1),
    (6, 3),
    (2, 4),
    (1, 5),
    (0, 6),
    (3, 3),
    (2, 6),
    (5, 1),
    (1, 2),
    (5, 5),
    (2, 5),
    (6, 5),
    (1, 4),
    (0, 4),
    (6, 4),
    (1, 1),
    (6, 1),
    (1, 0),
    (0, 5),
    (1, 6),
    (2, 0),
]


def test_get_data():
    with (files("data.samples") / "day_18.txt").open() as input_file:
        data = get_data(input_file)

    assert data == DATA


def test_part_1():
    result = part_1(DATA, size=7, nb_bytes=12)

    assert result == 22


def test_part_2():
    result = part_2(DATA, size=7, nb_bytes=12)

    assert result == (6, 1)
