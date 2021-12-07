import numpy as np

def check_board(board):
  trans_arr = board.T

  for row in board:
    if np.all(row == 'X'):
      return True
  for col in range(trans_arr.shape[0]):
      if np.all(trans_arr[col] == 'X'):
        return True

  return False

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

for called_num in bingo_nums:
  for board in bingo_boards:
    rows,cols =  np.where(board == called_num)
    if len(rows) > 0:
      for row in rows:
        for col in cols:
          board[row][col] = 'X'
    if check_board(board):
      winning_board = board
      final_num = called_num
      break
  else:
    continue
  break

winning_board[winning_board == 'X'] = '0'
print(f"Score: {winning_board.astype(int).sum() * int(final_num)}")