#!/usr/bin/env uv run

def determine_joltage(bank, battery_num):
    batteries = str(bank).strip()
    if battery_num > 2:
        batteries_left = battery_num - 1
    else:
        batteries_left = battery_num
    batteries_left = battery_num
    joltage = ''
    count = 1
    while count <= battery_num:
        # available_batteries = batteries[:-batteries_left+1]
        # battery_val = max(available_batteries)
        if count != battery_num:
            limit = battery_num - count
            battery_val = max(batteries[:-limit])
        else:
            battery_val = max(batteries)
        idx = batteries.index(battery_val)
        batteries = batteries[idx+1:]
        joltage += battery_val
        batteries_left -= 1
        count += 1

    return joltage


def main(input):
    answer1 = []
    answer2 = []

    for bank in input:
        joltage1 = determine_joltage(bank, 2)
        # print(joltage1)
        answer1.append(int(joltage1))

        joltage2 = determine_joltage(bank, 12)
        # print(joltage2)
        answer2.append(int(joltage2))


    return sum(answer1), sum(answer2)


if __name__ == '__main__':
    try:
        # with open('puzzle_input_sample.txt', 'r') as f:
        with open('puzzle_input.txt', 'r') as f:
            input = f.readlines()
    except FileNotFoundError:
        print("Error: The file 'puzzle_input.txt' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    answer1, answer2 = main(input)
    print(f"Solution1: {answer1}\nSolution2: {answer2}")