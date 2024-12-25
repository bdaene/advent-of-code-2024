import operator
from importlib.resources import files

from advent_of_code_2024.utils import timeit, setup_logging


@timeit
def get_data(input_file):
    variables = dict(x=0, y=0)
    for line in input_file:
        if line.isspace():
            break
        var, bit, value = line[0], line[1:3], line[5]
        variables[var] += int(value) << int(bit)

    gates = {}
    for line in input_file:
        a, op, b, _, c = line.strip().split(" ")
        gates[c] = (op, a, b)

    return variables, gates


def sort_gates(gates):
    wires = {c: {a, b} for c, (op, a, b) in gates.items()}

    available_wires = {i for inputs in wires.values() for i in inputs if i not in wires}
    sorted_wires = []
    while wires:
        new_available_wires = {c for c, inputs in wires.items() if not (inputs - available_wires)}
        sorted_wires += sorted(new_available_wires)
        available_wires |= new_available_wires
        for c in new_available_wires:
            del wires[c]

    return [(wire, gates[wire]) for wire in sorted_wires]


OPERATORS = {"AND": operator.and_, "OR": operator.or_, "XOR": operator.xor}


def compute(variables, gates):
    values = {}
    bit_length = max(int(wire[1:]) for wire, gate in gates if wire[0] == "z") + 1

    for variable, value in variables.items():
        for bit in range(bit_length):
            values[f"{variable}{bit:02d}"] = value & 1
            value >>= 1

    for wire, (op, a, b) in gates:
        va, vb = values[a], values[b]
        op = OPERATORS[op]
        values[wire] = op(va, vb)

    z = 0
    for bit in range(bit_length):
        z += values[f"z{bit:02d}"] << bit
    return z


@timeit
def part_1(data):
    variables, gates = data
    gates = sort_gates(gates)
    return compute(variables, gates)


@timeit
def part_2(data, operation=operator.add):
    variables, gates = data
    sorted_gates = sort_gates(gates)
    bit_length = max(int(wire[1:]) for wire in gates if wire[0] == "z") + 1
    number_format = "{:0" + str(bit_length) + "b}"

    line_format = "{:4} {:4} " + number_format + " " + number_format

    def extract_gates(gate, levels=3):
        if levels > 0 and gate in gates:
            op, a, b = gates[gate]
            a_, b_ = extract_gates(a, levels - 1), extract_gates(b, levels - 1)
            if a_ > b_:
                a_, b_ = b_, a_
            return f"{gate} = {op}({a_}, {b_})"
        return gate

    wrong_bits = set()
    for bit in range(bit_length):
        for x in range(2):
            x_, y_ = x << bit, 1 << bit
            z = compute(dict(x=x_, y=y_), sorted_gates)
            z_ = operation(x_, y_) & ((1 << bit_length) - 1)
            if z != z_:
                print(line_format.format(bit, x, z, z_))
                wrong_bits.add(bit)

    for bit in sorted(wrong_bits | {bit + 1 for bit in wrong_bits}):
        print(extract_gates(f"z{bit:02}"))

    return ",".join(f"z{bit:02}" for bit in wrong_bits)


def main():
    setup_logging()
    with (files("data.inputs") / "day_24.txt").open() as input_file:
        data = get_data(input_file)
    part_1(data)

    variables, gates = data

    swapped_gates = [
        # ("z14", "vss"),
        # ("kdh", "hjf"),
        # ("z31", "kpp"),
        # ("z35", "sgj"),
    ]
    for gate_a, gate_b in swapped_gates:
        gates[gate_a], gates[gate_b] = gates[gate_b], gates[gate_a]
    print(",".join(sorted(gate for swap in swapped_gates for gate in swap)))

    part_2((variables, gates))


if __name__ == "__main__":
    main()
