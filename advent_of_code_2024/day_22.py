from collections import Counter, deque
from importlib.resources import files

from advent_of_code_2024.utils import timeit, setup_logging


@timeit
def get_data(input_file):
    return [int(line.strip()) for line in input_file]


MASK = (1 << 24) - 1


def get_next(number):
    number ^= number << 6
    number &= MASK
    number ^= number >> 5
    # number &= MASK
    number ^= number << 11
    number &= MASK
    return number


@timeit
def part_1(data):
    total = 0
    for initial_secret_number in data:
        secret_number = initial_secret_number
        for _ in range(2000):
            secret_number = get_next(secret_number)
        # print(f"{initial_secret_number}: {secret_number}")
        total += secret_number

    return total


@timeit
def part_2(data):
    total_bananas = Counter()
    for initial_secret_number in data:
        bananas = {}
        secret_number = initial_secret_number
        price = secret_number % 10
        changes = deque()
        for _ in range(3):
            secret_number = get_next(secret_number)
            prev_price, price = price, secret_number % 10
            changes.append(price - prev_price)

        for _ in range(2000 - 3):
            secret_number = get_next(secret_number)
            prev_price, price = price, secret_number % 10
            changes.append(price - prev_price)
            bananas.setdefault(tuple(changes), price)
            changes.popleft()
        total_bananas += bananas

    return max(total_bananas.values())


def main():
    setup_logging()
    with (files("data.inputs") / "day_22.txt").open() as input_file:
        data = get_data(input_file)
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
