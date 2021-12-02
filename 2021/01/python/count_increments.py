#!/usr/bin/env python3

import fileinput
from typing import Optional


def part1() -> None:
    previous: Optional[int] = None
    increments = 0

    for i_str in fileinput.input():
        i = int(i_str)

        if previous is None:
            previous = i
            continue

        if i > previous:
            increments += 1

        previous = i

    print(f"Part 1: {increments}")


def part2() -> None:
    previous_sum: Optional[int] = None
    current_values: list[int] = []
    increments = 0

    puzzle_input = fileinput.input()

    for i_str in next(puzzle_input), next(puzzle_input), next(puzzle_input):
        current_values.append(int(i_str))

    previous_sum = sum(current_values)

    for i_str in puzzle_input:
        i = int(i_str)

        current_values = current_values[1:] + [i]

        if len(current_values) < 3:
            break

        current_sum = sum(current_values)
        if previous_sum is not None and current_sum > previous_sum:
            increments += 1

        previous_sum = current_sum

    print(f"Part 2: {increments}")


if __name__ == "__main__":
    part1()
    part2()
