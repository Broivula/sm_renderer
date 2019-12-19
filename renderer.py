import pygame


def render(data):
	
	pygame.init()

	black = (0, 0, 0)
	white = (255, 255, 255)


	X = 600
	Y = 1000

	display_surface = pygame.display.set_mode((X,Y))

	font = pygame.font.Font('freesansbold.ttf', 32)
	text = font.render(data, True, white, black) 
	textRect = text.get_rect()
	textRect.center = (X // 2, Y // 2) 
	display_surface.fill(black)
	display_surface.blit(text, textRect)
		
	pygame.display.update()
		

