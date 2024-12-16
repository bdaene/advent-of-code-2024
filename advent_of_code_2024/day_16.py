from heapq import heappop, heappush
from importlib.resources import files

from advent_of_code_2024.utils import timeit, setup_logging


@timeit
def get_data(input_file):
    return [line.strip() for line in input_file]


def dist(a, b):
    ar, ac = a
    br, bc = b
    return abs(br - ar) + abs(bc - ac)


INF = 10**9 + 7


@timeit
def part_1(data):
    grid = data

    start = next((row, col) for row, line in enumerate(grid) for col, cell in enumerate(line) if cell == "S")
    target = next((row, col) for row, line in enumerate(grid) for col, cell in enumerate(line) if cell == "E")
    print(start, target)

    start_direction = (0, 1)
    to_visit = [(dist(start, target), 0, start, (0, 1))]
    seen = {(start, start_direction): 0}
    while to_visit:
        # print(to_visit)
        _, cost, position, direction = heappop(to_visit)
        if position == target:
            return cost
        (row, col), (dr, dc) = position, direction
        for position_, direction_, cost_ in [
            ((row + dr, col + dc), direction, cost + 1),
            (position, (-dc, dr), cost + 1000),
            (position, (dc, -dr), cost + 1000),
        ]:
            row_, col_ = position_
            if grid[row_][col_] != "#" and seen.get((position_, direction_), INF) > cost:
                seen[(position_, direction_)] = cost
                heappush(to_visit, (dist(position_, target) + cost_, cost_, position_, direction_))


DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


@timeit
def part_2(data):
    grid = data

    start = next((row, col) for row, line in enumerate(grid) for col, cell in enumerate(line) if cell == "S")
    target = next((row, col) for row, line in enumerate(grid) for col, cell in enumerate(line) if cell == "E")
    print(start, target)

    to_visit = [(start, 0, 0)]
    costs = [[[INF] * 4 for cell in line] for line in grid]
    costs[start[0]][start[1]][0] = 0
    while to_visit:
        # print(to_visit)
        to_visit_ = []
        for position, direction, cost in to_visit:
            (row, col), (dr, dc) = position, DIRECTIONS[direction]
            for position_, direction_, cost_ in [
                ((row + dr, col + dc), direction, cost + 1),
                (position, (direction + 1) % 4, cost + 1000),
                (position, (direction - 1) % 4, cost + 1000),
            ]:
                (row_, col_) = position_
                if grid[row_][col_] != "#" and costs[row_][col_][direction_] > cost_:
                    costs[row_][col_][direction_] = cost_
                    to_visit_.append((position_, direction_, cost_))
        to_visit = to_visit_

    target_cost = min(costs[target[0]][target[1]][direction] for direction in range(4))

    # print('\n'.join(''.join(str(cost % 10) if (cost := min(cells)) < INF else '#' for cells in line) for line in costs))

    cells = {
        (target, direction, target_cost)
        for direction in range(4)
        if costs[target[0]][target[1]][direction] == target_cost
    }
    best_places = set()
    while cells:
        # print(cells)
        best_places |= {position for position, direction, cost in cells}
        cells_ = set()
        for position, direction, cost in cells:
            (row, col), (dr, dc) = position, DIRECTIONS[direction]
            for position_, direction_, cost_ in [
                ((row - dr, col - dc), direction, cost - 1),
                (position, (direction - 1) % 4, cost - 1000),
                (position, (direction + 1) % 4, cost - 1000),
            ]:
                (row_, col_) = position_
                if costs[row_][col_][direction_] == cost_:
                    cells_.add((position_, direction_, cost_))
        cells = cells_

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
