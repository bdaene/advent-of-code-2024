from collections import Counter
from functools import cache
from importlib.resources import files

from advent_of_code_2024.utils import timeit, setup_logging


@timeit
def get_data(input_file):
    return list(map(int, input_file.readline().split()))


@cache
def get_blink(stone):
    if stone == 0:
        return (1,)
    stone_s = str(stone)
    length, rest = divmod(len(stone_s), 2)
    if rest:
        return (stone * 2024,)
    else:
        return int(stone_s[:length]), int(stone_s[length:])


def count_stones_after(stones, blinks):
    stones = Counter(stones)
    for blink in range(blinks):
        stones_ = Counter()
        for stone, count in stones.items():
            for stone_ in get_blink(stone):
                stones_[stone_] += count
        stones = stones_
    return stones


@timeit
def part_1(data):
    return sum(count_stones_after(data, 25).values())


@timeit
def part_2(data):
    return sum(count_stones_after(data, 75).values())


def main():
    setup_logging()
    with (files("data.inputs") / "day_11.txt").open() as input_file:
        data = get_data(input_file)
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
