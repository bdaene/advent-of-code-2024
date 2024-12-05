from collections import defaultdict
from importlib.resources import files

from advent_of_code_2024.utils import timeit, setup_logging


@timeit
def get_data(input_file):
    after = defaultdict(set)
    for line in input_file:
        if line.isspace():
            break
        a, b = map(int, line.strip().split("|"))
        after[a].add(b)

    updates = [list(map(int, line.strip().split(","))) for line in input_file]

    return after, updates


@timeit
def part_1(data):
    after, updates = data
    total = 0
    for update in updates:
        for i, page in enumerate(update):
            if any(page_ in after[page] for page_ in update[:i]):
                break
        else:
            total += update[len(update) // 2]
    return total


@timeit
def part_2(data):
    after, updates = data
    total = 0
    for update in updates:
        ordered_update = []
        found_swap = False
        for page in update:
            for i, page_ in enumerate(ordered_update):
                if page_ in after[page]:
                    found_swap = True
                    ordered_update.insert(i, page)
                    break
            else:
                ordered_update.append(page)

        if found_swap:
            total += ordered_update[len(ordered_update) // 2]
    return total


def main():
    setup_logging()
    with (files("data.inputs") / "day_05.txt").open() as input_file:
        data = get_data(input_file)
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
