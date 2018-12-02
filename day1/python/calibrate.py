#!/usr/bin/env python3

import fileinput


def adjust(current, change):
    return current + int(change)


def part1():
    frequency = 0

    for i in fileinput.input():
        frequency = adjust(frequency, i)

    print("Part 1:", frequency)


def part2():
    frequency = 0
    past_frequencies = set()

    while True:
        for i in fileinput.input():
            frequency = adjust(frequency, i)

            if frequency in past_frequencies:
                print("Part 2:", frequency)
                return

            past_frequencies.add(frequency)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
