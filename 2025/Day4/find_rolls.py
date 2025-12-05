#!/usr/bin/env uv run


def isValidPos(x, y, x_max, y_max):
    if x < 0 or y < 0 or x >= x_max or y >= y_max:
        return 0
    return 1

def getAdjacentRolls(arr, x, y, x_max, y_max):
    ans = []

    if isValidPos(x - 1, y - 1, x_max, y_max):
        if arr[x - 1][y - 1] == "@":
            ans.append(arr[x - 1][y - 1])
    if isValidPos(x - 1, y, x_max, y_max):
        if arr[x - 1][y] == "@":
            ans.append(arr[x - 1][y])
    if isValidPos(x - 1, y + 1, x_max, y_max):
        if arr[x - 1][y + 1] == "@":
            ans.append(arr[x - 1][y + 1])
    if isValidPos(x, y - 1, x_max, y_max):
        if arr[x][y - 1] == "@":
            ans.append(arr[x][y - 1])
    if isValidPos(x, y + 1, x_max, y_max):
        if arr[x][y + 1] == "@":
            ans.append(arr[x][y + 1])
    if isValidPos(x + 1, y - 1, x_max, y_max):
        if arr[x + 1][y - 1] == "@":
            ans.append(arr[x + 1][y - 1])
    if isValidPos(x + 1, y, x_max, y_max):
        if arr[x + 1][y] == "@":
            ans.append(arr[x + 1][y])
    if isValidPos(x + 1, y + 1, x_max, y_max):
        if arr[x + 1][y + 1] == "@":
            ans.append(arr[x + 1][y + 1])

    return ans


def remove_rolls(input, debug=False):
    rolls_to_remove = 0
    new_input = []

    x_max = len(input)
    y_max = len(input[0])
    
    for x in range(0, x_max):
        print_line = []
        for y in range(0, y_max):
            if input[x][y] == "@":
                adj_rolls = getAdjacentRolls(input, x, y, x_max, y_max)
                if len(adj_rolls) < 4:
                    print_line.append("X")
                    rolls_to_remove += 1
                else:        
                    print_line.append(input[x][y])
            else:
                print_line.append(input[x][y])
        if debug:
            print("".join(print_line))
        new_line = [x.replace("X", ".") for x in print_line]
        new_input.append(new_line)


    return rolls_to_remove, new_input


def main(input, debug=False):
    answer1, input = remove_rolls(input, debug)
    answer2 = answer1

    rolls_left = True
    while rolls_left:
        rolls_to_remove, input = remove_rolls(input, debug)
        if rolls_to_remove == 0:
            rolls_left = False
        else:
            answer2 += rolls_to_remove


    return answer1, answer2


if __name__ == '__main__':
    try:
        # with open('puzzle_input_sample.txt', 'r') as f:
        with open('puzzle_input.txt', 'r') as f:
            full_file = f.readlines()
        input = [list(x.strip()) for x in full_file]

    except FileNotFoundError:
        print("Error: The file 'puzzle_input.txt' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    answer1, answer2 = main(input)
    print(f"Solution1: {answer1}\nSolution2: {answer2}")