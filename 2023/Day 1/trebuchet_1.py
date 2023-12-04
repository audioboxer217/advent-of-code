import re

calibration_values = []
with open("input.txt", "r") as input:
    for line in input:
        digits = re.findall(r"\d{1}", line)
        if len(digits) > 1:
            calibration_value = int(f"{digits[0]}{digits[-1]}")
        else:
            calibration_value = int(f"{digits[0]}{digits[0]}")
        calibration_values.append(calibration_value)

print(sum(calibration_values))
