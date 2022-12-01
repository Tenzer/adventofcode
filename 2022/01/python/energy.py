#!/usr/bin/env python3

import fileinput


def part1() -> None:
    calories = [0]
    for line in fileinput.input():
        line = line.strip()
        if line == "":
            # Next elf
            calories.append(0)
            continue

        calories[-1] += int(line)

    print(max(calories))


def part2() -> None:
    calories = [0]
    for line in fileinput.input():
        line = line.strip()
        if line == "":
            # Next elf
            calories.append(0)
            continue

        calories[-1] += int(line)

    calories.sort()
    print(sum(calories[-3:]))


if __name__ == "__main__":
    part1()
    part2()
