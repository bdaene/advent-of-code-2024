from importlib.resources import files

from advent_of_code_2024.utils import timeit, setup_logging


@timeit
def get_data(input_file):
    return [int(line.strip()) for line in input_file]


MASK = (1 << 24) - 1


def get_next(secret_number):
    secret_number ^= secret_number << 6
    secret_number &= MASK
    secret_number ^= secret_number >> 5
    # number &= MASK
    secret_number ^= secret_number << 11
    secret_number &= MASK
    return secret_number


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
    changes_modulo = 20**4
    seen_changes = [0] * changes_modulo
    total_bananas = [0] * changes_modulo
    for i, initial_secret_number in enumerate(data, 1):
        changes = 0
        secret_number = initial_secret_number
        price = secret_number % 10
        for _ in range(2000):
            # Update secret number
            secret_number ^= secret_number << 6
            secret_number &= MASK
            secret_number ^= secret_number >> 5
            # number &= MASK  # Not needed
            secret_number ^= secret_number << 11
            secret_number &= MASK

            prev_price, price = price, secret_number % 10
            changes = (changes * 20) % changes_modulo
            changes += 10 + price - prev_price
            if price >= prev_price and seen_changes[changes] < i:
                seen_changes[changes] = i
                total_bananas[changes] += price

    # print(sum(c > 0 for c in total_bananas) / changes_modulo)
    # print(nlargest(20, range(len(total_bananas)), key=total_bananas.__getitem__))
    return max(total_bananas)


def main():
    setup_logging()
    with (files("data.inputs") / "day_22.txt").open() as input_file:
        data = get_data(input_file)
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
