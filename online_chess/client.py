import pygame
import sys
from network import Network
from player import Player

		
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
	p1 = n.get_pos()
	#clock = pygame.time.Clock() 

	while run:
		#clock.tick(60)
		p2 = n.sending(p1)
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




