#!/usr/bin/env python3

import fileinput


def calc_fuel_used(crabs: list[int], target: int) -> int:
    fuel = 0

    for crab in crabs:
        fuel += abs(crab - target)

    return fuel


def part1() -> None:
    input_line = list(fileinput.input())[0].strip()
    crabs: list[int] = []

    for i_str in input_line.split(","):
        crabs.append(int(i_str))

    min_pos = min(crabs)
    max_pos = max(crabs)

    fuel_used: dict[int, int] = {}
    for i in range(min_pos, max_pos + 1):
        fuel = 0

        for crab in crabs:
            fuel += abs(crab - i)

        fuel_used[i] = fuel

    print(f"Part 1: {min(fuel_used.values())}")


def part2() -> None:
    input_line = list(fileinput.input())[0].strip()
    crabs: list[int] = []

    for i_str in input_line.split(","):
        crabs.append(int(i_str))

    min_pos = min(crabs)
    max_pos = max(crabs)

    fuel_used: dict[int, int] = {}
    for i in range(min_pos, max_pos + 1):
        fuel = 0

        for crab in crabs:
            diff = abs(crab - i)
            fuel += diff * (1 + diff) // 2

        fuel_used[i] = fuel

    print(f"Part 2: {min(fuel_used.values())}")


if __name__ == "__main__":
    part1()
    part2()
