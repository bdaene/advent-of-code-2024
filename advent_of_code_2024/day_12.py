from importlib.resources import files

from advent_of_code_2024.utils import timeit, setup_logging


@timeit
def get_data(input_file):
    return [line.strip() for line in input_file]


def gen_regions(plants):
    visited = [[False for _ in line] for line in plants]
    m, n = len(plants), len(plants[0])
    for start_row, line in enumerate(plants):
        for start_col, plant in enumerate(line):
            if visited[start_row][start_col]:
                continue
            visited[start_row][start_col] = True
            to_visit = [(start_row, start_col)]
            area, perimeter = 1, set()
            while to_visit:
                row, col = to_visit.pop()
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    row_, col_ = row + dr, col + dc
                    if 0 <= row_ < m and 0 <= col_ < n and plants[row_][col_] == plant:
                        if not visited[row_][col_]:
                            area += 1
                            visited[row_][col_] = True
                            to_visit.append((row_, col_))
                    else:
                        perimeter.add((row, col, row_, col_))
            # print(plant, area, perimeter)
            yield area, perimeter


@timeit
def part_1(data):
    return sum(area * len(perimeter) for area, perimeter in gen_regions(data))


def count_fences(perimeter):
    total = 0
    while perimeter:
        row, col, row_, col_ = perimeter.pop()
        total += 1
        if row == row_:
            for dr in (-1, 1):
                r = row + dr
                while (r, col, r, col_) in perimeter:
                    perimeter.remove((r, col, r, col_))
                    r += dr
        if col == col_:
            for dc in (-1, 1):
                c = col + dc
                while (row, c, row_, c) in perimeter:
                    perimeter.remove((row, c, row_, c))
                    c += dc
    return total


@timeit
def part_2(data):
    return sum(area * count_fences(perimeter) for area, perimeter in gen_regions(data))


def main():
    setup_logging()
    with (files("data.inputs") / "day_12.txt").open() as input_file:
        data = get_data(input_file)
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
