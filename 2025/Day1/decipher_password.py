#!/usr/bin/env uv run

def main(input):
    actual_zero = 0
    passes_zero = 0
    position = 50
    for rotation in input:
        direction = rotation[0]
        amount = int(rotation[1:])
        movement = amount % 100
        passes_zero += amount // 100

        if direction == 'R':
            position += movement
            if position >= 100:
                position -= 100
                if position != 0:
                    passes_zero += 1
        elif direction == 'L':
            if position == 0:
                position = 100
            position -= movement
            if position < 0:
                position += 100
                passes_zero += 1
        
        if position == 0:
            actual_zero += 1

    return actual_zero, actual_zero + passes_zero



if __name__ == '__main__':
    try:
        with open('puzzle_input.txt', 'r') as f:
            input = f.readlines()
    except FileNotFoundError:
        print("Error: The file 'puzzle_input.txt' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    answer1, answer2 = main(input)
    print(f"Solution1: {answer1}\nSolution2: {answer2}")