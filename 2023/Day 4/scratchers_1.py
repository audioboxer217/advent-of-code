import re

scores = []
with open("input.txt", "r") as input:
    for line in input:
        winning_nums = [num.group() for num in re.finditer(r"\d+", line[10:39].strip())]
        card_nums = [num.group() for num in re.finditer(r"\d+", line[41:].strip())]
        matches = len(set(winning_nums) & set(card_nums))
        if matches > 0:
            score = 2**(matches-1)
            scores.append(score)

print(f"Total Points: {sum(scores)}")