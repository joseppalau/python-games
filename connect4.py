import numpy as np

ROW_COUNT = 6
COL_COUNT = 7

def create_board():
	board = np.zeros((ROW_COUNT,COL_COUNT))
	return board

def drop_piece(board, row, sel, piece):
	board[row][sel] == piece

def is_valid_location(board, sel):
	return board[ROW_COUNT-1][sel] == 0

def get_next_open_row(board, sel):
	for row in range(ROW_COUNT):
		if board[row][sel] == 0:
			return row		

board = create_board()
print(board) 	

game_over = False
turn = 0

while not game_over:
	if turn == 0:
		sel = int(input('Player 1, make your selection (0-6):'))
		if is_valid_location(board, sel):
			row = get_next_open_row(board, sel)
			drop_piece(board, row, sel, 1)
	else:
		sel = int(input('Player 2, make your selection (0-6:'))
		if is_valid_location(board, sel):
			row = get_next_open_row(board, sel)
			drop_piece(board, row, sel, 2)

	turn += 1
	turn = turn % 2	