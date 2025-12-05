#!/usr/bin/env uv run
import os

def compress_ranges(fresh_ranges):
    fresh_ranges.sort(key=lambda r: int(r.split('-')[0]))

    i = 0
    while i < len(fresh_ranges) - 1:
        curr_start, curr_end = map(int, fresh_ranges[i].split('-'))
        next_start, next_end = map(int, fresh_ranges[i+1].split('-'))

        if curr_end >= next_start:
            fresh_ranges[i] = f"{curr_start}-{max(curr_end, next_end)}"
            fresh_ranges.pop(i+1)
        else:
            i += 1


    return fresh_ranges


def is_fresh(ingredient_id, fresh_ranges):
    for fresh_range in fresh_ranges:
        start, end = map(int, fresh_range.split('-'))
        if start <= ingredient_id <= end:
            return True
    return False


def count_fresh_ids(fresh_ranges):
    count = 0

    for fresh_range in fresh_ranges:
        start, end = map(int, fresh_range.split('-'))
        count += end - start + 1

    return count


def main(input, debug=False):
    answer1 = 0

    fresh_ranges = compress_ranges(input[0].split('\n'))
    available_ingredients = [int(i) for i in input[1].split('\n')]

    if debug:
        print(f"Fresh Ingredient Ranges: {fresh_ranges}")
        print(f"Available Ingredients: {available_ingredients}")

    for ingredient in available_ingredients:
        if is_fresh(ingredient, fresh_ranges):
            if debug:
                print(f"Ingredient {ingredient}: Fresh!")
            answer1 += 1
        else:
            if debug:
                print(f"Ingredient {ingredient}: Not fresh!")

    answer2 = count_fresh_ids(fresh_ranges)

    return answer1, answer2


if __name__ == '__main__':
    debug = bool(os.getenv('DEBUG', False))
    input_file = 'puzzle_input_sample.txt' if debug else 'puzzle_input.txt'

    try:
        with open(input_file, 'r') as f:
            input = f.read().split('\n\n')
    except FileNotFoundError:
        print("Error: The file 'puzzle_input.txt' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    answer1, answer2 = main(input, debug)
    print(f"Solution1: {answer1}\nSolution2: {answer2}")