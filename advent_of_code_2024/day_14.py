import re
from collections import Counter
from importlib.resources import files
from itertools import count

from advent_of_code_2024.utils import timeit, setup_logging

PATTERN = re.compile(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")


@timeit
def get_data(input_file):
    data = []
    for line in input_file:
        px, py, vx, vy = map(int, PATTERN.fullmatch(line.strip()).groups())
        data.append(((px, py), (vx, vy)))
    return data


@timeit
def part_1(data, tiles=(101, 103), time=100):
    counter = Counter()
    tx, ty = tiles
    for (px, py), (vx, vy) in data:
        px = (px + vx * time) % tx
        py = (py + vy * time) % ty
        qx = px - tx // 2
        qy = py - ty // 2
        qx = 0 if qx == 0 else (-1 if qx < 0 else 1)
        qy = 0 if qy == 0 else (-1 if qy < 0 else 1)
        counter[(qx, qy)] += 1

    return counter[(-1, -1)] * counter[(-1, 1)] * counter[(1, -1)] * counter[(1, 1)]


@timeit
def part_2(data, tiles=(101, 103), pattern="#" * 16):
    tx, ty = tiles
    for time in count(1):
        positions = set(((px + vx * time) % tx, (py + vy * time) % ty) for (px, py), (vx, vy) in data)
        s = "\n".join("".join("#" if (px, py) in positions else "." for px in range(tx)) for py in range(ty))
        if pattern in s:
            print(time)
            print(s)
            return time


def main():
    setup_logging()
    with (files("data.inputs") / "day_14.txt").open() as input_file:
        data = get_data(input_file)
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
