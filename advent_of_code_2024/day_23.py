from collections import defaultdict
from importlib.resources import files

from advent_of_code_2024.utils import timeit, setup_logging


@timeit
def get_data(input_file):
    return [tuple(line.strip().split("-")) for line in input_file]


@timeit
def part_1(data):
    graph = defaultdict(set)
    for a, b in data:
        graph[a].add(b)
        graph[b].add(a)

    count = 0
    for a in sorted(graph):
        for b in graph[a]:
            if b <= a:
                continue
            for c in graph[a] & graph[b]:
                if c <= b:
                    continue
                # print(a, b, c)
                count += any(node.startswith("t") for node in (a, b, c))

    return count


@timeit
def part_2(data):
    graph = defaultdict(set)
    for a, b in data:
        graph[a].add(b)
        graph[b].add(a)

    def get_fully_connected(candidates, connected_nodes=()):
        if not candidates:
            yield connected_nodes
            return

        while candidates:
            candidate = min(candidates)
            for new_connected_nodes in get_fully_connected(
                candidates & graph[candidate], connected_nodes + (candidate,)
            ):
                yield new_connected_nodes
                candidates -= set(new_connected_nodes)

    best = ()
    for connected_nodes in get_fully_connected(set(graph)):
        if len(connected_nodes) > len(best):
            best = connected_nodes
            # print(connected_nodes)

    return ",".join(best)


def main():
    setup_logging()
    with (files("data.inputs") / "day_23.txt").open() as input_file:
        data = get_data(input_file)
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
