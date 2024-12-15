from importlib.resources import files

from advent_of_code_2024.utils import timeit, setup_logging


@timeit
def get_data(input_file):
    grid = []
    for line in input_file:
        if line.isspace():
            break
        grid.append(line.strip())
    movements = ""
    for line in input_file:
        movements += line.strip()
    return grid, movements


DIRECTIONS = {
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
    "^": (-1, 0),
}


@timeit
def part_1(data):
    grid, movements = data
    start_row, start_col = next(
        (row, col) for row, line in enumerate(grid) for col, cell in enumerate(line) if cell == "@"
    )
    grid = [list(line) for line in grid]

    row, col = start_row, start_col
    for movement in movements:
        # print(movement)
        dr, dc = DIRECTIONS[movement]
        k = 1
        while grid[row + dr * k][col + dc * k] == "O":
            k += 1
        if grid[row + dr * k][col + dc * k] == "#":
            continue
        grid[row + dr * k][col + dc * k] = "O"
        grid[row + dr][col + dc] = "@"
        grid[row][col] = "."
        row, col = row + dr, col + dc
        # print('\n'.join(''.join(line) for line in grid))

    total = 0
    for row, line in enumerate(grid):
        for col, cell in enumerate(line):
            if cell == "O":
                total += row * 100 + col

    return total


CHANGES = {
    "#": "##",
    "O": "[]",
    ".": "..",
    "@": "@.",
}


@timeit
def part_2(data):
    grid_, movements = data
    grid = []
    for line_ in grid_:
        line = []
        for cell_ in line_:
            line += list(CHANGES[cell_])
        grid.append(line)

    # print('\n'.join(''.join(line) for line in grid))

    start_row, start_col = next(
        (row, col) for row, line in enumerate(grid) for col, cell in enumerate(line) if cell == "@"
    )

    row, col = start_row, start_col
    for movement in movements:
        # print(movement)
        if movement in "<>":
            dc = -1 if movement == "<" else 1
            k = 1
            while grid[row][col + dc * k] in "[]":
                k += 1
            if grid[row][col + dc * k] == "#":
                continue
            while k > 0:
                grid[row][col + dc * k] = grid[row][col + dc * (k - 1)]
                k -= 1
            grid[row][col] = "."
            col += dc
        else:
            dr = -1 if movement == "^" else 1
            collision = False
            k = 1
            cols = [{col}]
            while cols[-1]:
                if any(grid[row + dr * k][c] == "#" for c in cols[-1]):
                    collision = True
                    break
                cols.append({c for c in cols[-1] if grid[row + dr * k][c] in "[]"})
                cols[-1] |= {c - 1 if grid[row + dr * k][c] == "]" else c + 1 for c in cols[-1]}
                k += 1
            if collision:
                continue
            while k > 0:
                for c in cols.pop():
                    grid[row + dr * k][c] = grid[row + dr * (k - 1)][c]
                    grid[row + dr * (k - 1)][c] = "."
                k -= 1
            grid[row][col] = "."
            row += dr

        # print('\n'.join(''.join(line) for line in grid))

    total = 0
    for row, line in enumerate(grid):
        for col, cell in enumerate(line):
            if cell == "[":
                total += row * 100 + col

    return total


def main():
    setup_logging()
    with (files("data.inputs") / "day_15.txt").open() as input_file:
        data = get_data(input_file)
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
