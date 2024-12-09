from collections import deque, defaultdict
from dataclasses import dataclass
from importlib.resources import files

from advent_of_code_2024.utils import timeit, setup_logging


@timeit
def get_data(input_file):
    return list(map(int, input_file.readline().strip()))


@timeit
def part_1(data):
    if len(data) % 2 != 1:
        data.pop()

    queue = deque(data)
    l, r = 0, len(data) // 2
    i, total = 0, 0
    while queue:
        a = queue.popleft()
        total += sum(l * j for j in range(i, i + a))
        print(str(l) * a, end="")
        i += a
        l += 1

        if queue:
            a = queue.popleft()
            while a > 0:
                b = queue.pop()
                if b <= a:
                    total += sum(r * j for j in range(i, i + b))
                    print(str(r) * b, end="")
                    i += b
                    r -= 1
                    queue.pop()
                    a -= b
                else:
                    total += sum(r * j for j in range(i, i + a))
                    print(str(r) * a, end="")
                    i += a
                    queue.append(b - a)
                    a = 0
    print()
    return total


@dataclass
class Block:
    id: str
    length: int


@timeit
def part_2(data):
    data = [
        Block(str(i // 2), a) if i % 2 == 0 else Block(".", a)
        for i, a in enumerate(data)
    ]
    r = len(data)
    while r > 0:
        r -= 1
        if data[r].id == ".":
            continue
        block = data[r]
        l = next(
            (
                l
                for l, b in enumerate(data[:r])
                if b.id == "." and b.length >= block.length
            ),
            None,
        )
        if l is None:
            continue

        b = data[l]
        if b.length > block.length:
            data.insert(l + 1, Block(".", b.length - block.length))
            b.length = block.length
            r += 1
        b.id = block.id
        block.id = "."
        if data[r - 1].id == ".":
            b = data.pop(r - 1)
            block.length += b.length
            r -= 1
        if r + 1 < len(data) and data[r + 1].id == ".":
            b = data.pop(r + 1)
            block.length += b.length

    i, total = 0, 0
    for block in data:
        print(block.id[-1] * block.length, end="")
        if block.id != ".":
            total += sum(j * int(block.id) for j in range(i, i + block.length))
        i += block.length

    return total


def main():
    setup_logging()
    with (files("data.inputs") / "day_09.txt").open() as input_file:
        data = get_data(input_file)
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
