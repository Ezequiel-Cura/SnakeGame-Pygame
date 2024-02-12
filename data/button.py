import pygame
from data.constants import *

class Button:
    
	def __init__(self,x,y,image: pygame.Surface,size,text = "button",scale = 1, with_value = False) -> None:
		
		self.font = pygame.font.Font(None, 36) 


		if image == "":
			self.rect = pygame.Rect(x,y,size[0],size[1])
			self.text = self.font.render(text,False,WHITE)
			self.text_rect = self.text.get_rect()
			self.text_rect.center = (x,y)
			self.pos = (x,y)
			self.image = None
		else:
			width = image.get_width()
			height = image.get_height()
			self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
			self.rect = self.image.get_rect()
		
		
		self.rect.center = (x,y)
		self.clicked = False

		self.action = False

		self.with_value = with_value

	def draw(self,screen):
		
		if self.image == None:
			pygame.draw.rect(screen, RED, self.rect)
			screen.blit(self.text,self.text_rect)
		else:
			pass


	def update(self):
		self.action = False

		pos = pygame.mouse.get_pos()

		if self.rect.collidepoint(pos):
			
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				self.action = True

		
		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		return self.action


