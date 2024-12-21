from functools import cache
from heapq import heappop, heappush
from importlib.resources import files
from itertools import pairwise

from advent_of_code_2024.utils import timeit, setup_logging


@timeit
def get_data(input_file):
    return [line.strip() for line in input_file]


def parse_keypad(keypad):
    return {
        key: (row, col)
        for row, line in enumerate(keypad.split("\n"))
        for col, key in enumerate(line)
        if not key.isspace()
    }


NUMERIC_KEYPAD = parse_keypad("""
789
456
123
 0A 
""")

DIRECTIONAL_KEY_PAD = parse_keypad("""
 ^A
<v>
""")

DIRECTIONS = [(0, 1, ">"), (1, 0, "v"), (0, -1, "<"), (-1, 0, "^")]


def build_get_move_and_push_sequence_function(keypads):
    @cache
    def get_move_and_push_sequence(from_key, to_key, level):
        if level == 0:
            return to_key

        keypad = keypads[level]
        start_position, end_position = keypad[from_key], keypad[to_key]
        to_visit = [(0, True, "A", start_position, "")]
        while to_visit:
            _, need_push, prev_key, position, sequence = heappop(to_visit)
            if not need_push:
                return sequence
            if position == end_position:
                next_sequence = sequence + get_move_and_push_sequence(prev_key, "A", level - 1)
                heappush(to_visit, (len(next_sequence), False, "A", keypad["A"], next_sequence))
                continue
            row, col = position
            for dr, dc, move in DIRECTIONS:
                next_position = (row + dr, col + dc)
                if next_position in keypad.values():
                    next_sequence = sequence + get_move_and_push_sequence(prev_key, move, level - 1)
                    heappush(to_visit, (len(next_sequence), True, move, next_position, next_sequence))

    return get_move_and_push_sequence


# Same thing as get_move_and_push_sequence but only returns the length of the sequence instead of the sequence itself
def build_get_move_and_push_cost_function(keypads):
    @cache
    def get_move_and_push_cost(from_key, to_key, level):
        if level == 0:
            return 1

        keypad = keypads[level]
        start_position, end_position = keypad[from_key], keypad[to_key]
        to_visit = [(0, True, "A", start_position)]
        while to_visit:
            cost, need_push, prev_key, position = heappop(to_visit)
            if not need_push:
                return cost
            if position == end_position:
                next_cost = cost + get_move_and_push_cost(prev_key, "A", level - 1)
                heappush(to_visit, (next_cost, False, "A", keypad["A"]))
                continue
            row, col = position
            for dr, dc, move in DIRECTIONS:
                next_position = (row + dr, col + dc)
                if next_position in keypad.values():
                    next_cost = cost + get_move_and_push_cost(prev_key, move, level - 1)
                    heappush(to_visit, (next_cost, True, move, next_position))

    return get_move_and_push_cost


@timeit
def part_1(data):
    levels = 3
    keypads = [DIRECTIONAL_KEY_PAD] * levels + [NUMERIC_KEYPAD]
    get_move_and_push_sequence = build_get_move_and_push_sequence_function(keypads)

    total = 0
    for code in data:
        sequence = ""
        for from_key, to_key in pairwise("A" + code):
            sequence += get_move_and_push_sequence(from_key, to_key, levels)
        # print(code, sequence)
        total += len(sequence) * int(code[:-1])
    return total


@timeit
def part_2(data):
    levels = 26
    keypads = [DIRECTIONAL_KEY_PAD] * levels + [NUMERIC_KEYPAD]
    get_move_and_push_cost = build_get_move_and_push_cost_function(keypads)
    return sum(
        get_move_and_push_cost(from_key, to_key, levels) * int(code[:-1])
        for code in data
        for from_key, to_key in pairwise("A" + code)
    )


def main():
    setup_logging()
    with (files("data.inputs") / "day_21.txt").open() as input_file:
        data = get_data(input_file)
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
