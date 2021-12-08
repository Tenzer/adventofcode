#!/usr/bin/env python3

import fileinput


def part1() -> None:
    unique_numbers_found = 0

    for line in fileinput.input():
        _, output_value = line.strip().split(" | ", 2)

        for number in output_value.split(" "):
            if len(number) in {2, 3, 4, 7}:
                unique_numbers_found += 1

    print(f"Part 1: {unique_numbers_found}")


def decipher(input_values: list[str], output_values: list[str]) -> int:
    input_values = ["".join(sorted(i)) for i in input_values]
    output_values = ["".join(sorted(i)) for i in output_values]
    all_values = set(input_values + output_values)
    segment_mapping: dict[str, str] = {}
    number_mapping: dict[int, str] = {
        8: "abcdefg",
    }

    # 8s
    all_values.discard(number_mapping[8])

    # 1s
    for i in all_values:
        if len(i) == 2:
            number_mapping[1] = i
            all_values.discard(number_mapping[1])
            break

    # 7s
    for i in all_values:
        if len(i) == 3:
            number_mapping[7] = i
            all_values.discard(number_mapping[7])
            segment_mapping["a"] = (set(number_mapping[7]) - set(number_mapping[1])).pop()
            break

    # 4s
    for i in all_values:
        if len(i) == 4:
            number_mapping[4] = i
            all_values.discard(number_mapping[4])
            possible_b_d = set(number_mapping[4]) - set(number_mapping[1])
            break

    # 0s
    for i in all_values:
        if len(i) == 6:
            # Returns True if the b/d segment isn't found in i
            i_set = set(i)
            if possible_b_d - i_set:
                number_mapping[0] = i
                all_values.discard(number_mapping[0])
                segment_mapping["d"] = (possible_b_d - i_set).pop()
                possible_b_d.discard(segment_mapping["d"])
                segment_mapping["b"] = possible_b_d.pop()
                break

    # 6s
    set_1 = set(number_mapping[1])
    for i in all_values:
        if len(i) == 6:
            i_set = set(i)
            # Returns True if segment c or f is found in i
            if set_1 - i_set:
                number_mapping[6] = i
                all_values.discard(number_mapping[6])
                c_segment = set_1 - i_set
                segment_mapping["c"] = c_segment.pop()
                segment_mapping["f"] = (set_1 - c_segment).pop()
                break

    # 9s
    for i in all_values:
        if len(i) == 6:
            number_mapping[9] = i
            all_values.discard(number_mapping[9])
            segment_mapping["e"] = (set(number_mapping[8]) - set(number_mapping[9])).pop()
            break

    # Only 5 segment digits left from here

    # 2s
    for i in all_values:
        if segment_mapping["e"] in set(i):
            number_mapping[2] = i
            all_values.discard(number_mapping[2])
            break

    # 5s
    for i in all_values:
        if segment_mapping["b"] in set(i):
            number_mapping[5] = i
            all_values.discard(number_mapping[5])
            break

    # 3s
    for i in all_values:
        number_mapping[3] = i
        all_values.discard(number_mapping[3])
        break

    assert len(all_values) == 0

    number_mapping_flipped = {value: str(key) for key, value in number_mapping.items()}
    output = ""
    for output_value in output_values:
        output += number_mapping_flipped[output_value]

    return int(output)


def part2() -> None:
    total_output = 0

    for line in fileinput.input():
        input_value, output_value = line.strip().split(" | ", 2)
        input_values = input_value.split(" ")
        output_values = output_value.split(" ")
        total_output += decipher(input_values, output_values)

    print(f"Part 2: {total_output}")


if __name__ == "__main__":
    part1()
    part2()
