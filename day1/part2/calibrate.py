#!/usr/bin/env python3

import fileinput


def main():
    output = 0
    seen_frequencies = set()

    while True:
        for i in fileinput.input():
            output += int(i)

            if output in seen_frequencies:
                print(output)
                return

            seen_frequencies.add(output)


if __name__ == "__main__":
    main()
