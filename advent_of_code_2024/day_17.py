from importlib.resources import files

from advent_of_code_2024.utils import timeit, setup_logging


@timeit
def get_data(input_file):
    registers = []
    for line in input_file:
        if line.isspace():
            break
        register, value = line.strip().split(": ")
        registers.append(int(value))
    program = tuple(map(int, input_file.readline().strip().removeprefix("Program: ").split(",")))

    return tuple(registers), program


@timeit
def parse_and_compile(program, debug=False):
    def combo(value):
        if value < 4:
            return value
        return "abc"[value - 4]

    op_codes = [
        ("adv", True, "a >>= {}"),
        ("bxl", False, "b ^= {}"),
        ("bst", True, "b = {} & 0b111"),
        ("jnz", False, "if a: ip = {}"),
        ("bxc", False, "b ^= c"),
        ("out", True, "yield {} & 0b111"),
        ("bdv", True, "b = a >> {}"),
        ("cdv", True, "c = a >> {}"),
    ]

    program_code = []

    def tabulate(from_ip=0):
        for line in range(from_ip // 2, len(program_code)):
            program_code[line] = "    " + program_code[line]

    for ip in range(0, len(program), 2):
        op_code, operand = program[ip], program[ip + 1]
        op_name, is_combo, instruction = op_codes[op_code]
        if is_combo:
            operand = combo(operand)
        instruction = instruction.format(operand)
        if op_name == "jnz":
            program_code.append("if not a:")
            program_code.append("   break")
            tabulate(operand)
            program_code.insert(operand // 2, "while True:")
        else:
            program_code.append(instruction)

    if debug:
        program_code.insert(0, "if registers: a, b, c = registers")
        program_code.append("registers[:] = [a, b, c]")
        tabulate()
        program_code.insert(0, "def program(a=0, b=0, c=0, *, registers=None):")

    else:
        tabulate()
        program_code.insert(0, "def program(a=0, b=0, c=0):")

    program_code = "\n".join(program_code)

    print()
    print(program_code)

    local = {}
    exec(program_code, None, local)
    return local["program"]


@timeit
def part_1(registers, compiled_program):
    return ",".join(map(str, compiled_program(*registers)))


@timeit
def part_2(program, compiled_program):
    def gen_a(i):
        if i < 0:
            yield 0
            return

        for a in gen_a(i - 1):
            a <<= 3
            for bits in range(8):
                if next(compiled_program(a + bits)) == program[~i]:
                    yield a + bits

    return next(gen_a(len(program) - 1))


def main():
    setup_logging()
    with (files("data.inputs") / "day_17.txt").open() as input_file:
        registers, program = get_data(input_file)
    compiled_program = parse_and_compile(program)
    part_1(registers, compiled_program)
    part_2(program, compiled_program)


if __name__ == "__main__":
    main()
