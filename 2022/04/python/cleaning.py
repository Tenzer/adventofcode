#!/usr/bin/env python3

import fileinput


def part1() -> None:
    overlaps = 0

    for line in fileinput.input():
        line = line.strip()
        assignments = line.split(",")
        start_1, end_1 = assignments[0].split("-")
        start_2, end_2 = assignments[1].split("-")

        range1 = set(range(int(start_1), int(end_1) + 1))
        range2 = set(range(int(start_2), int(end_2) + 1))

        if range1.issubset(range2) or range2.issubset(range1):
            overlaps += 1

    print(overlaps)


def part2() -> None:
    overlaps = 0

    for line in fileinput.input():
        line = line.strip()
        assignments = line.split(",")
        start_1, end_1 = assignments[0].split("-")
        start_2, end_2 = assignments[1].split("-")

        range1 = set(range(int(start_1), int(end_1) + 1))
        range2 = set(range(int(start_2), int(end_2) + 1))

        if range1.intersection(range2):
            overlaps += 1

    print(overlaps)


if __name__ == "__main__":
    part1()
    part2()
