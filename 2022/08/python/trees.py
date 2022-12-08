#!/usr/bin/env python3

import fileinput
from itertools import product


def read_grid() -> list[list[int]]:
    grid: list[list[int]] = []
    for line in fileinput.input():
        grid.append([])
        for char in line.strip():
            grid[-1].append(int(char))

    return grid


def part1(grid: list[list[int]]) -> None:
    visible_trees: set[tuple[int, int]] = set()

    row_length = len(grid)
    column_length = len(grid[0])
    for row_index, column in enumerate(grid):
        # Left to right
        highest_value_seen = -1
        for column_index, value in enumerate(column):
            if value > highest_value_seen:
                visible_trees.add((row_index, column_index))
                highest_value_seen = value

        # Right to left
        highest_value_seen = -1
        for column_index, value in enumerate(reversed(column)):
            if value > highest_value_seen:
                visible_trees.add((row_index, column_length - 1 - column_index))
                highest_value_seen = value

    for column_index in range(column_length):
        # Top to bottom
        highest_value_seen = -1
        for row_index in range(row_length):
            value = grid[row_index][column_index]
            if value > highest_value_seen:
                visible_trees.add((row_index, column_index))
                highest_value_seen = value

        # Bottom to top
        highest_value_seen = -1
        for row_index in reversed(range(row_length)):
            value = grid[row_index][column_index]
            if value > highest_value_seen:
                visible_trees.add((row_index, column_index))
                highest_value_seen = value

    print(len(visible_trees))


def part2(grid: list[list[int]]) -> None:
    rows = (i for i in range(len(grid)))
    columns = (i for i in range(len(grid[0])))
    max_row = len(grid[0])

    scenic_scores: dict[tuple[int, int], int] = {}
    for row_index, column_index in product(rows, columns):
        tree_height = grid[row_index][column_index]

        # Looking left
        left_score = 0
        for i in reversed(grid[row_index][:column_index]):
            left_score += 1
            if i >= tree_height:
                break
        if left_score == 0:
            continue

        # Looking right
        right_score = 0
        for i in grid[row_index][column_index + 1:]:
            right_score += 1
            if i >= tree_height:
                break
        if right_score == 0:
            continue

        # Looking up
        up_score = 0
        for row in reversed(range(row_index)):
            up_score += 1
            if grid[row][column_index] >= tree_height:
                break
        if up_score == 0:
            continue

        # Looking down
        down_score = 0
        for row in range(row_index + 1, max_row):
            down_score += 1
            if grid[row][column_index] >= tree_height:
                break
        if down_score == 0:
            continue

        scenic_scores[(row_index, column_index)] = left_score * right_score * up_score * down_score

    print(max(scenic_scores.values()))


if __name__ == "__main__":
    parsed_grid = read_grid()
    part1(parsed_grid)
    part2(parsed_grid)
