#!/usr/bin/env python3

import fileinput
from collections import Counter, defaultdict


def get_sorted_entries():
    return sorted([line.strip() for line in fileinput.input()])


def process_data():
    guards = defaultdict(Counter)
    current_guard = None
    fell_asleep = None

    for entry in get_sorted_entries():
        if entry.endswith("begins shift"):
            current_guard = int(entry.split()[3].lstrip("#"))
        elif entry.endswith("falls asleep"):
            fell_asleep = int(entry.split(":")[1][0:2])
        elif entry.endswith("wakes up"):
            woke_up = int(entry.split(":")[1][0:2])
            for i in range(fell_asleep, woke_up):
                guards[current_guard][i] += 1

    return guards


def part1():
    guards = process_data()

    top_guard = 0
    top_count = 0

    for guard_id, counter in guards.items():
        count = sum(counter.values())
        if count > top_count:
            top_guard = guard_id
            top_count = count

    top_minute = guards[top_guard].most_common(1)[0]
    print("Part 1:", top_guard * top_minute[0])


def part2():
    guards = process_data()

    top_guard_id = 0
    top_minute = 0
    top_count = 0

    for guard_id, counter in guards.items():
        minute, count = counter.most_common(1)[0]
        if count > top_count:
            top_guard_id = guard_id
            top_minute = minute
            top_count = count

    print("Part 2:", top_guard_id * top_minute)


if __name__ == "__main__":
    part1()
    part2()
