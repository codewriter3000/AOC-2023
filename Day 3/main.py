def part_1():
    symbols = []
    part_numbers = []
    valid_part_numbers = []

    with open('input.txt', 'r') as file:
        for y in range(0, len(file_by_line := file.read().splitlines())):
            for x in range(0, len(line := file_by_line[y])):
                if not ((char := line[x]).isalnum() or char == '.'):
                    # print(char)
                    symbols.append((x, y))

    print(symbols)

    with open('input.txt', 'r') as file:
        number_stack = []

        for y in range(0, len(file_by_line := file.read().splitlines())):
            for x in range(0, len(line := file_by_line[y])):
                if (char := line[x]).isnumeric():
                    number_stack.append((char, x, y))
                elif (length := len(number_stack)) > 0:
                    part_number_list = [n[0] for n in number_stack]

                    part_number = ''

                    for c in part_number_list:
                        part_number += c

                    part_numbers.append((part_number, (x - length, y), (x, y)))

                    number_stack.clear()

    print(part_numbers)

    def validify_part_number(start_position, end_position, y_position):
        for x_position in range(int(start_position[0]), int(end_position[0])):
            for symbol in symbols:
                if (x_position, y_position) in [(symbol[0] - 1, symbol[1] - 1), (symbol[0], symbol[1] - 1),
                                                (symbol[0] - 1, symbol[1]), (symbol[0] - 1, symbol[1] + 1),
                                                (symbol[0] + 1, symbol[1] - 1), (symbol[0], symbol[1] + 1),
                                                (symbol[0] + 1, symbol[1]), (symbol[0] + 1, symbol[1] + 1)]:
                    valid_part_numbers.append(int(part_number_tuple[0]))
                    return

    for part_number_tuple in part_numbers:
        validify_part_number(part_number_tuple[1], part_number_tuple[2], int(part_number_tuple[1][1]))

    print(valid_part_numbers)

    print(sum(valid_part_numbers))


def part_2():
    pass


if __name__ == '__main__':
    part_1()
