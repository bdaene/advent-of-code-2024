from collections import Counter
from importlib.resources import files

from advent_of_code_2024.utils import timeit, setup_logging


@timeit
def get_data(input_file):
    return list(map(int, input_file.readline().split()))


def compute_after(stones, blinks):
    stones = Counter(stones)
    for _ in range(blinks):
        stones_ = Counter()
        for stone, count in stones.items():
            if stone == 0:
                stones_[1] += count
                continue
            stone_s = str(stone)
            l, r = divmod(len(stone_s), 2)
            if r:
                stones_[stone * 2024] += count
            else:
                stones_[int(stone_s[:l])] += count
                stones_[int(stone_s[l:])] += count
        stones = stones_

    return stones


@timeit
def part_1(data):
    return sum(compute_after(data, 25).values())


@timeit
def part_2(data):
    return sum(compute_after(data, 75).values())


def main():
    setup_logging()
    with (files("data.inputs") / "day_11.txt").open() as input_file:
        data = get_data(input_file)
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
