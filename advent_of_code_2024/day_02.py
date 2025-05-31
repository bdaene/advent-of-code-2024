from importlib.resources import files

from advent_of_code_2024.utils import timeit, setup_logging


@timeit
def get_data(input_file):
    return [list(map(int, line.split())) for line in input_file]


def is_safe(report, allowed_bad_levels=0):
    report = reversed(report)
    last_level = next(report)
    for level in report:
        if 1 <= level - last_level <= 3:
            last_level = level
        elif allowed_bad_levels <= 0:
            return False
        else:
            allowed_bad_levels -= 1
    return True


@timeit
def part_1(data):
    return sum(is_safe(report) or is_safe(report[::-1]) for report in data)


@timeit
def part_2(data, allowed_bad_levels=1):
    count = 0
    for report in data:
        reversed_report = report[::-1]
        for skip in range(allowed_bad_levels + 1):
            if is_safe(report, allowed_bad_levels - skip) or is_safe(reversed_report, allowed_bad_levels - skip):
                count += 1
                break
            report.pop()
            reversed_report.pop()
    return count


def main():
    setup_logging()
    with (files("data.inputs") / "day_02.txt").open() as input_file:
        data = get_data(input_file)
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
