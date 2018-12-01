#!/usr/bin/env python3

import fileinput


def main():
    output = 0
    seen_frequencies = set()
    keep_going = True

    while keep_going:
        for i in fileinput.input():
            if i[0] == "+":
                output += int(i[1:])
            elif i[0] == "-":
                output -= int(i[1:])

            if output in seen_frequencies:
                keep_going = False
                break

            seen_frequencies.add(output)

    print(output)


if __name__ == "__main__":
    main()
