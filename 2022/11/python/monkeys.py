#!/usr/bin/env python3

import copy
import fileinput
import math
from dataclasses import dataclass
from itertools import islice
from typing import Literal


@dataclass
class Monkey:
    items: list[int]
    operation: tuple[str, int | Literal["old"]]
    test_divisible_by: int
    true_target: int
    false_target: int
    inspections: int = 0


def batched(iterable, n):
    """Batch data into lists of length n. The last batch may be shorter.

    Taken from https://docs.python.org/3/library/itertools.html."""
    if n < 1:
        raise ValueError("n must be at least one")
    it = iter(iterable)
    while batch := list(islice(it, n)):
        yield batch


def parse_input() -> list[Monkey]:
    monkeys: list[Monkey] = []

    for lines in batched(fileinput.input(), 7):
        items_str = lines[1].split("  Starting items: ")[1]
        items = [int(i) for i in items_str.split(",")]

        operation_list = lines[2].split("  Operation: new = old ")[1].split()
        if operation_list[1] != "old":
            operation_list[1] = int(operation_list[1])
        operation = operation_list[0], operation_list[1]

        test_divisible_by = int(lines[3].split("  Test: divisible by ")[1])
        true_target = int(lines[4].split("    If true: throw to monkey ")[1])
        false_target = int(lines[5].split("    If false: throw to monkey ")[1])

        monkeys.append(Monkey(
            items=items,
            operation=operation,
            test_divisible_by=test_divisible_by,
            true_target=true_target,
            false_target=false_target,
        ))

    return monkeys


def part1(monkeys: list[Monkey]) -> None:
    for _ in range(20):
        for monkey in monkeys:
            for old_value in monkey.items:
                if monkey.operation[1] == "old":
                    if monkey.operation[0] == "*":
                        new_value = old_value * old_value
                    else:
                        new_value = old_value + old_value
                else:
                    if monkey.operation[0] == "*":
                        new_value = old_value * monkey.operation[1]
                    else:
                        new_value = old_value + monkey.operation[1]

                new_value = math.floor(new_value / 3)

                if new_value % monkey.test_divisible_by == 0:
                    monkeys[monkey.true_target].items.append(new_value)
                else:
                    monkeys[monkey.false_target].items.append(new_value)

                monkey.inspections += 1

            monkey.items.clear()

    inspections = [monkey.inspections for monkey in monkeys]
    inspections.sort()
    print(inspections[-2] * inspections[-1])


def part2(monkeys: list[Monkey]) -> None:
    least_common_multiple = math.lcm(*[monkey.test_divisible_by for monkey in monkeys])

    for _ in range(10_000):
        for monkey in monkeys:
            for value in monkey.items:
                if monkey.operation[1] == "old":
                    if monkey.operation[0] == "*":
                        value *= value
                    else:
                        value += value
                else:
                    if monkey.operation[0] == "*":
                        value *= monkey.operation[1]
                    else:
                        value += monkey.operation[1]

                # Bring the values down to keep the runtime reasonable
                value %= least_common_multiple

                if value % monkey.test_divisible_by == 0:
                    monkeys[monkey.true_target].items.append(value)
                else:
                    monkeys[monkey.false_target].items.append(value)

                monkey.inspections += 1

            monkey.items.clear()

    inspections = [monkey.inspections for monkey in monkeys]
    inspections.sort()
    print(inspections[-2] * inspections[-1])


if __name__ == "__main__":
    parsed_input = parse_input()
    part1(copy.deepcopy(parsed_input))
    part2(copy.deepcopy(parsed_input))
