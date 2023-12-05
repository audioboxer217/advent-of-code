import re
import math

with open("input.txt", "r") as input:
    game_powers = []
    for line in input:
        game_number = int(line.split(":")[0].replace("Game ", ""))
        print(f"Game: {game_number}")

        color_min = dict()
        pulls = [e.strip() for e in line.split(":")[1].split(";")]
        for pull in pulls:
            counts = pull.split(",")
            for count in counts:
                val, key = count.strip().split(" ")
                if key not in color_min or color_min[key] < int(val):
                    color_min[key] = int(val)
        set_power = math.prod(color_min.values())
        print(f"  Set Power: {set_power}")
        game_powers.append(set_power)

    print(sum(game_powers))
