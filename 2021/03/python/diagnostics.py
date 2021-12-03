#!/usr/bin/env python3

import fileinput
from collections import Counter


def part1() -> None:
    lines_seen = 0
    counter: Counter[int] = Counter()

    for line in fileinput.input():
        lines_seen += 1

        for index, value in enumerate(line.strip()):
            counter[index] += int(value)

    gamma_str = ""
    epsilon_str = ""
    for index in counter:
        if counter[index] > lines_seen // 2:
            gamma_str += "1"
            epsilon_str += "0"
        else:
            gamma_str += "0"
            epsilon_str += "1"

    print("Part 1:", int(gamma_str, 2) * int(epsilon_str, 2))


def filter_lines(lines: list[str], bitpos: int, most_significant: bool) -> list[str]:
    zeroes: list[str] = []
    ones: list[str] = []

    for line in lines:
        if line[bitpos] == "0":
            zeroes.append(line)
        else:
            ones.append(line)

    zeroes_count = len(zeroes)
    ones_count = len(ones)
    if most_significant:
        if zeroes_count > ones_count:
            return zeroes
        return ones

    if ones_count < zeroes_count:
        return ones
    return zeroes


def part2() -> None:
    all_lines: list[str] = []

    for line in fileinput.input():
        if line.strip():
            all_lines.append(line.strip())

    bits = len(all_lines[0])

    # oxygen generator rating
    oxygen_lines = all_lines
    oxygen_generator_rating: int
    for bit in range(bits):
        oxygen_lines = filter_lines(oxygen_lines, bitpos=bit, most_significant=True)
        if len(oxygen_lines) == 1:
            oxygen_generator_rating = int(oxygen_lines[0], 2)
            break

    # co2 scrubber rating
    co2_lines = all_lines
    co2_scrubber_rating: int
    for bit in range(bits):
        co2_lines = filter_lines(co2_lines, bitpos=bit, most_significant=False)
        if len(co2_lines) == 1:
            co2_scrubber_rating = int(co2_lines[0], 2)
            break

    print(f"Part 2: {oxygen_generator_rating * co2_scrubber_rating}")

if __name__ == "__main__":
    part1()
    part2()
