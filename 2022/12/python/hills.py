#!/usr/bin/env python3

import fileinput
import string

import networkx


def parse_input() -> tuple[list[list[int]], tuple[int, int], tuple[int, int]]:
    start: tuple[int, int]
    end: tuple[int, int]
    grid: list[list[int]] = []

    for row_index, line in enumerate(fileinput.input()):
        grid.append([])
        for column_index, character in enumerate(line.strip()):
            if character == "S":
                start = row_index, column_index
                character = "a"
            elif character == "E":
                end = row_index, column_index
                character = "z"

            grid[row_index].append(string.ascii_lowercase.index(character))

    return grid, start, end


def part1(grid: list[list[int]], start: tuple, end: tuple) -> None:
    graph = networkx.DiGraph()
    max_index = len(grid) - 1, len(grid[0]) - 1

    for row_index,row in enumerate(grid):
        for column_index, value in enumerate(row):
            if row_index > 0:
                adjecent_value = grid[row_index - 1][column_index]
                if adjecent_value <= value + 1:
                    graph.add_edge((row_index, column_index), (row_index - 1, column_index))

            if column_index > 0:
                adjecent_value = row[column_index - 1]
                if adjecent_value <= value + 1:
                    graph.add_edge((row_index, column_index), (row_index, column_index - 1))

            if row_index < max_index[0]:
                adjecent_value = grid[row_index + 1][column_index]
                if adjecent_value <= value + 1:
                    graph.add_edge((row_index, column_index), (row_index + 1, column_index))

            if column_index < max_index[1]:
                adjecent_value = row[column_index + 1]
                if adjecent_value <= value + 1:
                    graph.add_edge((row_index, column_index), (row_index, column_index + 1))

    print(len(networkx.shortest_path(graph, start, end)) - 1)


def part2(grid: list[list[int]], _: tuple, end: tuple) -> None:
    graph = networkx.DiGraph()
    max_index = len(grid) - 1, len(grid[0]) - 1
    lowest_points: set[tuple[int, int]] = set()

    for row_index,row in enumerate(grid):
        for column_index, value in enumerate(row):
            if value == 0:
                lowest_points.add((row_index, column_index))

            if row_index > 0:
                adjecent_value = grid[row_index - 1][column_index]
                if adjecent_value <= value + 1:
                    graph.add_edge((row_index, column_index), (row_index - 1, column_index))

            if column_index > 0:
                adjecent_value = row[column_index - 1]
                if adjecent_value <= value + 1:
                    graph.add_edge((row_index, column_index), (row_index, column_index - 1))

            if row_index < max_index[0]:
                adjecent_value = grid[row_index + 1][column_index]
                if adjecent_value <= value + 1:
                    graph.add_edge((row_index, column_index), (row_index + 1, column_index))

            if column_index < max_index[1]:
                adjecent_value = row[column_index + 1]
                if adjecent_value <= value + 1:
                    graph.add_edge((row_index, column_index), (row_index, column_index + 1))

    shortest_found = 1_024
    for source, path in networkx.shortest_path(graph, target=end).items():
        if source not in lowest_points:
            continue

        path_length = len(path)
        if path_length < shortest_found:
            shortest_found = path_length

    print(shortest_found - 1)


if __name__ == "__main__":
    part1(*parse_input())
    part2(*parse_input())
