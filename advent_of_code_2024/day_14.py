import re
from collections import Counter
from importlib.resources import files

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
        if qx == 0 or qy == 0:
            continue
        counter[(qx > 0, qy > 0)] += 1

    total = 1
    for v in counter.values():
        total *= v
    return total


@timeit
def part_2(data, tiles=(101, 103)):
    tx, ty = tiles
    vars_x, vars_y = [], []
    for time in range(max(tiles)):
        positions = set(((px + vx * time) % tx, (py + vy * time) % ty) for (px, py), (vx, vy) in data)

        n = len(positions)
        sum_x2, sum_x = sum(px**2 for px, py in positions), sum(px for px, py in positions)
        vars_x.append(sum_x2 / n - (sum_x / n) ** 2)
        sum_y2, sum_y = sum(py**2 for px, py in positions), sum(py for px, py in positions)
        vars_y.append(sum_y2 / n - (sum_y / n) ** 2)

    time_x = min(range(len(vars_x)), key=vars_x.__getitem__)
    time_y = min(range(len(vars_y)), key=vars_y.__getitem__)
    # print(time_x, time_y)

    # time = time_x + tx * u = time_y + ty * v
    u = ((time_y - time_x) * pow(tx, -1, ty)) % ty
    time = time_x + u * tx

    # print(time)
    # positions = set(((px + vx * time) % tx, (py + vy * time) % ty) for (px, py), (vx, vy) in data)
    # print("\n".join("".join("#" if (px, py) in positions else "." for px in range(tx)) for py in range(ty)))

    return time


def main():
    setup_logging()
    with (files("data.inputs") / "day_14.txt").open() as input_file:
        data = get_data(input_file)
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
