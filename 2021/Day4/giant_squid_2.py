import numpy as np

def mark_board(called_num, board):
  rows,cols =  np.where(board == called_num)
  # print(f"{called_num} found in {rows},{cols}")
  if len(rows) > 0:
    for row in rows:
      for col in cols:
        board[row][col] = 'X'

  return board

def check_board(board):
  trans_arr = board.T

  for row in board:
    if np.all(row == 'X'):
      return True
  for col in range(trans_arr.shape[0]):
      if np.all(trans_arr[col] == 'X'):
        return True

  return False

def remove_from_array(array, item):
  for i in range(len(array)):
    if np.array_equal(array[i],item):
      array.pop(i)
      break

with open('input.txt','r') as input_file:
  input_lines = input_file.read().splitlines()
  bingo_nums = input_lines[0].split(',')
  bingo_board_input = input_lines[1:]
  bingo_boards = []
  for line in bingo_board_input:
    if line == '':
      try:
        bingo_boards.append(np.array(board))
      except NameError:
        pass
      board = []
    else:
      board_line = line.split()
      board.append(board_line)
  bingo_boards.append(np.array(board))

winning_boards = []
for called_num in bingo_nums:
  for board in winning_boards:
    remove_from_array(bingo_boards, board)
  for board in bingo_boards:
    board = mark_board(called_num, board)
    if check_board(board):
      winning_boards.append(board)
      if len(bingo_boards) == 1:
        last_winning_board = board
        final_num = called_num
        break
  else:
    continue
  break

last_winning_board[last_winning_board == 'X'] = '0'
print(f"Score: {last_winning_board.astype(int).sum() * int(final_num)}")