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
    for a in graph:
        chief_a = a[0] == "t"
        for b in graph[a]:
            if b <= a:
                continue
            chief_b = chief_a or b[0] == "t"
            for c in graph[b]:
                if c <= b:
                    continue
                chief_c = chief_b or c[0] == "t"
                if chief_c and a in graph[c]:
                    # print(a, b, c)
                    count += 1

    return count


@timeit
def part_2(data):
    graph = defaultdict(set)
    for a, b in data:
        graph[a].add(b)
        graph[b].add(a)

    def gen_maximal_cliques(candidates, connected, rejected):
        if not candidates:
            if not rejected:
                yield connected
            return

        u = min(candidates)
        for candidate in sorted(candidates - graph[u]):
            yield from gen_maximal_cliques(
                candidates & graph[candidate], connected + (candidate,), rejected & graph[candidate]
            )
            candidates.remove(candidate)
            rejected.add(candidate)

    best = ()
    for connected_nodes in gen_maximal_cliques(set(graph), (), set()):
        if len(connected_nodes) > len(best):
            best = connected_nodes
            # print(connected_nodes)

    return ",".join(sorted(best))


def main():
    setup_logging()
    with (files("data.inputs") / "day_23.txt").open() as input_file:
        data = get_data(input_file)
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
