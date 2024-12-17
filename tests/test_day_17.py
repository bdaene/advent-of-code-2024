from importlib.resources import files

import pytest

from advent_of_code_2024.day_17 import get_data, run_program, part_1, part_2, get_combo

DATA = ((729, 0, 0), (0, 1, 5, 4, 3, 0))


def test_get_data():
    with (files("data.samples") / "day_17.txt").open() as input_file:
        data = get_data(input_file)

    assert data == DATA


@pytest.mark.parametrize(
    "combo, expected_value",
    [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 0xA),
        (5, 0xB),
        (6, 0xC),
    ],
)
def test_get_combo(combo, expected_value):
    value = get_combo(combo, [0xA, 0xB, 0xC])
    assert value == expected_value


def test_run_program__1():
    registers, program = [0, 0, 9], (2, 6)
    list(run_program(registers, program))
    assert registers[1] == 1


def test_run_program__2():
    registers, program = [10, 0, 0], (5, 0, 5, 1, 5, 4)
    out = list(run_program(registers, program))
    assert out == [0, 1, 2]


def test_run_program__3():
    registers, program = [2024, 0, 0], (0, 1, 5, 4, 3, 0)
    out = list(run_program(registers, program))
    assert out == [4, 2, 5, 6, 7, 7, 7, 7, 3, 1, 0]
    assert registers[0] == 0


def test_run_program__4():
    registers, program = [0, 29, 0], (1, 7)
    list(run_program(registers, program))
    assert registers[1] == 26


def test_run_program__5():
    registers, program = [0, 2024, 43690], (4, 0)
    list(run_program(registers, program))
    assert registers[1] == 44354


def test_part_1():
    result = part_1(DATA)

    assert result == "4,6,3,5,6,3,5,2,1,0"


def test_part_2():
    program = (0, 3, 5, 4, 3, 0)
    a = part_2(((0, 0, 0), program))

    assert a == 117440


def test_part_2_2():
    program = (2, 4, 1, 1, 7, 5, 1, 5, 4, 1, 5, 5, 0, 3, 3, 0)
    out = tuple(run_program([164278764924605, 0, 0], program))
    assert out == program
