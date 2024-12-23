from importlib.resources import files

from advent_of_code_2024.day_23 import get_data, part_1, part_2

DATA = [
    ("kh", "tc"),
    ("qp", "kh"),
    ("de", "cg"),
    ("ka", "co"),
    ("yn", "aq"),
    ("qp", "ub"),
    ("cg", "tb"),
    ("vc", "aq"),
    ("tb", "ka"),
    ("wh", "tc"),
    ("yn", "cg"),
    ("kh", "ub"),
    ("ta", "co"),
    ("de", "co"),
    ("tc", "td"),
    ("tb", "wq"),
    ("wh", "td"),
    ("ta", "ka"),
    ("td", "qp"),
    ("aq", "cg"),
    ("wq", "ub"),
    ("ub", "vc"),
    ("de", "ta"),
    ("wq", "aq"),
    ("wq", "vc"),
    ("wh", "yn"),
    ("ka", "de"),
    ("kh", "ta"),
    ("co", "tc"),
    ("wh", "qp"),
    ("tb", "vc"),
    ("td", "yn"),
]


def test_get_data():
    with (files("data.samples") / "day_23.txt").open() as input_file:
        data = get_data(input_file)

    assert data == DATA


def test_part_1():
    result = part_1(DATA)

    assert result == 7


def test_part_2():
    result = part_2(DATA)

    assert result == "co,de,ka,ta"
