from importlib.resources import files

from advent_of_code_2024.utils import timeit, setup_logging


@timeit
def get_data(input_file):
    return [line.strip() for line in input_file]


@timeit
def part_1(data):
    xmas = "XMAS"
    m, n = len(data), len(data[0])
    count = 0
    for row in range(m):
        for col in range(n):
            if data[row][col] != xmas[0]:
                continue
            for dr, dc in [
                (0, 1),
                (1, 1),
                (1, 0),
                (1, -1),
                (0, -1),
                (-1, -1),
                (-1, 0),
                (-1, 1),
            ]:
                for k, c in enumerate(xmas):
                    row_, col_ = row + dr * k, col + dc * k
                    if not (0 <= row_ < m and 0 <= col_ < n and data[row_][col_] == c):
                        break
                else:
                    count += 1

    return count


@timeit
def part_2(data):
    xmas = "MSM"
    m, n = len(data), len(data[0])
    count = 0
    for row in range(1, m - 1):
        for col in range(1, n - 1):
            if data[row][col] == "A":
                if (
                    data[row - 1][col - 1] + data[row + 1][col + 1] in xmas
                    and data[row - 1][col + 1] + data[row + 1][col - 1] in xmas
                ):
                    count += 1
    return count


def main():
    setup_logging()
    with (files("data.inputs") / "day_04.txt").open() as input_file:
        data = get_data(input_file)
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
