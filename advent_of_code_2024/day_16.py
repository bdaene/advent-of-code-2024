from heapq import heappush, heappop
from importlib.resources import files

from advent_of_code_2024.utils import timeit, setup_logging


@timeit
def get_data(input_file):
    return [line.strip() for line in input_file]


INF = 10**9 - 1
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def extract_position(grid, cell_value):
    return next((row, col) for row, line in enumerate(grid) for col, cell in enumerate(line) if cell == cell_value)


def compute_costs(grid, start):
    start_row, start_col = start

    costs = [[[INF] * 4 for cell in line] for line in grid]  # costs[row][col]dir]
    costs[start_row][start_col][0] = 0

    to_visit = [(0, start, 0), (2000, start, 2)]
    while to_visit:
        cost, position, direction = heappop(to_visit)
        (row, col) = position
        for direction_, cost_ in [
            (direction, cost + 1),
            ((direction + 1) % 4, cost + 1001),
            ((direction - 1) % 4, cost + 1001),
        ]:
            dr_, dc_ = DIRECTIONS[direction_]
            row_, col_ = row + dr_, col + dc_
            if grid[row_][col_] != "#" and costs[row_][col_][direction_] > cost_:
                costs[row_][col_][direction_] = cost_
                heappush(to_visit, (cost_, (row_, col_), direction_))

    return costs


@timeit
def part_1(data):
    grid = data

    start = extract_position(grid, "S")
    end = extract_position(grid, "E")

    costs = compute_costs(grid, start)

    end_row, end_col = end
    return min(costs[end_row][end_col][direction] for direction in range(4))


@timeit
def part_2(data):
    grid = data

    start = extract_position(grid, "S")
    end = extract_position(grid, "E")

    costs = compute_costs(grid, start)
    # print('\n'.join(''.join(str(cost % 10) if (cost := min(cells)) < INF else '#' for cells in line) for line in costs))

    end_row, end_col = end
    end_cost = min(costs[end_row][end_col][direction] for direction in range(4))

    best_places = set()
    best_paths = {(end, direction, end_cost) for direction in range(4) if costs[end[0]][end[1]][direction] == end_cost}
    while best_paths:
        # print(best_paths)
        best_places |= {position for position, direction, cost in best_paths}
        best_paths_ = set()
        for position, direction, cost in best_paths:
            (row, col), (dr, dc) = position, DIRECTIONS[direction]
            row_, col_ = row - dr, col - dc
            for direction_, cost_ in [
                (direction, cost - 1),
                ((direction - 1) % 4, cost - 1001),
                ((direction + 1) % 4, cost - 1001),
            ]:
                if costs[row_][col_][direction_] == cost_:
                    best_paths_.add(((row_, col_), direction_, cost_))
        best_paths = best_paths_

    # print('\n'.join(''.join('O' if (row, col) in best_places else cell for col, cell in enumerate(line)) for row, line in enumerate(grid)))

    return len(best_places)


def main():
    setup_logging()
    with (files("data.inputs") / "day_16.txt").open() as input_file:
        data = get_data(input_file)
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
