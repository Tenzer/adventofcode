#!/usr/bin/env python3

import fileinput
from collections import Counter
from collections.abc import Sequence


def get_range(start: str, end: str) -> Sequence[int]:
    start_int = int(start)
    end_int = int(end)

    if start_int <= end_int:
        return range(start_int, end_int + 1)

    return range(start_int, end_int - 1, -1)


def part1() -> None:
    counter: Counter[str] = Counter()

    for line in fileinput.input():
        start, end = line.strip().split(" -> ", 2)
        start_x, start_y = start.split(",", 2)
        end_x, end_y = end.split(",", 2)

        if start_x != end_x and start_y != end_y:
            # Skip lines that aren't either horizontal or vertical
            continue

        x_range = get_range(start_x, end_x)
        y_range = get_range(start_y, end_y)

        for x in x_range:
            for y in y_range:
                counter[f"{x}_{y}"] += 1

    overlapping_spots = 0
    for count in counter.values():
        if count >= 2:
            overlapping_spots += 1

    print(f"Part 1: {overlapping_spots}")


def part2() -> None:
    counter: Counter[str] = Counter()

    for line in fileinput.input():
        start, end = line.strip().split(" -> ", 2)
        start_x, start_y = start.split(",", 2)
        end_x, end_y = end.split(",", 2)

        x_range = get_range(start_x, end_x)
        y_range = get_range(start_y, end_y)

        if start_x == end_x or start_y == end_y:
            for x in x_range:
                for y in y_range:
                    counter[f"{x}_{y}"] += 1
        else:
            for x, y in zip(x_range, y_range):
                counter[f"{x}_{y}"] += 1

    overlapping_spots = 0
    for count in counter.values():
        if count >= 2:
            overlapping_spots += 1

    print(f"Part 2: {overlapping_spots}")


if __name__ == "__main__":
    part1()
    part2()
