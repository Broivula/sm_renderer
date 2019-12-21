import pygame

class Renderer:

	black = (0, 0, 0)
	white = (255, 255, 255)
	X = 600
	Y = 1000
	display_surface = None
	text_elements = {}

	def __init__(self):	
		pygame.init()
		self.display_surface = pygame.display.set_mode((self.X, self.Y))
		
	
	def update_rendered_data(self, data):
		self.text_elements[data["uid"]] = self.create_text_element(data)
		self.display_surface.fill(self.black)
		self.render()
		
		

	def create_text_element(self, data):
		font = pygame.font.Font('freesansbold.ttf', 32)
		text = font.render(data["content"], True,  self.white,  self.black) 
		textRect = text.get_rect()
		textRect.center = (data["posX"],  data["posY"]) 
		return (text, textRect)
	

	def render(self):
		for key in list(self.text_elements):
			element = self.text_elements[key]
			self.display_surface.blit(element[0], element[1])
		
		pygame.display.update()
		

