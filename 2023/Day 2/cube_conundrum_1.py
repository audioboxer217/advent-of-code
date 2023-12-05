import re

max_numbers = dict(
    {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
)

with open("input.txt", "r") as input:
    possible_games = []
    for line in input:
        possible = True

        game_number = int(line.split(":")[0].replace("Game ", ""))
        print(f"Game: {game_number}")

        pulls = [e.strip() for e in line.split(":")[1].split(";")]
        for pull in pulls:
            counts = pull.split(",")
            for count in counts:
                val, key = count.strip().split(" ")
                if int(val) > max_numbers[key]:
                    possible = False
                    print(f"  Game Impossible: {key}: {val} > {max_numbers[key]}")
                else:
                    print(f"  Game Possible: {key}: {val} <= {max_numbers[key]}")

        if possible:
            possible_games.append(game_number)

    print(sum(possible_games))
