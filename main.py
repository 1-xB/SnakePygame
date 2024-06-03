import pygame, random
from pygame.math import Vector2
from sys import exit


class Fruit():
    def __init__(self) -> None:
        self.x = random.randint(0, cell_number - 1 )
        self.y = random.randint(0, cell_number - 1)     
        self.pos = Vector2(self.x, self.y)
        self.apple = pygame.image.load('Graphics/apple.png')
        self.apple_rect = self.apple.get_rect(topleft=(int(self.pos.x * cell_size), int(self.pos.y * cell_size)))
    
    def draw(self):
        screen.blit(self.apple, self.apple_rect)

class Snake():
    def __init__(self) -> None:
        self.body = [Vector2(5,10), Vector2(6, 10) , Vector2(7, 10),]
        self.direction = Vector2(1, 0)
    def draw(self):
        for block in self.body:
            block_rect = pygame.Rect(int(block.x * cell_size), int(block.y * cell_size), cell_size, cell_size)
            pygame.draw.rect(screen, ('#2c5da3'), block_rect)
    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, self.body[0] + self.direction)
        self.body = body_copy[:]
        
# clock
clock = pygame.time.Clock()

# cell 
cell_size = 40 #  rozmiar komórki
cell_number = 20

# basic settings
pygame.init()
screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))

# instances
fruit = Fruit()
snake = Snake()

# timers
screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update, 150)


while True:
    for event in pygame.event.get():
        # quit
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        # timers
        if event.type == screen_update:
            snake.move_snake()
            
        # moves
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                snake.direction = Vector2(1, 0)
            if event.key == pygame.K_UP:
                snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                snake.direction = Vector2(0, 1)
            
        
    screen.fill('#e5b952')
    fruit.draw()
    snake.draw()
    
    pygame.display.update()
    clock.tick(60)
    