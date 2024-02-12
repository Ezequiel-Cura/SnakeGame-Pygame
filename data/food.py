import random
import pygame
from data.constants import *

class Food:
    def __init__(self,size) -> None:

        self.cordinates = self.random_pos_generator(size)
        self.eaten = False

        self.rect = pygame.Rect(self.cordinates[0],self.cordinates[1],50,50)


    def update(self,screen,size):
        self.draw(screen)

        if self.eaten == True:
            self.cordinates = self.random_pos_generator(size)
            self.rect.x = self.cordinates[0]
            self.rect.y = self.cordinates[1]

            self.eaten = False


    def random_pos_generator(self,size):

        x = random.randint(0,size[0] // 50) * 50 
        y = random.randint(0,size[1] // 50) * 50

        if x == size[0]:
            x -= 50
        
        if y == size[1]:
            y -= 50

        

        return (x,y)


    def draw(self,screen):

        pygame.draw.rect(screen,RED,self.rect)
