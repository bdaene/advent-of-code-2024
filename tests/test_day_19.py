from importlib.resources import files

from advent_of_code_2024.day_19 import get_data, part_1, part_2, Trie

DATA = (
    ("r", "wr", "b", "g", "bwu", "rb", "gb", "br"),
    ("brwrr", "bggr", "gbbr", "rrbgbr", "ubwu", "bwurrg", "brgr", "bbrgwb"),
)


def test_get_data():
    with (files("data.samples") / "day_19.txt").open() as input_file:
        data = get_data(input_file)

    assert data == DATA


def test_trie():
    towels, designs = DATA
    trie = Trie()
    for towel in towels:
        trie.add(towel)
    for design in designs:
        count = trie.count_matches(design)
        splits = trie.split(design)
        assert count == len(splits)
        assert all("".join(split) == design for split in splits)


def test_part_1():
    result = part_1(DATA)

    assert result == 6


def test_part_2():
    result = part_2(DATA)

    assert result == 16
