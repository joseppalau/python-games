import numpy as np
import pygame
import sys

ROW_COUNT = 6
COL_COUNT = 7
BLUE = (0,102,204)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

SQUARESIZE = 100
WIDTH = COL_COUNT * SQUARESIZE
HEIGHT = (ROW_COUNT+1) * SQUARESIZE
SIZE = (WIDTH, HEIGHT)
RADIUS = SQUARESIZE//2 - 5
D = SQUARESIZE//2 # the circle center will match the square center  
cells_filled = {}
tablero = pygame.Surface((SQUARESIZE * COL_COUNT, SQUARESIZE * ROW_COUNT))
tablero.fill(BLUE)
tablero.set_colorkey(BLACK)

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

def cell_to_fill(row,sel):
	return cells_filled.get((row,sel),False) 


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

def draw_board(board): #the circle center matchs the square center 
	for c in range(COL_COUNT):
		for r in range(ROW_COUNT):
			if board[r][c] == 1 and cells_filled.get((r,c),False):
				pygame.draw.circle(tablero, RED, (c*SQUARESIZE+D, r*SQUARESIZE+D), RADIUS)
			elif board[r][c] == 2 and cells_filled.get((r,c),False):
				pygame.draw.circle(tablero, YELLOW, (c*SQUARESIZE+D, r*SQUARESIZE+D), RADIUS)				
			else:
				pygame.draw.circle(tablero, BLACK, (c*SQUARESIZE+D, r*SQUARESIZE+D), RADIUS)
	screen.blit(tablero, (0, SQUARESIZE))					


'''def draw_board(board):
	d = SQUARESIZE//2 #the circle center matchs the square center 
	for c in range(COL_COUNT):
		for r in range(1,ROW_COUNT+1):
			pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE, SQUARESIZE, SQUARESIZE))
			if board[r-1][c] == 1 and cells_filled.get((r-1,c),False):
				pygame.draw.circle(screen, RED, (c*SQUARESIZE+d, r*SQUARESIZE+d), RADIUS)
			elif board[r-1][c] == 2 and cells_filled.get((r-1,c),False):
				pygame.draw.circle(screen, YELLOW, (c*SQUARESIZE+d, r*SQUARESIZE+d), RADIUS)				
			else:
				pygame.draw.circle(screen, BLACK, (c*SQUARESIZE+d, r*SQUARESIZE+d), RADIUS)'''		

def dropping_piece(sel,piece,yPos):
	if piece == 1:
		pygame.draw.circle(screen,RED,(sel*SQUARESIZE+D, yPos),RADIUS)
	else:
		pygame.draw.circle(screen,YELLOW,(sel*SQUARESIZE+D, yPos),RADIUS)


pygame.font.init()

def message_winner(surface, piece, color):
	message_font = pygame.font.SysFont('comicsans', 75)
	message_text = message_font.render('Player {0} wins!!'.format(piece), 1, color)
	surface.blit(message_text,(10,10) )						

board = create_board()
print_board(board)	

game_over = False
turn = 0

screen = pygame.display.set_mode(SIZE)
#np.flip(board, 0)
draw_board(board)
pygame.display.update()

while not game_over:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEMOTION:
			posX = event.pos[0]
			pygame.draw.rect(screen, BLACK,(0,0,WIDTH,SQUARESIZE))
			if turn == 0:	
				pygame.draw.circle(screen,RED,(posX,SQUARESIZE//2),RADIUS)
			else:
				pygame.draw.circle(screen,YELLOW,(posX,SQUARESIZE//2),RADIUS)		

		if event.type == pygame.MOUSEBUTTONDOWN:
			y_moving_piece = RADIUS
			dy = 1
			if turn == 0:
				posX = event.pos[0]
				sel = posX//SQUARESIZE #'Player 1, make your selection (0-6):'))
				if is_valid_location(board, sel):
					row = get_next_open_row(board, sel)
					drop_piece(board, row, sel, 1)
					print_board(board)

					pygame.time.delay(50)
					while y_moving_piece < (row+1)*SQUARESIZE + RADIUS:
						pygame.draw.rect(screen, BLACK,(0,0,SQUARESIZE * COL_COUNT, SQUARESIZE * (ROW_COUNT+1)))
						dropping_piece(sel,1,yPos=y_moving_piece)
						draw_board(board)
						pygame.display.update()
						y_moving_piece += dy	

					cells_filled[(row,sel)] = True
					draw_board(board)
					pygame.display.update()	
					
					if winning_move(board, 1):
						print('Player 1 WINS!!!')
						pygame.draw.rect(screen, BLACK,(0,0,WIDTH,SQUARESIZE))
						message_winner(screen,1, RED)
						pygame.display.update()	
						pygame.time.wait(3000)
						game_over = True
						
			else:
				posX = event.pos[0] #'Player 2, make your selection (0-6):'))
				sel = posX//SQUARESIZE
				if is_valid_location(board, sel):
					row = get_next_open_row(board, sel)
					drop_piece(board, row, sel, 2)
					print_board(board)
					
					pygame.time.delay(50)
					while y_moving_piece < (row+1)*SQUARESIZE + RADIUS:
						pygame.draw.rect(screen, BLACK,(0,0,SQUARESIZE * COL_COUNT, SQUARESIZE * (ROW_COUNT+1)))
						dropping_piece(sel,2,yPos=y_moving_piece)
						draw_board(board)
						pygame.display.update()
						y_moving_piece += dy	

					cells_filled[(row,sel)] = True
					draw_board(board)
					pygame.display.update()		
					
					if winning_move(board, 2):
						print('Player 2 WINS!!!')
						pygame.draw.rect(screen, BLACK,(0,0,WIDTH,SQUARESIZE))
						message_winner(screen,2, YELLOW)
						pygame.display.update()	
						pygame.time.wait(3000)
						game_over = True

			#cells_filled[(row,sel)]=True			

			turn += 1
			turn = turn % 2				

		pygame.display.update()