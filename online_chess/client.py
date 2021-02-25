import pygame

WITH = 500
HEIGHT = 500

screen = pygame.display.set_mode(size=(WITH, HEIGHT))
pygame.display.set_caption(title='CLIENT')

clientNumber = 0

class Player():
	def __init__(self, x, y, width, height, color):
		self.x = x
		self.y = yself.width = width
		self.height = height
		self.color = color
		self.rect =(x,y,width,height) 

	def draw(self, screen):
		pygame.draw.rect(screen, self.color, self.rect)	


def redraw_screen():
	screen.fill(color=(255,255,255))
	pygame.display.update()

def main():
	run = True

	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()




