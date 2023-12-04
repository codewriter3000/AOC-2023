import re

INPUT_FILE = 'input.txt'
REGEX_STR = r'^([0-9]+)-([0-9]+),([0-9]+)-([0-9]+)$'


def read_input(path):
    with open(path) as file_handler:
        return [line for line in file_handler.read().splitlines()]


def part_1():
    enclosed_assignment_pairs = 0

    for line in read_input(INPUT_FILE):
        match = re.match(REGEX_STR, line)
        left_start = int(match[1])
        left_end = int(match[2])
        right_start = int(match[3])
        right_end = int(match[4])

        if ((left_start >= right_start and left_end <= right_end) or
                (left_start <= right_start and left_end >= right_end)):
            enclosed_assignment_pairs += 1

    return enclosed_assignment_pairs


def part_2():
    overlapping_assignment_pairs = 0

    for line in read_input(INPUT_FILE):
        match = re.match(REGEX_STR, line)
        left_start = int(match[1])
        left_end = int(match[2])
        right_start = int(match[3])
        right_end = int(match[4])

        if ((left_start <= right_start <= left_end) or
                (right_start <= left_start <= right_end)):
            overlapping_assignment_pairs += 1

    return overlapping_assignment_pairs


if __name__ == '__main__':
    print(part_1())
    print(part_2())
