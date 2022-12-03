#!/usr/bin/env python3

import fileinput
from itertools import islice


# Padded with underscore to make the scores right
priority_lookup = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def batched(iterable, n):
    """Batch data into lists of length n. The last batch may be shorter.

    Taken from https://docs.python.org/3/library/itertools.html."""
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while (batch := list(islice(it, n))):
        yield batch


def part1() -> None:
    total_priority = 0

    for line in fileinput.input():
        line = line.strip()
        line_midpoint = int(len(line) / 2)
        compartment_1 = set(line[:line_midpoint])
        compartment_2 = set(line[line_midpoint:])

        common = compartment_1.intersection(compartment_2)
        assert len(common) == 1
        total_priority += priority_lookup.find(list(common)[0])

    print(total_priority)


def part2() -> None:
    total_priority = 0

    for lines in batched(fileinput.input(), 3):
        line_1, line_2, line_3 = set(lines[0].strip()), set(lines[1].strip()), set(lines[2].strip())
        common = line_1.intersection(line_2, line_3)
        assert len(common) == 1
        total_priority += priority_lookup.find(list(common)[0])

    print(total_priority)


if __name__ == "__main__":
    part1()
    part2()
