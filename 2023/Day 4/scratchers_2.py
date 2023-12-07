import re

scores = dict({0:0})
with open("input.txt", "r") as input:
    for i, line in enumerate(input):
        if i not in scores:
            scores[i] = 1
        else:
            scores[i] += 1
        winning_nums = [num.group() for num in re.finditer(r"\d+", line[10:39].strip())]
        card_nums = [num.group() for num in re.finditer(r"\d+", line[41:].strip())]
        matches = len(set(winning_nums) & set(card_nums))
        for n in range(matches):
            card = i+1+n
            if card not in scores:
                scores[card] = scores[i]
            else:
                scores[card] += scores[i]

print(f"Total Points: {sum(scores.values())}")