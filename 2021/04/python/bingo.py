#!/usr/bin/env python3

from __future__ import annotations

import fileinput
from dataclasses import dataclass
from typing import Optional


@dataclass
class BingoBoard:
    numbers: list[list[Optional[int]]]

    @classmethod
    def from_strings(cls, strings: list[str]) -> BingoBoard:
        numbers: list[list[int]] = []
        for line in strings:
            numbers.append([
                int(i)
                for i in line.strip().split(" ")
                if i
            ])

        return BingoBoard(numbers)

    def number_called(self, number: int) -> Optional[int]:
        did_board_change = False

        # Replace number with None in entire board
        for row_index, row in enumerate(self.numbers):
            for column_index, i in enumerate(row):
                if i == number:
                    self.numbers[row_index][column_index] = None
                    did_board_change = True

        if not did_board_change:
            return None

        # Check if any rows or columns are empty
        for index in range(5):
            # Row
            if all(self.numbers[index][i] is None for i in range(5)):
                return self.bingo(number)

            # Column
            if all(self.numbers[i][index] is None for i in range(5)):
                return self.bingo(number)

        return None

    def bingo(self, last_number: int) -> int:
        total_sum = 0
        for row in self.numbers:
            for number in row:
                if number:
                    total_sum += number

        return total_sum * last_number


def part1() -> None:
    lines = list(fileinput.input())
    called_numbers_str = lines.pop(0).strip().split(",")
    called_numbers = map(int, called_numbers_str)

    num_boards = len(lines) // 6
    boards: list[BingoBoard] = []

    for i in range(num_boards):
        offset = i * 6
        boards.append(BingoBoard.from_strings(lines[1 + offset:6 + offset]))

    for number in called_numbers:
        for board in boards:
            if board_sum := board.number_called(number):
                print(f"Part 1: {board_sum}")
                return


def part2() -> None:
    lines = list(fileinput.input())
    called_numbers_str = lines.pop(0).strip().split(",")
    called_numbers = map(int, called_numbers_str)

    num_boards = len(lines) // 6
    boards: list[BingoBoard] = []

    for i in range(num_boards):
        offset = i * 6
        boards.append(BingoBoard.from_strings(lines[1 + offset:6 + offset]))

    for number in called_numbers:
        boards_still_in_play: list[BingoBoard] = []

        for board in boards:
            if board_sum := board.number_called(number):
                if len(boards) == 1:
                    print(f"Part 2: {board_sum}")
                    return
            else:
                boards_still_in_play.append(board)

        boards = boards_still_in_play


if __name__ == "__main__":
    part1()
    part2()
