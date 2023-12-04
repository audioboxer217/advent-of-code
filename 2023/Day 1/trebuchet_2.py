import re


def convert_word(string):
    num_words = dict(
        {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
        }
    )

    string_nums = dict()
    for k, v in num_words.items():
        regex = re.compile(r"({})|({})".format(k, v))
        for match in re.finditer(regex, string):
            start = match.start()
            string_nums[start] = v

    locs = list(string_nums.keys())
    locs.sort()
    string_nums = {i: string_nums[i] for i in locs}
    return "".join(string_nums.values())


calibration_values = []
with open("input.txt", "r") as input:
    for line in input:
        line = convert_word(line)
        digits = re.findall(r"\d{1}", line)
        if len(digits) > 1:
            calibration_value = int(f"{digits[0]}{digits[-1]}")
        else:
            calibration_value = int(f"{digits[0]}{digits[0]}")
        calibration_values.append(calibration_value)

print(sum(calibration_values))
