from data.constants import *
import pygame
from data.food import Food

class Snake():
    def __init__(self) -> None:
        
        self.flag_time = True
        self.score = 0

        self.change = False
        self.can_change = True

        self.tiempo = pygame.time.get_ticks() 
        self.snake_length = 2
        self.is_dead = False
        self.direction = SnakeDirection.RIGHT

        self.cordinates = []
        self.squares = []

        self.speed = 100

        for i in range(0,self.snake_length):
            self.cordinates.append((500,500))

        for x,y in self.cordinates:
            self.squares.append(pygame.rect.Rect(x,y,50,50))


    def reset_snake(self):
        self.is_dead = False
        self.direction = SnakeDirection.RIGHT
        self.snake_length = 2
        self.flag_time = True

        self.score = 0
        self.cordinates = []
        self.squares = []

        for i in range(0,self.snake_length):
            self.cordinates.append((500,500))

        for x,y in self.cordinates:
            self.squares.append(pygame.rect.Rect(x,y,50,50))

    def update(self,screen,size,food,infinte_border, color):

        x,y = self.cordinates[0]

        self.change_direction()

        if self.direction == SnakeDirection.RIGHT :
            x += 50
        elif self.direction == SnakeDirection.LEFT:
            x -= 50
        elif self.direction == SnakeDirection.DOWN:
            y += 50
        elif self.direction == SnakeDirection.UP:
            y -= 50

        self.check_collisions(food,size,(x,y),infinte_border)

        if infinte_border == True:
            x,y = self.infinte_border_fun(x,y,size,infinte_border)

        self.draw(screen,color)
        self.movement(x,y)


    def movement(self,x,y):
        if self.flag_time == True:
            self.tiempo = pygame.time.get_ticks() 
            self.flag_time = False

        if pygame.time.get_ticks() > self.tiempo + self.speed:
            self.cordinates.insert(0,(x,y))
            self.squares.insert(0,pygame.rect.Rect(x,y,50,50))
            self.tiempo += self.speed

            print(self.speed)
            del self.cordinates[-1]
            del self.squares[-1]

    def infinte_border_fun(self,x,y,size,infinte_border):

        if x >= size[0]:
            x = 0
        
        if x < 0:
            x = size[0]
        
        if y >= size[1]:
            y = 0
        
        if y < 0:
            y = size[1]

        return x,y


    def draw(self,screen,color):

        for i in range(0,len(self.squares)):
            if i == 0:
                pygame.draw.rect(screen,WHEAT,self.squares[i])
            else:
                pygame.draw.rect(screen,color,self.squares[i])
            
    
    def change_direction(self):

        old_direction = self.direction

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and self.can_change == True:
            if old_direction != SnakeDirection.RIGHT:
                self.change = True
                self.can_change = False
                self.direction = SnakeDirection.LEFT
        elif keys[pygame.K_d] and self.can_change == True:
            if old_direction != SnakeDirection.LEFT:
                self.change = True
                self.can_change = False
                self.direction = SnakeDirection.RIGHT
        elif keys[pygame.K_w] and self.can_change == True:
            if old_direction != SnakeDirection.DOWN:
                self.change = True
                self.can_change = False
                self.direction = SnakeDirection.UP
        elif keys[pygame.K_s] and self.can_change == True:
            if old_direction != SnakeDirection.UP:
                self.change = True
                self.can_change = False
                self.direction = SnakeDirection.DOWN


        if self.change == True:
            pygame.time.set_timer(pygame.USEREVENT , 100, 1)
            self.change = False

    
    def check_collisions(self,food:Food, size,pos, infinte_border):

        x,y = self.cordinates[0]

        if self.squares[0].colliderect(food.rect) and food.eaten == False:
            self.snake_length += 1
            self.score += 1
            self.cordinates.insert(0,(pos[0],pos[1]))
            self.squares.insert(0,pygame.rect.Rect(pos[0] ,pos[1],50,50))
            food.eaten = True


        for i in range(3,len(self.squares)):
            if self.squares[0].colliderect(self.squares[i]):
                self.is_dead = True

        if infinte_border == False:
            if x >= size[0]  or y >= size[1]  or x <= 0 -1  or y <= 0 -1 :
                self.is_dead = True



