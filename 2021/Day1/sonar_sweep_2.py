with open('input.txt','r') as input:
  depth_readings = input.read().splitlines()

increases = 0
for i in range(len(depth_readings)):
  curr_window = int(depth_readings[i]) + int(depth_readings[i-1]) + int(depth_readings[i-2])
  prev_window = int(depth_readings[i-1]) + int(depth_readings[i-2]) + int(depth_readings[i-3])
  if curr_window > prev_window:
    increases += 1

print(f"{increases = }")