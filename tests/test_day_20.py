from importlib.resources import files

import pytest

from advent_of_code_2024.day_20 import get_data, count_cheats, part_1

DATA = [
    "###############",
    "#...#...#.....#",
    "#.#.#.#.#.###.#",
    "#S#...#.#.#...#",
    "#######.#.#.###",
    "#######.#.#...#",
    "#######.#.###.#",
    "###..E#...#...#",
    "###.#######.###",
    "#...###...#...#",
    "#.#####.#.###.#",
    "#.#...#.#.#...#",
    "#.#.#.#.#.#.###",
    "#...#...#...###",
    "###############",
]


def test_get_data():
    with (files("data.samples") / "day_20.txt").open() as input_file:
        data = get_data(input_file)

    assert data == DATA


@pytest.mark.parametrize(
    "cheat_time, minimal_cheat_time, expected_cheats_count",
    [
        (
            2,
            0,
            {
                2: 14,
                4: 14,
                6: 2,
                8: 4,
                10: 2,
                12: 3,
                20: 1,
                36: 1,
                38: 1,
                40: 1,
                64: 1,
            },
        ),
        (
            20,
            50,
            {
                50: 32,
                52: 31,
                54: 29,
                56: 39,
                58: 25,
                60: 23,
                62: 20,
                64: 19,
                66: 12,
                68: 14,
                70: 12,
                72: 22,
                74: 4,
                76: 3,
            },
        ),
    ],
)
def test_count_cheats(cheat_time, minimal_cheat_time, expected_cheats_count):
    cheats_count = count_cheats(DATA, cheat_time)
    filtered_cheats_count = {time: count for time, count in cheats_count.items() if time >= minimal_cheat_time}

    assert filtered_cheats_count == expected_cheats_count


def test_part_1():
    result = part_1(DATA, max_cheat_time=20, minimal_cheat=50)

    assert result == 32 + 31 + 29 + 39 + 25 + 23 + 20 + 19 + 12 + 14 + 12 + 22 + 4 + 3
