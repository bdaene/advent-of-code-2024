from importlib.resources import files

from advent_of_code_2024.utils import timeit, setup_logging


@timeit
def get_data(input_file):
    locks, keys = [], []
    while True:
        grid = [input_file.readline().strip() for _ in range(7)]
        pins = tuple(sum(line[col] == "#" for line in grid) - 1 for col in range(5))
        if grid[0] == "#" * 5:
            locks.append(pins)
        else:
            keys.append(pins)

        if not input_file.readline():
            break

    return locks, keys


@timeit
def part_1(data):
    locks, keys = data
    return sum(all(lock_pin + key_pin <= 5 for lock_pin, key_pin in zip(lock, key)) for lock in locks for key in keys)


def main():
    setup_logging()
    with (files("data.inputs") / "day_25.txt").open() as input_file:
        data = get_data(input_file)
    part_1(data)


if __name__ == "__main__":
    main()
