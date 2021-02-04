import pygame
import random

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
top_left_y = (s_height - play_height)//2

screen = pygame.display.set_mode((s_width,s_height))

BLUE = (0,102,204)
pygame.draw.rect(screen, BLUE, (top_lef_x,top_left_y,play_width,play_height))
pygame.display.update()


S = [[],[]]
Z = [[],[]]
I = [[],[]]
O = [[]]
J = [[],[],[],[]]
L = [[],[],[],[]]
T = [[],[],[],[]] 

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
	grid = [ (0,0,0) for _ in range(10) for _ in range(20)]

	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if (j,i) in locked_pos:
				c = locked_pos[(j,i)]
				grid[i][j] = c
	return grid			

def draw_grid(surface):
	surface.fill((0,0,0))
	
	pygame.font.init()
	font = pygame.font.SysFont('comicsans', 69)
	label = font.render('Tetris', 1, (255,255,255))

	surface.blit(lable, (top_lef_x + play_width/2 - label.get_with()//2, 30)

def get_shape():
	return random.choice(shapes)


while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()



