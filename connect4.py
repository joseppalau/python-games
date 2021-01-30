import numpy as np
import pygame
import sys

ROW_COUNT = 6
COL_COUNT = 7
BLUE = (0,102,204)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)


def create_board():
	board = np.zeros((ROW_COUNT,COL_COUNT))
	return board

def drop_piece(board, row, sel, piece):
	board[row][sel] = piece

def is_valid_location(board, sel):
	return board[0][sel] == 0

def get_next_open_row(board, sel):
	if board[ROW_COUNT-1][sel] == 0:
		return ROW_COUNT-1
	else:	
		for row in range(ROW_COUNT-1):
			if board[row+1][sel] != 0:
				return row	

def winning_move(board, piece):
	#vertical movements
	for c in range(COL_COUNT-3):
		for r in range(ROW_COUNT):
			if all(map(lambda x: board[r][x] == piece, range(c,c+4))):
				return True		

	#horizontal movements			
	for r in range(ROW_COUNT-3):
		for c in range(COL_COUNT):
			if all(map(lambda x: board[x][c] == piece, range(r,r+4))):
				return True		

	#positive diagonals			
	for c in range(COL_COUNT-3):
		for r in range(ROW_COUNT-3):
			 if all(map(lambda x: board[x[0]][x[1]] == piece, [(r,c),(r+1,c+1),(r+2,c+2),(r+3,c+3)])):
			 	return True 

	#negative diagonals
	for c in range(COL_COUNT-3):
		for r in range(3, ROW_COUNT):
			 if all(map(lambda x: board[x[0]][x[1]] == piece, [(r,c), (r-1,c-1),(r-2,c-2),(r-3,c-3)])):
			 	return True

				

def print_board(board):
	print(board)	

def draw_board(board):
	d = SQUARESIZE//2 #the circle center matchs the square center 
	for c in range(COL_COUNT):
		for r in range(1,ROW_COUNT+1):
			pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE, SQUARESIZE, SQUARESIZE))
			if board[r-1][c] == 1:
				pygame.draw.circle(screen, RED, (c*SQUARESIZE+d, r*SQUARESIZE+d), RADIUS)
			elif board[r-1][c] == 2:
				pygame.draw.circle(screen, YELLOW, (c*SQUARESIZE+d, r*SQUARESIZE+d), RADIUS)				
			else:
				pygame.draw.circle(screen, BLACK, (c*SQUARESIZE+d, r*SQUARESIZE+d), RADIUS)				

board = create_board()
print_board(board)	

game_over = False
turn = 0

pygame.init()

SQUARESIZE = 100
WIDTH = COL_COUNT * SQUARESIZE
HEIGHT = (ROW_COUNT+1) * SQUARESIZE
SIZE = (WIDTH, HEIGHT)
RADIUS = SQUARESIZE//2 - 5

screen = pygame.display.set_mode(SIZE)
#np.flip(board, 0)
draw_board(board)
pygame.display.update()

while not game_over:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN:
			if turn == 0:
				posX = event.pos[0]
				sel = posX//SQUARESIZE #'Player 1, make your selection (0-6):'))
				if is_valid_location(board, sel):
					row = get_next_open_row(board, sel)
					drop_piece(board, row, sel, 1)
					draw_board(board)	
					print_board(board)
					if winning_move(board, 1):
						print('Player 1 WINS!!!')
						game_over = True
			else:
				posX = event.pos[0] #'Player 2, make your selection (0-6):'))
				sel = posX//SQUARESIZE
				if is_valid_location(board, sel):
					row = get_next_open_row(board, sel)
					drop_piece(board, row, sel, 2)
					draw_board(board)
					print_board(board)
					if winning_move(board, 2):
						print('Player 2 WINS!!!')
						game_over = True

			turn += 1
			turn = turn % 2				

			draw_board(board)
			pygame.display.update()					
	