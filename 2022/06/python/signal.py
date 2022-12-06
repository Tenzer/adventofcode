#!/usr/bin/env python3

import fileinput


def part1() -> None:
    lines = list(fileinput.input())
    line = lines[0]

    for i in range(4, len(line)):
        subset = line[i - 4:i]
        if len(set(subset)) == 4:
            print(i)
            break


def part2() -> None:
    lines = list(fileinput.input())
    line = lines[0]

    for i in range(14, len(line)):
        subset = line[i - 14:i]
        if len(set(subset)) == 14:
            print(i)
            break


if __name__ == "__main__":
    part1()
    part2()
