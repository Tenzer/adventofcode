#!/usr/bin/env python3

import fileinput
from collections import defaultdict
from pathlib import PosixPath

DIRECTORY_LISTING: dict[str, list[int]] = defaultdict(list)


def parse_directories() -> None:
    global DIRECTORY_LISTING
    current_path = PosixPath("/")

    for line in fileinput.input():
        tokens = line.strip().split(" ")

        if tokens[0] == "$" and tokens[1] == "cd":
            current_path = current_path.joinpath(tokens[2]).resolve()
            DIRECTORY_LISTING[str(current_path)].append(0)
            continue

        if tokens[0] == "$" and tokens[1] == "ls":
            continue

        if tokens[0] == "dir":
            continue

        DIRECTORY_LISTING[str(current_path)].append(int(tokens[0]))


def part1() -> None:
    total_size = 0

    for current_path, current_files in DIRECTORY_LISTING.items():
        current_path_size = sum(current_files)

        for path, files in DIRECTORY_LISTING.items():
            if current_path == path:
                continue

            if not path.startswith(f"{current_path}/"):
                continue

            current_path_size += sum(files)

        if current_path_size <= 100_000:
            total_size += current_path_size

    print(total_size)


def part2() -> None:
    space_to_clear = 30_000_000 - (70_000_000 - sum([sum(i) for i in DIRECTORY_LISTING.values()]))
    result = 70_000_000

    for current_path, current_files in DIRECTORY_LISTING.items():
        current_path_size = sum(current_files)

        for path, files in DIRECTORY_LISTING.items():
            if current_path == path:
                continue

            if not path.startswith(f"{current_path}/"):
                continue

            current_path_size += sum(files)

        if result > current_path_size >= space_to_clear:
            result = current_path_size

    print(result)


if __name__ == "__main__":
    parse_directories()
    part1()
    part2()
