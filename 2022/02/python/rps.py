#!/usr/bin/env python3

import fileinput


def part1() -> None:
    total_points = 0
    for line in fileinput.input():
        hands = line.strip()

        if hands == "A X":  # draw
            total_points += 1 + 3
        elif hands == "A Y":  # win
            total_points += 2 + 6
        elif hands == "A Z":  # loss
            total_points += 3
        elif hands == "B X":  # loss
            total_points += 1
        elif hands == "B Y":  # draw
            total_points += 2 + 3
        elif hands == "B Z":  # win
            total_points += 3 + 6
        elif hands == "C X":  # win
            total_points += 1 + 6
        elif hands == "C Y":  # loss
            total_points += 2
        elif hands == "C Z":  # draw
            total_points += 3 + 3

    print(total_points)


def part2() -> None:
    total_points = 0
    for line in fileinput.input():
        hands = line.strip()

        if hands == "A X":  # loss, C
            total_points += 3
        elif hands == "A Y":  # draw, A
            total_points += 1 + 3
        elif hands == "A Z":  # win, B
            total_points += 2 + 6
        elif hands == "B X":  # loss, A
            total_points += 1
        elif hands == "B Y":  # draw, B
            total_points += 2 + 3
        elif hands == "B Z":  # win, C
            total_points += 3 + 6
        elif hands == "C X":  # loss, B
            total_points += 2
        elif hands == "C Y":  # draw, C
            total_points += 3 + 3
        elif hands == "C Z":  # win, A
            total_points += 1 + 6

    print(total_points)


if __name__ == "__main__":
    part1()
    part2()
