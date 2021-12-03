with open('input.txt','r') as input:
  diag_report = input.read().splitlines()

diag_arr = [[line[pos] for line in diag_report] for pos in range(len(diag_report[0]))]

gamma = int(''.join([max(set(pos), key = pos.count) for pos in diag_arr]),2)
epsilon = int(''.join([min(set(pos), key = pos.count) for pos in diag_arr]),2)

print(f"Power Consumtion: {gamma * epsilon}")