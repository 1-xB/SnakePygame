import pygame
from sys import exit

# basic settings
pygame.init()
screen = pygame.display.set_mode((800,800))

# clock
clock = pygame.time.Clock()

# cell - kratka

while True:
    for event in pygame.event.get():
        # quit
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    screen.fill('#d30bdd')
    
    
    pygame.display.update()
    clock.tick(60)
    