from importlib.resources import files

from advent_of_code_2024.utils import timeit, setup_logging


@timeit
def get_data(input_file):
    return [line.strip() for line in input_file]


@timeit
def part_1(data):
    row, col = next(
        (row, col) for row, row_cells in enumerate(data) for col, cell in enumerate(row_cells) if cell == "^"
    )

    grid = [list(line) for line in data]
    dr, dc = -1, 0
    m, n = len(grid), len(grid[0])
    while 0 <= row < m and 0 <= col < n:
        if grid[row][col] == "#":
            row -= dr
            col -= dc
            dr, dc = dc, -dr
            continue
        grid[row][col] = "X"
        row += dr
        col += dc

    return sum(cell == "X" for row_cells in grid for cell in row_cells)


DIRECTIONS = "^>v<"


def check(grid, m, n, row, col, dr, dc, d):
    seen = set()
    while 0 <= row < m and 0 <= col < n:
        # Obstacle
        if grid[row][col] == "#":
            row -= dr
            col -= dc
            dr, dc = dc, -dr
            d = (d + 1) % 4
            row += dr
            col += dc
            continue

        # Move forward
        if (row, col, d) in seen:
            return True
        seen.add((row, col, d))
        row += dr
        col += dc
    return False


@timeit
def part_2(data):
    start_row, start_col = next(
        (row, col) for row, row_cells in enumerate(data) for col, cell in enumerate(row_cells) if cell == "^"
    )

    m, n = len(data), len(data[0])
    grid = [list(line) for line in data]
    row, col, d, dr, dc = start_row, start_col, 0, -1, 0
    new_obstacles = {(start_row, start_col)}
    while 0 <= row < m and 0 <= col < n:
        # Obstacle
        if grid[row][col] == "#":
            row -= dr
            col -= dc
            dr, dc = dc, -dr
            d = (d + 1) % 4
            row += dr
            col += dc
            continue
        # New Obstacle
        if (row, col) not in new_obstacles:
            old_cell = grid[row][col]
            grid[row][col] = "#"
            if check(grid, m, n, start_row, start_col, -1, 0, 0):
                new_obstacles.add((row, col))
            grid[row][col] = old_cell

        # Move forward
        grid[row][col] = DIRECTIONS[d]
        row += dr
        col += dc

    return len(new_obstacles) - 1


def main():
    setup_logging()
    with (files("data.inputs") / "day_06.txt").open() as input_file:
        data = get_data(input_file)
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
