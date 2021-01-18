import pygame

side = 500
rows = 20

class Cube(object):
	rows = 0
	w = 0

	def __init__(self, start, dirnx=1, dirny= 0, color=(255,0,0)):
		pass

	def move(self, dirnx, dirny):
		pass

	def draw(self, surface, eyes= False):
		pass		

class Snake(object):
	body = []
	turns = []

	def __init__(self, color, position):
		self.color = color
		self.head = Cube(position)
		self.body.append(self.head)

	def move(self):
		pass

	def reset(self, position):
		pass

	def addCube(self):
		pass

	def draw(self, surface):
		pass	


def drawGrid(side, rows, surface):
	sizeCell = side // rows
	x = 0
	y = 0

	for l in range(rows):
		x += sizeCell
		y += sizeCell

		pygame.draw.line(surface, (255,255,255), (x,0), (x,side))
		pygame.draw.line(surface, (255,255,255), (0,y), (side,y))

def redrawWindow(surface):
	surface.fill((0,0,0))
	drawGrid(side, rows, surface)
	pygame.display.update()
	pass

def main():
	
	win = pygame.display.set_mode((side, side))
	#s = Snake((255,0,0), (10,10))

	clock = pygame.time.Clock()
	flag = True

	while flag:

		pygame.time.delay(50)
		clock.tick(10)
		redrawWindow(win)


main()