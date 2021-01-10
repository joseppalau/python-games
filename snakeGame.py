import pygame


class Snake(object):

	def __init__(self, color, position):
		pass

	def move(self):
		pass

	def reset(self, position):
		pass

	def addCube(self):
		pass

	def draw(self, surface):
		pass	


def drawGrid(width, rows, surface):
	sizeCell = width // rows
	x = 0
	y = 0

	for l in range(rows):
		x += sizeCell
		y += sizeCell

def redrawWindow(surface):
	surface.fill((0,0,0))
	#drawGrid(width, rows, surface)
	pygame.display.update()
	pass

def main():
	width = 500
	height = 500
	rows = 20
	win = pygame.display.set_mode((width, height))
	#s = Snake((255,0,0), (10,10))

	clock = pygame.time.Clock()
	flag = True

	while flag:

		pygame.time.delay(50)
		clock.tick(10)
		redrawWindow(win)


print('hello')


main()