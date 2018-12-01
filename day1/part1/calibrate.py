#!/usr/bin/env python3

import fileinput


def main():
    output = 0

    for i in fileinput.input():
        if i[0] == "+":
            output += int(i[1:])
        elif i[0] == "-":
            output -= int(i[1:])

    print(output)


if __name__ == "__main__":
    main()
