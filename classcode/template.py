import pygame

# Pygame Init tells pygame we're gonna do pygame stuff 
pygame.init()

# Screen width & height definitions
screen_width = 1200
screen_height = 800
caption = "Keypress"
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption(caption)

# colors
RED = [255, 0, 0] # all in caps so we can signal to other codewriters that our "variables" here are not supposed to be changed - are like "constants"
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
YELLOW = [255,255,0]
GREEN = [0,255,0]

running = True

fps = 120
fps_clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False

    pygame.display.flip() # refresh the screen
    fps_clock.tick(fps)