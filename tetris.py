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

shape_colors = {}

while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()



