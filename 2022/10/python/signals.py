#!/usr/bin/env python3

import fileinput


def add_to_result(current_cycle: int, x_value: int) -> int:
    if current_cycle not in {20, 60, 100, 140, 180, 220}:
        return 0

    return current_cycle * x_value


def part1() -> None:
    current_cycle = 0
    X = 1
    result = 0

    for line in fileinput.input():
        current_cycle += 1
        arguments = line.strip().split()

        if arguments[0] == "noop":
            result += add_to_result(current_cycle, X)
        elif arguments[0] == "addx":
            result += add_to_result(current_cycle, X)
            current_cycle += 1
            result += add_to_result(current_cycle, X)
            X += int(arguments[1])

    print(result)


def draw_pixel(current_cycle: int, x_value: int) -> None:
    pixel = (current_cycle - 1) % 40
    if x_value + 1 >= pixel >= x_value - 1:
        print("#", end="")
    else:
        print(".", end="")

    if pixel == 39:
        print()


def part2() -> None:
    current_cycle = 0
    X = 1

    for line in fileinput.input():
        current_cycle += 1
        arguments = line.strip().split()

        if arguments[0] == "noop":
            draw_pixel(current_cycle, X)
        elif arguments[0] == "addx":
            draw_pixel(current_cycle, X)
            current_cycle += 1
            draw_pixel(current_cycle, X)
            X += int(arguments[1])


if __name__ == "__main__":
    part1()
    part2()
