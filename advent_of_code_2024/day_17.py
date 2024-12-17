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


def get_combo(combo, registers):
    if combo < 4:
        return combo
    combo -= 4
    if combo < len(registers):
        return registers[combo]
    raise ValueError(f"Invalid combo {combo}")


RA, RB, RC = range(3)


def run_program(registers, program):
    ip = 0
    while 0 <= ip < len(program):
        opcode, operand = program[ip], program[ip + 1]
        ip += 2
        if opcode == 0:  # adv
            registers[RA] >>= get_combo(operand, registers)
        elif opcode == 1:  # bxl
            registers[RB] ^= operand
        elif opcode == 2:  # bst
            registers[RB] = get_combo(operand, registers) % 8
        elif opcode == 3:  # jnz
            if registers[RA] != 0:
                ip = operand
        elif opcode == 4:  # bxc
            registers[RB] ^= registers[RC]
        elif opcode == 5:  # out
            yield get_combo(operand, registers) % 8
        elif opcode == 6:  # bdv
            registers[RB] = registers[RA] >> get_combo(operand, registers)
        elif opcode == 7:  # cdv
            registers[RC] = registers[RA] >> get_combo(operand, registers)
        else:
            raise ValueError(f"Invalid opcode: {ip} {opcode} {operand}")


@timeit
def part_1(data):
    registers, program = data
    registers = list(registers)
    return ",".join(map(str, run_program(registers, program)))


@timeit
def part_2(data):
    registers, program = data

    def gen_a(i):
        if i < 0:
            yield 0
            return

        for a in gen_a(i - 1):
            a <<= 3
            for bits in range(8):
                if next(run_program([a + bits, 0, 0], program)) == program[~i]:
                    yield a + bits

    return next(gen_a(len(program) - 1))


def main():
    setup_logging()
    with (files("data.inputs") / "day_17.txt").open() as input_file:
        data = get_data(input_file)
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
