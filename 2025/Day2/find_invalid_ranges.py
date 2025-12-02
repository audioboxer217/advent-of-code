#!/usr/bin/env uv run

def main(input):
    answer1 = []
    answer2 = []
    for id_range in input:
        # print(id_range)
        for id in range(int(id_range.split('-')[0]), int(id_range.split('-')[1]) + 1):
            s_id = str(id)
            full_length = len(s_id)
            midpoint = full_length // 2
            first_half = s_id[:midpoint]
            second_half = s_id[midpoint:]
            if first_half == second_half:
                print(f"  Invalid ID: {id}")
                answer1.append(id)
            for portion in range(1, midpoint + 1):
                if full_length % portion == 0:
                    pattern = s_id[:portion]
                    if pattern * (full_length // portion) == s_id:
                        print(f"  Invalid ID: {id} (pattern: {pattern})")
                        answer2.append(id)
                        break

    return sum(answer1), sum(answer2)


if __name__ == '__main__':
    try:
        # with open('puzzle_input_sample.txt', 'r') as f:
        with open('puzzle_input.txt', 'r') as f:
            input = f.read().split(',')
    except FileNotFoundError:
        print("Error: The file 'puzzle_input.txt' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    answer1, answer2 = main(input)
    print(f"Solution1: {answer1}\nSolution2: {answer2}")