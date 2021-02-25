import pygame

WITH = 500
HEIGHT = 500

screen = pygame.display.set_mode(size=(WITH, HEIGHT))
pygame.display.set_caption('CLIENT')

clientNumber = 0

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
		self.rect=(self.x, self.y, self.width, self.height)		


def redraw_screen(screen, player):
	screen.fill(color=(255,255,255))
	player.draw(screen)
	pygame.display.update()

def main(screen):
	run = True
	p = Player(50,50,100,100,(0,255,0))
	clock = pygame.time.Clock()

	while run:
		clock.tick(60)
		dx = 0
		dy = 0
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					dx = -1
				if event.key == pygame.K_RIGHT:
					dx = 1
				if event.key == pygame.K_UP:
					dy = -1
				if event.key == pygame.K_DOWN:	
					dy = 1

		p.move(dx, dy)
		redraw_screen(screen, p)	

main(screen)			




