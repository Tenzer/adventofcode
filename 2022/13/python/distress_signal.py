#!/usr/bin/env python3

import fileinput
import itertools
from functools import cmp_to_key


def check_order(left: list, right: list) -> int:
    for l, r in itertools.zip_longest(left, right):
        if isinstance(l, int) and not isinstance(r, int):
            l = [l]
        elif isinstance(r, int) and not isinstance(l, int):
            r = [r]

        if isinstance(l, int) and isinstance(r, int):
            if l < r:
                return -1
            if r < l:
                return 1

        if l is None and r is not None:
            return -1
        if r is None and l is not None:
            return 1

        if isinstance(l, list) and isinstance(r, list):
            result = check_order(l, r)
            if result != 0:
                return result

    return 0


def part1() -> None:
    lines = list(fileinput.input())
    result = 0

    for line_index in range(0, len(lines), 3):
        left = eval(lines[line_index])
        right = eval(lines[line_index + 1])

        if check_order(left, right) == -1:
            result += line_index // 3 + 1

    print(result)


def part2() -> None:
    lines = [[[2]], [[6]]]

    for line in fileinput.input():
        line = line.strip()
        if not line:
            continue
        lines.append(eval(line))

    lines.sort(key=cmp_to_key(check_order))
    two_index = lines.index([[2]]) + 1
    six_index = lines.index([[6]]) + 1
    print(two_index * six_index)


if __name__ == "__main__":
    part1()
    part2()
