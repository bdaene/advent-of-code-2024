from importlib.resources import files

from advent_of_code_2024.day_25 import get_data, part_1

DATA = (
    [  # Locks
        (0, 5, 3, 4, 3),
        (1, 2, 0, 5, 3),
    ],
    [  # Keys
        (5, 0, 2, 1, 3),
        (4, 3, 4, 0, 2),
        (3, 0, 2, 0, 1),
    ],
)


def test_get_data():
    with (files("data.samples") / "day_25.txt").open() as input_file:
        data = get_data(input_file)

    assert data == DATA


def test_part_1():
    result = part_1(DATA)

    assert result == 3
