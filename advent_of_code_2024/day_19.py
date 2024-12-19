from collections import Counter, defaultdict
from importlib.resources import files

from advent_of_code_2024.utils import timeit, setup_logging


@timeit
def get_data(input_file):
    towels = tuple(input_file.readline().strip().split(", "))
    input_file.readline()
    designs = tuple(line.strip() for line in input_file)
    return towels, designs


class Trie:
    def __init__(self):
        self.nodes = [{}]
        self.patterns = [None]

    def add(self, string):
        node_id = 0
        for c in string:
            if c not in self.nodes[node_id]:
                self.nodes[node_id][c] = len(self.nodes)
                self.patterns.append(None)
                self.nodes.append({})
            node_id = self.nodes[node_id][c]
        self.nodes[node_id]["$"] = 1
        self.patterns[node_id] = string

    def count_matches(self, string):
        nodes = Counter({0: 1})
        for c in string:
            nodes_ = Counter()
            for node_id, count in nodes.items():
                if c in self.nodes[node_id]:
                    nodes_[self.nodes[node_id][c]] += count
            root = 0
            for node_id, count in nodes_.items():
                root += self.nodes[node_id].get("$", 0) * count
            nodes_[0] += root
            nodes = nodes_

        return nodes[0]

    def split(self, string):
        nodes = {0: [()]}
        for c in string:
            nodes_ = defaultdict(list)
            for node_id, splits in nodes.items():
                if c in self.nodes[node_id]:
                    nodes_[self.nodes[node_id][c]] += splits
            root = []
            for node_id, splits in nodes_.items():
                if (pattern := self.patterns[node_id]) is not None:
                    root += [split + (pattern,) for split in splits]
            nodes_[0] += root
            nodes = nodes_

        return nodes[0]


@timeit
def part_1(data):
    towels, designs = data

    trie = Trie()
    for towel in towels:
        trie.add(towel)

    return sum(trie.count_matches(design) > 0 for design in designs)


@timeit
def part_2(data):
    towels, designs = data

    trie = Trie()
    for towel in towels:
        trie.add(towel)

    return sum(trie.count_matches(design) for design in designs)


def main():
    setup_logging()
    with (files("data.inputs") / "day_19.txt").open() as input_file:
        data = get_data(input_file)
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
