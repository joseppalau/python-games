import pygame
import random
import sys

#pygame.font.init()

#GLOBAL WORDS
s_width = 800
s_height = 700
play_width = 300
play_height = 600
block_size = 30 
# given the block size = 30, those are the numbers of cells in each axis
#10 cells width - x axis
#20 cells height - y aixs
top_lef_x = (s_width - play_width)//2
top_left_y = (s_height - play_height) -25

screen = pygame.display.set_mode((s_width,s_height))
pygame.display.set_caption('Tetris')

BLUE = (0,102,204)
pygame.draw.rect(screen, BLUE, (top_lef_x,top_left_y,play_width,play_height))
pygame.display.update()


S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S,Z,I,O,J,L,T]
shape_colors = [(0,255,0),(255,0,0),(0,255,255),(255,255,0),(255,165,0),(0,0,255),(128,0,128)]

class Piece(object):
	def __init__(self, x, y, shape):
		self.x = x
		self.y = y
		self.shape = shape
		self.color = shape_colors[shapes.index(shape)]
		self.rotation = 0

def create_grid(locked_pos = {}):
	grid = [[(0,0,0) for _ in range(10)] for _ in range(20)]

	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if (j,i) in locked_pos:
				c = locked_pos[(j,i)]
				grid[i][j] = c
	return grid		

def convert_shape(piece):
	positions = []
	format = piece.shape[piece.rotation % len(piece.shape)]

	for i, line in enumerate(format):
		row = list(line)
		for j,column in enumerate(row):
			if column == '0':
				positions.append((piece.x + j, piece.y + i))

	for i,pos in enumerate(positions):
		positions[i] = (pos[0] - 2, pos[1] - 4)

	return positions	


def valid_space(piece, grid):
	accepted_pos = [(j,i) for j in range(10) for i in range(20) if grid[i][j] == (0,0,0) ]

	formatted = convert_shape(piece)

	for pos in formatted:
		if pos not in accepted_pos:
			if pos[1] > -1:
				return False

	return True		


def check_lost(positions):
	for pos in positions:
		x,y = pos
		if y < 1:
			return True

	return False								


def draw_grid(surface):
	x = top_lef_x
	y = top_left_y

	xc = play_width//block_size
	yc = play_height//block_size

	for _ in range(xc-1):
		pygame.draw.line(surface, (255,255,255), (x+block_size, y), (x+block_size, y+play_height))
		x += block_size

	x = top_lef_x 

	for _ in range(yc-1):
		pygame.draw.line(surface, (255,255,255), (x, y+block_size), (x+play_width, y+block_size))
		y += block_size

	x = top_lef_x
	y = top_left_y	


def draw_next_shape(surface, piece): 	
	pygame.font.init()
	font = pygame.font.SysFont('comicsans', 50)
	label = font.render('Next Shape', 1, (255,255,255))

	lx = top_lef_x + play_width + 40
	ly = top_left_y + play_height//2 -100

	format = piece.shape[piece.rotation % len(piece.shape)]

	for i, line in enumerate(format):
		row = list(line)
		for j,column in enumerate(row):
			if column == '0':
				pygame.draw.rect(surface, piece.color, (lx + j*block_size, ly + 60 + i*block_size, block_size, block_size),0)

	surface.blit(label, (lx,ly))				
			

def draw_window(surface, grid):
	surface.fill((0,0,0))
	
	pygame.font.init()
	font = pygame.font.SysFont('comicsans', 69)
	label = font.render('Tetris', 1, (255,255,255))
	surface.blit(label, (top_lef_x + play_width//2 - label.get_width()//2, 20))

	for i in range(len(grid)):
		for j in range(len(grid[i])):
			pygame.draw.rect(surface, grid[i][j], (top_lef_x + j*block_size, top_left_y + i*block_size, block_size, block_size))	

	draw_grid(surface)	


def get_shape():
	return Piece(5, 0, random.choice(shapes))


def main(surface):
	locked_pos = {}
	grid = create_grid(locked_pos)

	change_piece = False
	run = True
	current_piece = get_shape()
	next_piece = get_shape()
	clock = pygame.time.Clock()
	fall_time = 0
	fall_speed = 0.27

	while run:

		grid = create_grid(locked_pos)
		fall_time += clock.get_rawtime()
		clock.tick()

		if fall_time/1000 > fall_speed:
			fall_time = 0
			current_piece.y += 1
			if not valid_space(current_piece, grid) and current_piece.y > 0:
				current_piece.y -= 1
				change_piece = True


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				sys.exit()

			if event.type == pygame.KEYDOWN:
				
				if event.key == pygame.K_LEFT:
					current_piece.x -= 1
					if not valid_space(current_piece, grid):
						current_piece.x += 1

				if event.key == pygame.K_RIGHT:
					current_piece.x += 1
					if not valid_space(current_piece, grid):
						current_piece.x -= 1

				if event.key == pygame.K_DOWN:	
					current_piece.y += 1
					if not valid_space(current_piece, grid):
						current_piece.y -= 1				

				if event.key == pygame.K_UP:
					current_piece.rotation += 1
					if not valid_space(current_piece, grid):
						current_piece.rotation -= 1

		shape_pos = convert_shape(current_piece)
		
		for i in range(len(shape_pos)):
			x,y = shape_pos[i]
			if y > -1:
				grid[y][x] = current_piece.color 				

		if change_piece:
			for pos in shape_pos:
				p = (pos[0],pos[1])
				locked_pos[p] = current_piece.color

			current_piece = next_piece
			next_piece = get_shape()

			change_piece = False	

		draw_window(surface, grid)		
		draw_next_shape(surface, next_piece)	
		pygame.display.update()

		
		if check_lost(locked_pos):
			run = False	

	pygame.display.quit()		


def main_menu(surface):
	main(surface)


main_menu(screen)


				


