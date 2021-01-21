import pygame
import random

side = 500
rows = 20

class Cube(object):

	def __init__(self, start, dirnx=1, dirny= 0, color=(255,0,0)):
		self.pos = start
		self.dirnx = dirnx
		self.dirny = dirny
		self.color = color

	def move(self, dirnx, dirny):
		self.dirnx = dirnx
		self.dirny = dirny
		self.pos = (self.pos[0]+dirnx, self.pos[1]+dirny)
	

	def draw(self, surface, eyes= False):
		dis = side // rows		
		i = self.pos[0]
		j = self.pos[1]

		pygame.draw.rect(surface, self.color, (i*dis+1, j*dis+1, dis-2, dis-2))

		if eyes:
			centre = dis // 2
			radius = 3
			circleMiddle = (i*dis+centre-radius, j*dis+8)
			circleMiddle2 = (i*dis + dis - radius*2, j*dis+8)
			pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
			pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)

class Snake(object):
	body = []
	turns = {}

	def __init__(self, color, position):
		self.color = color
		self.head = Cube(position)
		self.body.append(self.head)
		self.dirnx = 1
		self.dirny = 0

	def move(self):
		'''for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()'''

		keys = pygame.key.get_pressed()
			
		if keys[pygame.K_LEFT]:
			self.dirnx = -1
			self.dirny = 0
			self.turns[self.head.pos[:]] = [self.dirnx, self.dirny] 

		elif keys[pygame.K_RIGHT]:
			self.dirnx = 1
			self.dirny = 0
			self.turns[self.head.pos[:]] = [self.dirnx, self.dirny] 

		elif keys[pygame.K_UP]:
			self.dirnx = 0
			self.dirny = -1				
			self.turns[self.head.pos[:]] = [self.dirnx, self.dirny] 

		elif keys[pygame.K_DOWN]:
			self.dirnx = 0
			self.dirny = 1
			self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

		for i,c in enumerate(self.body):
			p = c.pos[:]
			if p in self.turns:
				turn = self.turns[p]
				c.move(turn[0], turn[1])
				if i == len(self.body)-1:
					self.turns.pop(p)

			else:
				if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (rows-1, c.pos[1])
				elif c.dirnx == 1 and c.pos[0] >= rows - 1: c.pos= (0,c.pos[1])
				elif c.dirny == 1 and c.pos[1] >= rows-1: c.pos = (c.pos[0], 0) 
				elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0], rows-1)
				else: c.move(c.dirnx,c.dirny)		


	def reset(self, position):
		pass

	def addCube(self):
		tail = self.body[-1]
		dx, dy = tail.dirnx, tail.dirny

		if dx == 1 and dy == 0: 
			self.body.append(Cube((tail.pos[0]-1, tail.pos[1])))
		elif dx == -1 and dy == 0:
			self.body.append(Cube((tail.pos[0]+1, tail.pos[1])))
		elif dx == 0 and dy == 1:
			self.body.append(Cube((tail.pos[0], tail.pos[1]-1)))
		else:
			self.body.append(Cube((tail.pos[0], tail.pos[1]+1)))

		self.body[-1].dirnx = dx
		self.body[-1].dirny = dy			

	def draw(self, surface):
		for i, c in enumerate(self.body):
			if i == 0:
				c.draw(surface, True)
			else:
				c.draw(surface)	


def drawGrid(side, rows, surface):
	sizeCell = side // rows
	x = 0
	y = 0

	for l in range(rows):
		x += sizeCell
		y += sizeCell

		pygame.draw.line(surface, (255,255,255), (x,0), (x,side))
		pygame.draw.line(surface, (255,255,255), (0,y), (side,y))


def redrawWindow(surface, snake, snack):
	surface.fill((0,0,0))
	drawGrid(side, rows, surface)
	snack.draw(surface)
	snake.draw(surface)
	pygame.display.update()


def randomSnake(item):
	cubes = item.body

	while True:
		x = random.randrange(rows)
		y = random.randrange(rows)

		if len(list(filter(lambda z: z.pos == (x,y), cubes))) > 0:
			continue
		else:
			break

	return (x,y)			
	

def main():
	
	win = pygame.display.set_mode((side, side))
	s = Snake((255,0,0), (10,10))
	snack = Cube(randomSnake(s), color=(0,255,0))

	clock = pygame.time.Clock()
	flag = True
	r = 0

	while flag:
		pygame.time.delay(50)
		clock.tick(10)
		s.move()

		if s.body[0].pos == snack.pos:
			s.addCube()
			snack = Cube(randomSnake(s), color=(0,255,0))

		redrawWindow(win, s, snack)

main()