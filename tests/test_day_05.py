from importlib.resources import files

from advent_of_code_2024.day_05 import get_data, part_1, part_2

DATA = (
    {
        29: {13},
        47: {29, 13, 61, 53},
        53: {13, 29},
        61: {29, 53, 13},
        75: {13, 47, 29, 53, 61},
        97: {75, 13, 47, 61, 53, 29}
    },
    [
        [75, 47, 61, 53, 29],
        [97, 61, 53, 29, 13],
        [75, 29, 13],
        [75, 97, 47, 61, 53],
        [61, 13, 29],
        [97, 13, 75, 29, 47],
    ]
)


def test_get_data():
    with (files("data.samples") / "day_05.txt").open() as input_file:
        data = get_data(input_file)

    assert data == DATA


def test_part_1():
    result = part_1(DATA)

    assert result == 143


def test_part_2():
    result = part_2(DATA)

    assert result == 123
