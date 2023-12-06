import re

board = list()
char_locs = list()
num_locs = dict()
with open("input.txt", "r") as input:
    for line_idx, line in enumerate(input):
        board.append([*line.strip()])
        for char in re.finditer(r"[^0-9.\n]", line):
            char_locs.append((line_idx, char.start()))
        for num in re.finditer(f"\d+", line):
            surrounding_square = {
                (r, c)
                for r in (line_idx - 1, line_idx, line_idx + 1)
                for c in range(num.start() - 1, num.end() + 1)
            }
            num_locs[(line_idx, num.start(), num.end())] = surrounding_square

part_nums = []
for num_loc, square in num_locs.items():
    overlap = set(char_locs).intersection(set(square))
    if len(overlap) > 0:
        overlap = overlap.pop()
        part_nums.append(int("".join(board[num_loc[0]][num_loc[1] : num_loc[2]])))

print(sum(part_nums))
