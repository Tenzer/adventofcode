#!/usr/bin/env python3

import fileinput
from collections import Counter


def main():
    two_letters = 0
    three_letters = 0
    counter = Counter()

    for line in fileinput.input():
        counter.update(line)

        if 2 in counter.values():
            two_letters += 1
        if 3 in counter.values():
            three_letters += 1

        counter.clear()

    print(two_letters * three_letters)


if __name__ == "__main__":
    main()
