with open('input.txt','r') as input:
  depth_readings = input.read().splitlines()

increases = 0
for i in range(len(depth_readings)):
  print(i)
  if depth_readings[i] > depth_readings[i-1]:
    print(f"increase")
    increases += 1

print(f"{increases = }")