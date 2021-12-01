#!/usr/bin/env python3

import fileinput
from collections import Counter


def parse_spec(spec):
    spec = spec.strip().split(" ")
    identifier = spec[0].lstrip("#")
    offsets = spec[2].strip(":").split(",")
    sizes = spec[3].split("x")

    return (
        int(identifier),
        (int(offsets[0]), int(offsets[1])),
        (int(sizes[0]), int(sizes[1])),
    )


def generate_coords(offsets, size):
    for x in range(size[0]):
        for y in range(size[1]):
            # Tuples are a bit faster than strings but use more memory 🤔
            yield x + offsets[0], y + offsets[1]
            # yield f"{x + offsets[0]}_{y + offsets[1]}"


def part1():
    counter = Counter()

    for line in fileinput.input():
        _, offsets, size = parse_spec(line)

        for coord in generate_coords(offsets, size):
            counter[coord] += 1

    print("Part 1:", len([i for i in counter.values() if i > 1]))


def part2():
    counter = Counter()
    claims = dict()

    for line in fileinput.input():
        claim_id, offsets, size = parse_spec(line)
        claims[claim_id] = offsets, size

        for coord in generate_coords(offsets, size):
            counter[coord] += 1

    single_squares = set()
    for key, value in counter.items():
        if value == 1:
            single_squares.add(key)

    for claim_id, spec in claims.items():
        coords = set(generate_coords(*spec))
        if coords.issubset(single_squares):
            print("Part 2:", claim_id)


if __name__ == "__main__":
    part1()
    part2()
