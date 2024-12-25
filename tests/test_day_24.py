import operator
from importlib.resources import files

from advent_of_code_2024.day_24 import get_data, part_1, part_2

DATA = (
    {"x": 13, "y": 31},
    {
        "bfw": ("OR", "vdt", "tnw"),
        "bqk": ("OR", "ffh", "nrd"),
        "djm": ("AND", "y00", "y03"),
        "ffh": ("XOR", "x03", "y03"),
        "fgs": ("OR", "y04", "y02"),
        "frj": ("OR", "tnw", "fst"),
        "fst": ("OR", "x00", "x03"),
        "gnj": ("OR", "tnw", "pbm"),
        "hwm": ("AND", "nrd", "vdt"),
        "kjc": ("AND", "x04", "y00"),
        "kpj": ("OR", "pbm", "djm"),
        "kwq": ("OR", "ntg", "kjc"),
        "mjb": ("XOR", "ntg", "fgs"),
        "nrd": ("OR", "y03", "x01"),
        "ntg": ("XOR", "x00", "y04"),
        "pbm": ("AND", "y01", "x02"),
        "psh": ("OR", "y03", "y00"),
        "qhw": ("OR", "djm", "pbm"),
        "rvg": ("AND", "kjc", "fst"),
        "tgd": ("XOR", "psh", "fgs"),
        "tnw": ("OR", "y02", "x01"),
        "vdt": ("OR", "x03", "x00"),
        "wpb": ("XOR", "nrd", "fgs"),
        "z00": ("XOR", "bfw", "mjb"),
        "z01": ("XOR", "tgd", "rvg"),
        "z02": ("AND", "gnj", "wpb"),
        "z03": ("AND", "hwm", "bqk"),
        "z04": ("XOR", "frj", "qhw"),
        "z05": ("OR", "kwq", "kpj"),
        "z06": ("OR", "bfw", "bqk"),
        "z07": ("OR", "bqk", "frj"),
        "z08": ("OR", "bqk", "frj"),
        "z09": ("XOR", "qhw", "tgd"),
        "z10": ("AND", "bfw", "frj"),
        "z11": ("AND", "gnj", "tgd"),
        "z12": ("XOR", "tgd", "rvg"),
    },
)


def test_get_data():
    with (files("data.samples") / "day_24.txt").open() as input_file:
        data = get_data(input_file)

    assert data == DATA


def test_part_1():
    result = part_1(DATA)

    assert result == 2024


def test_part_2():
    with (files("data.samples") / "day_24_2.txt").open() as input_file:
        data = get_data(input_file)
    result = part_2(data, operator.and_)

    assert result == "z00,z01,z02,z05"
