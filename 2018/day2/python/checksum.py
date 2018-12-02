#!/usr/bin/env python3

import fileinput
from collections import Counter


def part1():
    two_letters = 0
    three_letters = 0
    counter = Counter()

    for line in fileinput.input():
        counter.update(line)

        if 2 in counter.values():
            two_letters += 1
        if 3 in counter.values():
            three_letters += 1

        counter.clear()

    print("Part 1:", two_letters * three_letters)


def part2():
    found = set()

    for line in fileinput.input():
        line = line.strip()
        found_line = set()

        for index, _ in enumerate(line):
            item = line[:index] + line[index + 1 :]

            if item in found:
                print("Part 2:", item)
                return

            found_line.add(item)

        found.update(found_line)


if __name__ == "__main__":
    part1()
    part2()
