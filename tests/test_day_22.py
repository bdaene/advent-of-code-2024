from importlib.resources import files

from advent_of_code_2024.day_22 import get_data, get_next, part_1, part_2

DATA = [1, 10, 100, 2024]


def test_get_data():
    with (files("data.samples") / "day_22.txt").open() as input_file:
        data = get_data(input_file)

    assert data == DATA


def test_gen_secret_numbers():
    secret_number, result = 123, []
    for _ in range(10):
        secret_number = get_next(secret_number)
        result.append(secret_number)

    assert result == [
        15887950,
        16495136,
        527345,
        704524,
        1553684,
        12683156,
        11100544,
        12249484,
        7753432,
        5908254,
    ]


def test_part_1():
    result = part_1(DATA)

    assert result == 37327623


def test_part_2():
    result = part_2([1, 2, 3, 2024])

    assert result == 23
