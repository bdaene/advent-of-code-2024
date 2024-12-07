from importlib.resources import files

from advent_of_code_2024.day_07 import get_data, part_1, part_2

DATA = [
    (190, (10, 19)),
    (3267, (81, 40, 27)),
    (83, (17, 5)),
    (156, (15, 6)),
    (7290, (6, 8, 6, 15)),
    (161011, (16, 10, 13)),
    (192, (17, 8, 14)),
    (21037, (9, 7, 18, 13)),
    (292, (11, 6, 16, 20)),
]


def test_get_data():
    with (files("data.samples") / "day_07.txt").open() as input_file:
        data = get_data(input_file)

    assert data == DATA


def test_part_1():
    result = part_1(DATA)

    assert result == 3749


def test_part_2():
    result = part_2(DATA)

    assert result == 11387
