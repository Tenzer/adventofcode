#!/usr/bin/env python3

import fileinput


def get_new_position(head_pos: tuple[int, int], tail_pos: tuple[int, int]) -> tuple[int, int]:
    if abs(head_pos[0] - tail_pos[0]) < 2 and abs(head_pos[1] - tail_pos[1]) < 2:
        return tail_pos

    new_position = list(tail_pos)
    if head_pos[0] > tail_pos[0]:
        new_position[0] += 1
    elif head_pos[0] < tail_pos[0]:
        new_position[0] -= 1

    if head_pos[1] > tail_pos[1]:
        new_position[1] += 1
    elif head_pos[1] < tail_pos[1]:
        new_position[1] -= 1

    return new_position[0], new_position[1]


def part1() -> None:
    head_pos = 0, 0
    tail_pos = 0, 0
    historic_tail_positions: set[tuple[int, int]] = set([tail_pos])

    for line in fileinput.input():
        direction, moves_str = line.strip().split()
        moves = int(moves_str)

        match direction:
            case "L":
                change_per_move = -1, 0
            case "R":
                change_per_move = 1, 0
            case "U":
                change_per_move = 0, -1
            case "D":
                change_per_move = 0, 1

        for _ in range(moves):
            head_pos = head_pos[0] + change_per_move[0], head_pos[1] + change_per_move[1]
            tail_pos = get_new_position(head_pos, tail_pos)
            historic_tail_positions.add(tail_pos)

    print(len(historic_tail_positions))

def part2() -> None:
    rope_positions = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
    historic_tail_positions: set[tuple[int, int]] = set([rope_positions[9]])

    for line in fileinput.input():
        direction, moves_str = line.strip().split()
        moves = int(moves_str)

        match direction:
            case "L":
                change_per_move = -1, 0
            case "R":
                change_per_move = 1, 0
            case "U":
                change_per_move = 0, -1
            case "D":
                change_per_move = 0, 1

        for _ in range(moves):
            rope_positions[0] = rope_positions[0][0] + change_per_move[0], rope_positions[0][1] + change_per_move[1]

            for i in range(1, 10):
                rope_positions[i] = get_new_position(rope_positions[i - 1], rope_positions[i])

                if i == 9:
                    historic_tail_positions.add(rope_positions[i])

    print(len(historic_tail_positions))


if __name__ == "__main__":
    part1()
    part2()
