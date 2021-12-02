#!/usr/bin/env python3

import fileinput


def part1() -> None:
    horizontal = 0
    depth = 0

    for i in fileinput.input():
        direction, amount_str = i.split(" ", 1)
        amount = int(amount_str)

        if direction == "forward":
            horizontal += amount
        elif direction == "up":
            depth -= amount
        elif direction == "down":
            depth += amount

    print(f"Part 1: {horizontal * depth}")


def part2() -> None:
    horizontal = 0
    depth = 0
    aim = 0

    for i in fileinput.input():
        direction, amount_str = i.split(" ", 1)
        amount = int(amount_str)

        if direction == "forward":
            horizontal += amount
            depth += aim * amount
        elif direction == "up":
            aim -= amount
        elif direction == "down":
            aim += amount

    print(f"Part 2: {horizontal * depth}")

if __name__ == "__main__":
    part1()
    part2()
