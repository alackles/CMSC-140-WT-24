import pygame

# Pygame Init tells pygame we're gonna do pygame stuff 
pygame.init()

# Screen width & height definitions
screen_width = 1200
screen_height = 800
caption = "Keypress"
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption(caption)

cat_img = pygame.image.load('cat.png')
cat_rect = cat_img.get_rect()
cat_rect.center = [100, 400]
cat_x = 100
cat_y = 400

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
        if event.type == pygame.QUIT:
            running = False

        # check for key press
        elif event.type == pygame.KEYDOWN:
            print("Key down")
            # check type of key
            if event.key == pygame.K_w:
                print("w key pressed")
        
        elif event.type == pygame.MOUSEMOTION:
            cat_x, cat_y = event.pos
        
    screen.blit(cat_img, [cat_x, cat_y])
            
        
        #elif event.type == pygame.KEYUP:
        #    print("Key up")
        #elif event.type == pygame.MOUSEBUTTONDOWN:
        #    print("Mouse button down")

    pygame.display.flip() # refresh the screen
    fps_clock.tick(fps)