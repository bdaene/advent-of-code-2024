from importlib.resources import files

from advent_of_code_2024.day_17 import get_data, parse_and_compile, part_1, part_2

DATA = ((729, 0, 0), (0, 1, 5, 4, 3, 0))


def test_get_data():
    with (files("data.samples") / "day_17.txt").open() as input_file:
        data = get_data(input_file)

    assert data == DATA


def test_run_program__1():
    registers = [0, 0, 9]
    program = parse_and_compile([2, 6], debug=True)
    program(registers=registers)
    assert registers[1] == 1


def test_run_program__2():
    program = parse_and_compile([5, 0, 5, 1, 5, 4])
    out = list(program(a=10))
    assert out == [0, 1, 2]


def test_run_program__3():
    registers = [2024, 0, 0]
    program = parse_and_compile([0, 1, 5, 4, 3, 0], debug=True)
    out = list(program(registers=registers))
    assert out == [4, 2, 5, 6, 7, 7, 7, 7, 3, 1, 0]
    assert registers[0] == 0


def test_run_program__4():
    registers = [0, 29, 0]
    program = parse_and_compile([1, 7], debug=True)
    program(registers=registers)
    assert registers[1] == 26


def test_run_program__5():
    registers = [0, 2024, 43690]
    program = parse_and_compile([4, 0], debug=True)
    program(registers=registers)
    assert registers[1] == 44354


def test_part_1():
    registers, program = DATA
    compiled_program = parse_and_compile(program)
    result = part_1(registers, compiled_program)

    assert result == "4,6,3,5,6,3,5,2,1,0"


def test_part_2():
    program, expected_a = (0, 3, 5, 4, 3, 0), 117440
    compiled_program = parse_and_compile(program)

    assert tuple(compiled_program(a=expected_a)) == program
    assert part_2(program, compiled_program) == expected_a
