with open('input.txt','r') as input:
  diag_report = input.read().splitlines()


def bit_criteria(pos_arr, reading_type):
  if pos_arr.count('0') != pos_arr.count('1'):
    bit_criteria_dict = {
      'co2': min(set(pos_arr), key = pos_arr.count),
      'o2': max(set(pos_arr), key = pos_arr.count)
    }
  else:
    bit_criteria_dict = {
      'co2': '0',
      'o2': '1'
    }
  return bit_criteria_dict[reading_type]

def get_reading(reading_type, readings_report = [], curr_pos = 0):
  if curr_pos > 0:
    reading_arr = [[line[pos] for line in readings_report] for pos in range(len(readings_report[0]))]
    readings_report = [reading for reading in readings_report if reading[curr_pos] == bit_criteria(reading_arr[curr_pos],reading_type)]
  else:
    reading_arr = [[line[pos] for line in diag_report] for pos in range(len(diag_report[0]))]
    readings_report = [reading for reading in diag_report if reading[0] == bit_criteria(reading_arr[0],reading_type)]

  if len(readings_report) == 1:
    return readings_report[0]
  else:
    curr_pos += 1
    return get_reading(reading_type,readings_report,curr_pos)


o2_reading = int(get_reading('o2'),2)
co2_reading = int(get_reading('co2'),2)

print(f"Oxygen Generator Rating: {o2_reading * co2_reading}")