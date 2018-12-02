#!/usr/bin/env python3

import fileinput


def main():
    found = set()

    for line in fileinput.input():
        line = line.strip()
        found_line = set()

        for index, _ in enumerate(line):
            item = line[:index] + line[index + 1 :]

            if item in found:
                print(item)
                return

            found_line.add(item)

        found.update(found_line)


if __name__ == "__main__":
    main()
