#!/usr/bin/env python3

import fileinput


def part1() -> None:
    fish: list[int] = []
    input_data = "\n".join(fileinput.input()).strip()

    for i_str in input_data.split(","):
        fish.append(int(i_str))

    days = 80
    while days:
        new_fish: list[int] = []
        for i in fish:
            if i == 0:
                # Existing fish resets
                new_fish.append(6)
                # New fish appears
                new_fish.append(8)
            else:
                new_fish.append(i - 1)

        days -= 1
        fish = new_fish

    print("Part 1:", len(fish))


def part2() -> None:
    """
    Very inspired by https://www.reddit.com/r/adventofcode/comments/r9z49j/comment/hnfaisu/.
    """

    input_data = "\n".join(fileinput.input()).strip()
    initial_fish = list(map(int, input_data.split(",")))

    # Count the number of initial at each state
    fish = [initial_fish.count(i) for i in range(9)]

    days = 256
    while days:
        # Get the number of fish that are going to give birth, and move all other fish closer to it
        breeding_fish = fish.pop(0)

        # Bring the fish that have given birth back into the list
        fish[6] += breeding_fish

        # Add the newly born fish
        fish.append(breeding_fish)

        days -= 1

    print("Part 2:", sum(fish))


if __name__ == "__main__":
    part1()
    part2()
