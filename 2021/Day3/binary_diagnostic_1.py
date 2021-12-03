with open('input.txt','r') as input:
  diag_report = input.read().splitlines()

diag_arr = [[line[pos] for line in diag_report] for pos in range(len(diag_report[0]))]

bin_gamma = ''
bin_epsilon = ''
for pos in diag_arr:
  bin_gamma += max(set(pos), key = pos.count)
  bin_epsilon += min(set(pos), key = pos.count)

gamma = int(bin_gamma,2)
epsilon = int(bin_epsilon,2)

print(f"Power Consumtion: {gamma * epsilon}")