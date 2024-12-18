from importlib.resources import files

from advent_of_code_2024.utils import timeit, setup_logging


@timeit
def get_data(input_file):
    return [tuple(map(int, line.strip().split(","))) for line in input_file]


def get_nb_steps(corrupted, size):
    steps = 0
    to_visit = [(0, 0)]
    visited = [[None for col in range(size)] for row in range(size)]
    while to_visit:
        steps += 1
        to_visit_ = []
        for row, col in to_visit:
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                row_, col_ = row + dr, col + dc
                if 0 <= row_ < size and 0 <= col_ < size:
                    if corrupted[row_][col_] or visited[row_][col_]:
                        continue
                    to_visit_.append((row_, col_))
                    visited[row_][col_] = steps
                    if row_ == size - 1 and col_ == size - 1:
                        return steps
        to_visit = to_visit_


@timeit
def part_1(data, size=71, nb_bytes=1024):
    corrupted = [[False for col in range(size)] for row in range(size)]
    for x, y in data[:nb_bytes]:
        corrupted[y][x] = True

    # print()
    # print("\n".join("".join("#" if cell else "." for cell in line) for line in corrupted))

    return get_nb_steps(corrupted, size)


@timeit
def part_2(data, size=71, nb_bytes=1024):
    corrupted = [[False for col in range(size)] for row in range(size)]
    for x, y in data[:nb_bytes]:
        corrupted[y][x] = True

    while get_nb_steps(corrupted, size) is not None:
        x, y = data[nb_bytes]
        corrupted[y][x] = True
        nb_bytes += 1

    return data[nb_bytes - 1]


def main():
    setup_logging()
    with (files("data.inputs") / "day_18.txt").open() as input_file:
        data = get_data(input_file)
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
