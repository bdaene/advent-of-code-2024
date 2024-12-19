from heapq import heappop, heappush
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
def part_1(data, size=70, nb_bytes=1024):
    size += 1
    corrupted = [[False for col in range(size)] for row in range(size)]
    for x, y in data[:nb_bytes]:
        corrupted[y][x] = True

    # print()
    # print("\n".join("".join("#" if cell else "." for cell in line) for line in corrupted))

    return get_nb_steps(corrupted, size)


def get_first_obstacle(obstacles, size):
    inf = len(obstacles)
    target = size
    size += 1

    corrupted_time = [[inf for col in range(size)] for row in range(size)]
    for i, (x, y) in enumerate(obstacles):
        corrupted_time[y][x] = i

    unreachable_time: list[list[int | None]]
    unreachable_time = [[inf + 1 for col in range(size)] for row in range(size)]
    unreachable_time[0][0] = corrupted_time[0][0]
    to_visit = [(-unreachable_time[0][0], 0, 0)]
    while to_visit:
        first_obstacle, row, col = heappop(to_visit)
        first_obstacle = -first_obstacle
        assert all(row_ != row or col_ != col for first_obstacle_, row_, col_ in to_visit)
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            row_, col_ = row + dr, col + dc
            if 0 <= row_ < size and 0 <= col_ < size and unreachable_time[row_][col_] > inf:
                first_obstacle_ = min(first_obstacle, corrupted_time[row_][col_])
                unreachable_time[row_][col_] = first_obstacle_
                heappush(to_visit, (-first_obstacle_, row_, col_))
                if row_ == target and col_ == target:
                    to_visit.clear()
                    break

    # from matplotlib import pyplot
    # fig, axes = pyplot.subplots(1, 2)
    # axes[0].imshow(corrupted_time, cmap='hot_r')
    # image = axes[1].imshow(unreachable_time, cmap='hot_r')
    # axes[0].set_title("Time of byte fall")
    # axes[1].set_title("Maximum reachable time")
    # fig.colorbar(image, ax=axes, shrink=0.5)
    # pyplot.show()

    return unreachable_time


@timeit
def part_2(data, size=70):
    return data[get_first_obstacle(data, size)[size][size]]


def main():
    setup_logging()
    with (files("data.inputs") / "day_18.txt").open() as input_file:
        data = get_data(input_file)
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
