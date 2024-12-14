from collections import deque
from heapq import heapify, heappop, heappush
from importlib.resources import files

from advent_of_code_2024.utils import timeit, setup_logging


@timeit
def get_data(input_file):
    return list(map(int, input_file.readline().strip()))


def compute_prefix_sum(length_limit):
    prefix_sum, s = [0], 0
    for length in range(0, LENGTH_LIMIT):
        s += length
        prefix_sum.append(s)
    return prefix_sum


LENGTH_LIMIT = 10
PREFIX_SUM = compute_prefix_sum(LENGTH_LIMIT)


@timeit
def part_1(data):
    blocks = deque(enumerate(data[::2]))
    empty_spaces = data[1::2][::-1]

    data = []
    start, total = 0, 0
    while blocks:
        block_id, block_length = blocks.popleft()
        total += block_id * (start * block_length + PREFIX_SUM[block_length])
        # data.append(str(block_id)[-1]*block_length)
        start += block_length

        space_length = empty_spaces.pop()
        while blocks and space_length > 0:
            block_id, block_length = blocks.pop()
            if space_length >= block_length:
                total += block_id * (start * block_length + PREFIX_SUM[block_length])
                # data.append(str(block_id)[-1] * block_length)
                start += block_length
                space_length -= block_length
            else:
                total += block_id * (start * space_length + PREFIX_SUM[space_length])
                # data.append(str(block_id)[-1] * space_length)
                start += space_length
                blocks.append((block_id, block_length - space_length))
                space_length = 0

    # print(''.join(data))
    return total


@timeit
def part_2(data):
    data_starts, data_lengths = [], []
    empty_spaces = [[] for length in range(LENGTH_LIMIT)]

    start = 0
    for i, length in enumerate(data):
        if i % 2:
            empty_spaces[length].append(start)
        else:
            data_starts.append(start)
            data_lengths.append(length)
        start += length

    for spaces in empty_spaces:
        heapify(spaces)

    for block_id in range(len(data_starts) - 1, -1, -1):
        block_start, block_length = data_starts[block_id], data_lengths[block_id]
        best = (block_start, None, None)
        for space_length in range(block_length, LENGTH_LIMIT):
            spaces = empty_spaces[space_length]
            if spaces and spaces[0] < best[0]:
                best = (spaces[0], space_length, spaces)
        space_start, space_length, spaces = best
        if spaces is None:
            continue
        heappop(spaces)
        data_starts[block_id] = space_start
        heappush(empty_spaces[space_length - block_length], space_start + block_length)

    # data = ['.'] * sum(data)
    total = 0
    for block_id, (block_start, block_length) in enumerate(zip(data_starts, data_lengths)):
        total += block_id * (block_start * block_length + PREFIX_SUM[block_length])
        # data[block_start:block_start+block_length] = str(block_id)[-1] * block_length

    # print(''.join(data))
    return total


def main():
    setup_logging()
    with (files("data.inputs") / "day_09.txt").open() as input_file:
        data = get_data(input_file)
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
