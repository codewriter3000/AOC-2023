import re


def part_1():
    max_red = 12
    max_green = 13
    max_blue = 14

    passed_game_sum = 0

    def process_rounds(rs):
        for r in rs:
            for c in r.strip().split(','):
                pick = re.findall(r'^([0-9]+) ([a-z]+)', c.strip())

                if pick[0][1] == 'red' and int(pick[0][0]) > max_red:
                    return 'failed', parsed_line[0][0]
                elif pick[0][1] == 'green' and int(pick[0][0]) > max_green:
                    return 'failed', parsed_line[0][0]
                elif pick[0][1] == 'blue' and int(pick[0][0]) > max_blue:
                    return 'failed', parsed_line[0][0]

        return 'passed', parsed_line[0][0]

    with open('input.txt', 'r') as file:
        for line in file.read().splitlines():
            parsed_line = re.findall(r'^Game ([0-9]+): (.+)$', line)
            rounds = parsed_line[0][1].split(';')

            if (game := process_rounds(rounds))[0] == 'passed':
                passed_game_sum += int(game[1])

        print(passed_game_sum)


def part_2():
    set_power = 0

    def process_game(rs):
        fewest_red = 0
        fewest_green = 0
        fewest_blue = 0

        for r in rs:
            for c in r.strip().split(','):
                pick = re.findall(r'^([0-9]+) ([a-z]+)', c.strip())[0]

                quantity = int(pick[0])
                color = pick[1]

                if color == 'red' and quantity > fewest_red:
                    fewest_red = quantity
                elif color == 'green' and quantity > fewest_green:
                    fewest_green = quantity
                elif color == 'blue' and quantity > fewest_blue:
                    fewest_blue = quantity

        return fewest_red * fewest_green * fewest_blue

    with open('input.txt', 'r') as file:

        for line in file.read().splitlines():
            parsed_line = re.findall(r'^Game ([0-9]+): (.+)$', line)
            rounds = parsed_line[0][1].split(';')

            set_power += process_game(rounds)
            print(f'set power: {set_power}\n')

        print(set_power)


if __name__ == '__main__':
    part_2()
