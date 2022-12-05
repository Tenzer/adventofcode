#!/usr/bin/env python3

import copy
import fileinput


starting_position = [
    "_",  # Filler to make up for zero-indexing used in Python
    ["N", "R", "G", "P"],
    ["J", "T", "B", "L", "F", "G", "D", "C"],
    ["M", "S", "V"],
    ["L", "S", "R", "C", "Z", "P"],
    ["P", "S", "L", "V", "C", "W", "D", "Q"],
    ["C", "T", "N", "W", "D", "M", "S"],
    ["H", "D", "G", "W", "P"],
    ["Z", "L", "P", "H", "S", "C", "M", "V"],
    ["R", "P", "F", "L", "W", "G", "Z"],
]


def part1() -> None:
    stacks = copy.deepcopy(starting_position)

    for line in fileinput.input():
        if not line.startswith("move"):
            continue

        line = line.strip()
        _, num, _, source_str, _, destination_str = line.split(" ")
        source, destination = int(source_str), int(destination_str)

        for _ in range(0, int(num)):
            stacks[destination].append(stacks[source].pop())

    print("".join([i[-1] for i in stacks[1:]]))


def part2() -> None:
    stacks = copy.deepcopy(starting_position)

    for line in fileinput.input():
        if not line.startswith("move"):
            continue

        line = line.strip()
        _, num_str, _, source_str, _, destination_str = line.split(" ")
        num, source, destination = int(num_str), int(source_str), int(destination_str)

        stacks[destination] += stacks[source][0 - num:]
        del stacks[source][0 - num:]

    print("".join([i[-1] for i in stacks[1:]]))


if __name__ == "__main__":
    part1()
    part2()
