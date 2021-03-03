import pygame
import sys
from network import Network

class Player():
	def __init__(self, x, y, width, height, color):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color = color
		self.rect =(x,y,width,height) 
		self.speed = 3

	def draw(self, screen):
		pygame.draw.rect(screen, self.color, self.rect)	

	def move(self, dx, dy):
		self.x += dx * self.speed
		self.y += dy * self.speed
		self.update()	

	def update(self):
		self.rect=(self.x, self.y, self.width, self.height)	
			
def read_pos(data):
	data = data.split(',')
	return (int(data[0]), int(data[1]))

def make_pos(data):
	return str(data[0]) + ',' + str(data[1])

def redraw_screen(screen, player1, player2):
	screen.fill(color=(255,255,255))
	player1.draw(screen)
	player2.draw(screen)
	pygame.display.update()

def main(screen, n):
	run = True
	startPos = read_pos(n.get_pos())
	p1 = Player(startPos[0],startPos[1],100,100,(0,255,0))
	p2 = Player(0,0,100,100,(0,255,0))
	#clock = pygame.time.Clock() 

	while run:
		#clock.tick(60)
		p2Pos = read_pos(n.sending(make_pos((p1.x, p1.y))))
		p2.x = p2Pos[0]
		p2.y = p2Pos[1]
		p2.update()

		dx = 0
		dy = 0
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					dx = -1
				if event.key == pygame.K_RIGHT:
					dx = 1
				if event.key == pygame.K_UP:
					dy = -1
				if event.key == pygame.K_DOWN:	
					dy = 1


		p1.move(dx, dy)
		redraw_screen(screen, p1, p2)	


if __name__ == '__main__':
	
	WIDTH = 500
	HEIGHT = 500

	screen = pygame.display.set_mode(size=(WIDTH, HEIGHT))
	pygame.display.set_caption('CLIENT')

	server = input('Introduce server')
	port = int(input('Introduce port'))

	n = Network(server, port)


	main(screen, n)			




