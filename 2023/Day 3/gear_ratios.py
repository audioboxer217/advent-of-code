import re
import math

board = list(open("input.txt"))
gears = {(r, c): [] for r in range(140) for c in range(140) if board[r][c] == "*"}

for line_idx, line in enumerate(board):
    for num in re.finditer(r"\d+", line):
        square = {
            (r, c)
            for r in (line_idx - 1, line_idx, line_idx + 1)
            for c in range(num.start() - 1, num.end() + 1)
        }

        for overlap in square & gears.keys():
            gears[overlap].append(int(num.group()))

gear_ratios = [
    math.prod(part_nums) for part_nums in gears.values() if len(part_nums) == 2
]
print(sum(gear_ratios))
