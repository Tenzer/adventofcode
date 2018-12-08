#!/usr/bin/env python3

import fileinput
from collections import Counter
from string import ascii_lowercase


def is_match(a, b):
    if a.lower() == b.lower():
        if a.islower() and b.isupper() or a.isupper() and b.islower():
            return True

    return False


def reduce(polymer):
    i = 0
    while True:
        try:
            if not is_match(polymer[i], polymer[i + 1]):
                i += 1
                continue
        except IndexError:
            return polymer

        polymer = polymer[:i] + polymer[i + 2 :]
        if i > 0:
            i -= 1


def part1():
    polymer = ""

    for line in fileinput.input():
        polymer = line.strip()

    polymer = reduce(polymer)
    print("Part 1:", len(polymer))


def part2():
    root_polymer = ""
    counts = Counter()

    for line in fileinput.input():
        root_polymer = line.strip()

    for letter in ascii_lowercase:
        polymer = "".join(i for i in root_polymer if i.lower() != letter)

        counts[letter] += len(reduce(polymer))

    print("Part 2:", counts.most_common()[-1][1])


if __name__ == "__main__":
    part1()
    part2()
