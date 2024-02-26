import pygame

pygame.init()

screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("test2 game")

red = [255, 0, 0] # all in caps so we can signal to other codewriters that our "variables" here are not supposed to be changed - are like "constants"
white = [255, 255, 255]
black = [0, 0, 0]
yellow = [255,255,0]
green = [0,255,0]

# generic code for loading an image into pygame and picking a center
cat_img = pygame.image.load('cat.png')
cat_rect = cat_img.get_rect()
cat_rect.center = [100, 400]

cat_x = 10
cat_y = 10

# change size
# first argument: the image
# second argument: its new size
#cat_img = pygame.transform.scale(cat_img, [500, 500])
#print(cat_rect)

running = true

fps = 120
fps_clock = pygame.time.clock()

direction = 'left'

while running:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = false

    screen.blit(cat_img, cat_rect)

    if direction == 'right':
        cat_x = cat_x + 5
        if cat_x > screen_width-100:
            direction = 'down'
            cat_img = pygame.transform.flip(cat_img, true, false)

            
    elif direction == 'left':
        cat_x = cat_x - 5
        if cat_x < 0:
            direction = 'up'
            cat_img = pygame.transform.flip(cat_img, true, false)
    
    elif direction == 'down':
        cat_y = cat_y + 5
        if cat_y > screen_height -100:
            direction = 'left'
            cat_img = pygame.transform.flip(cat_img, false, true)
    
    elif direction == 'up':
        cat_y -= 5
        if cat_y < 0:
            direction = 'right'
            cat_img = pygame.transform.flip(cat_img, false, true)
    
    screen.blit(cat_img, [cat_x, cat_y])
    pygame.display.flip() # refresh the screen
    fps_clock.tick(fps)