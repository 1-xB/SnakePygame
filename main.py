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
        self.body = [Vector2(5,10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(-1, 0)
        self.new_direction = True
        

    def draw(self):
        head_rect = pygame.Rect(int(self.body[0].x * cell_size),int(self.body[0].y * cell_size), cell_size -1, cell_size -1)
        pygame.draw.rect(screen, ('#1aad30'), head_rect)
        for block in self.body[1:]:
            block_rect = pygame.Rect(int(block.x * cell_size), int(block.y * cell_size), cell_size -1 , cell_size -1)
            pygame.draw.rect(screen, ('#04e526'), block_rect)

    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, self.body[0] + self.direction)
        self.body = body_copy[:]


class Main():
    def __init__(self) -> None:
        self.snake = Snake()
        self.fruit = Fruit()
        self.game = False
        self.start_menu = True
        self.score = 0
        
    def start(self):
        screen.fill('#e5b952')
        font = pygame.font.SysFont('arial', 30)
        logo = pygame.image.load('Graphics/logo.png')
        logo_rect = logo.get_rect(center=(int(cell_number * cell_size / 2), 200))
        screen.blit(logo, logo_rect)

        start_text = font.render('Press any key to start', True, (255, 255, 255))
        start_text_rect = start_text.get_rect(center=(int(cell_number * cell_size / 2), int(cell_number * cell_size / 2) + 50))
        screen.blit(start_text, start_text_rect)

    
    def update(self):
        self.snake.new_direction = True
        self.snake.move_snake()
        self.apple_collision()
        self.body_collision()
        
        
    def draw(self):
        self.score_window()
        self.fruit.draw()
        self.snake.draw()
        
        
        
    def apple_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            crunch_sound.play()
            self.fruit.pos = Vector2(random.randint(0, cell_number - 1 ), random.randint(0, cell_number - 1))
            while self.fruit.pos in self.snake.body:
                self.fruit.pos = Vector2(random.randint(0, cell_number - 1 ), random.randint(0, cell_number - 1))
            coords = int(self.fruit.pos.x * cell_size), int(self.fruit.pos.y * cell_size)
            self.fruit.apple_rect = self.fruit.apple.get_rect(topleft=(coords))
            self.snake.body.append(self.snake.body[-1])
            self.score += 1
    
    def body_collision(self):
        for block in self.snake.body[1:]:
            if block == self.snake.body[0] or (not (0 <= self.snake.body[0].x <= 19) or not (0 <= self.snake.body[0].y <= 19)):
                game_over.play()
                self.game = False
    
    def score_window(self):
        text = pygame.font.Font(None, 36)
        score_text = text.render(str(self.score), True, 'black')
        apple = pygame.image.load('Graphics/apple.png')
        apple_rect = apple.get_rect(topleft=(701, 725))
        pygame.draw.rect(screen, ('#bbce2d'), (700, 720, 90, 50))
        screen.blit(apple, apple_rect)
        screen.blit(score_text, (740, 735))
        

# clock
clock = pygame.time.Clock()

# cell 
cell_size = 40 # rozmiar komórki
cell_number = 20

# sounds
pygame.mixer.init()
crunch_sound = pygame.mixer.Sound('Sound/crunch.wav')
move_left = pygame.mixer.Sound('Sound/1.wav')
move_right = pygame.mixer.Sound('Sound/3.wav')
move_down = pygame.mixer.Sound('Sound/2.wav')
move_up = pygame.mixer.Sound('Sound/4.wav')
game_over = pygame.mixer.Sound('Sound/gameover.wav')

# basic settings
pygame.init()
screen = pygame.display.set_mode((cell_number*cell_size, cell_number*cell_size))

# instances
main = Main()

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
        if event.type == screen_update and main.game:
            main.update()
            
        
        if (event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN) and main.start_menu:
            main.start_menu = False
            main.game = True
        
        # moves
        if event.type == pygame.KEYDOWN and main.snake.new_direction and main.game:
            
            if event.key == pygame.K_LEFT or event.key == pygame.K_a and main.snake.direction != Vector2(1, 0) and main.snake.direction != Vector2(-1, 0):
                main.snake.new_direction = False
                move_left.play()
                main.snake.direction = Vector2(-1, 0)
                
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d and main.snake.direction != Vector2(-1, 0) and main.snake.direction != Vector2(1, 0):
                main.snake.new_direction = False
                move_right.play()
                main.snake.direction = Vector2(1, 0)
                
            if event.key == pygame.K_UP or event.key == pygame.K_w and main.snake.direction != Vector2(0, 1) and main.snake.direction != Vector2(0, -1):
                main.snake.new_direction = False
                move_up.play()
                main.snake.direction = Vector2(0, -1)\
                    
            if event.key == pygame.K_DOWN or event.key == pygame.K_s and main.snake.direction != Vector2(0, -1) and main.snake.direction != Vector2(0, 1):
                main.snake.new_direction = False
                move_down.play()
                main.snake.direction = Vector2(0, 1)
    if main.game:    
        screen.fill('#e5b952')
        main.draw()
        
    if main.start_menu:
         main.start()
        
    
    pygame.display.update()
    clock.tick(144)
