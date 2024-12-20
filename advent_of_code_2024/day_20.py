from collections import defaultdict, Counter
from importlib.resources import files

from advent_of_code_2024.utils import timeit, setup_logging


@timeit
def get_data(input_file):
   return [line.strip() for line in input_file]


def get_times(grid):
   end = next((row, col) for row, line in enumerate(grid) for col, cell in enumerate(line) if cell == 'E')

   times: list[list[int | None]] = [[None for cell in line] for line in grid]
   times[end[0]][end[1]] = 0
   time, to_visit = 0, [end]
   while to_visit:
      time += 1
      to_visit_ = []
      for row, col in to_visit:
         for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            row_, col_ = row + dr, col + dc
            if times[row_][col_] is None and grid[row_][col_] != '#':
               times[row_][col_] = time
               to_visit_.append((row_, col_))
      to_visit = to_visit_

   return times


def count_cheats(grid, cheat_time):
   times = get_times(grid)

   # print()
   # print('\n'.join(''.join('#' if cell is None else str(cell % 10) for cell in line) for line in times))

   cheats_directions = {(dr, dc): dr + dc for dr in range(cheat_time + 1) for dc in range(cheat_time + 1 - dr)}
   cheats_directions |= {(dr, -dc): time for (dr, dc), time in cheats_directions.items()}
   cheats_directions |= {(-dr, dc): time for (dr, dc), time in cheats_directions.items()}

   cheats = Counter()
   for row, line in enumerate(times):
      for col, cell in enumerate(line):
         if cell is None:
            continue
         for (dr, dc), time in cheats_directions.items():
            row_, col_ = row + dr, col + dc
            if 0 <= row_ < len(times) and 0 <= col_ < len(line):
               cell_ = times[row_][col_]
               if cell_ is None:
                  continue
               if cell_ + time < cell:
                  cheats[cell - cell_ - time] += 1

   # for time, count in sorted(cheats.items()):
   #    print(time, count)

   return cheats


@timeit
def part_1(grid, cheat_time=2, minimal_cheat=100):
   cheats = count_cheats(grid, cheat_time)
   return sum(count for time, count in cheats.items() if time >= minimal_cheat)


def main():
   setup_logging()
   with (files("data.inputs") / "day_20.txt").open() as input_file:
      data = get_data(input_file)
   part_1(data)
   part_1(data, cheat_time=20)


if __name__ == "__main__":
   main()
