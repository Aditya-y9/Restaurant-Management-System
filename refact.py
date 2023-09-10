import random
import pygame
pygame.init()
# initializing pygame modules

red = (255, 0, 0)
# color definitions
white = (255, 255, 255)
black = (0, 0, 0)

screen_w = 500 # variables for screen size
screen_h = 800

pos_x  = 30 # rectangle (snake) positions
pos_y = 30

size_x = 40  # rectangle size
size_y = 40

vel_x = 0 # velocity definitions
vel_y = 0

# modules to generate random integers
target_x = random.randint(80, screen_w-200)  # starting from 20 till screen_w /2 because we want to keep food in middle
target_y = random.randint(80, screen_h-200)  # random value of x and y in the limit 0 to screen boundaries.

# to assign velocity
master_vel = 8



screen = pygame.display.set_mode((screen_h, screen_w))
pygame.display.set_caption("Snakes")



score = 0


end_game = False
game_over = False

clock = pygame.time.Clock()

while not end_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                vel_x = master_vel
                vel_y = 0
            if event.key == pygame.K_LEFT:
                vel_x = -master_vel
                vel_y = 0
            if event.key == pygame.K_UP:
                vel_y = -master_vel
                vel_x = 0
            if event.key == pygame.K_DOWN:
                vel_y = master_vel
                vel_x = 0
    screen.fill(black)
    if abs(pos_x - target_x)<30 and abs(pos_y - target_y)<30:
        score += 1
        print("Score: ", score)
        target_x = random.randint(80, screen_w/2 + 100)
        # starting from 80 till screen_w /2 + 100 because we want to keep food in middle
        target_y = random.randint(80, screen_h/2 + 100)
        # starting from 80 till screen_w /2 + 100 because we want to keep food in middle
        while abs(pos_x-target_x) < 90:
            target_x = random.randint(10, screen_w / 2 + 100)
            target_y = random.randint(10, screen_h / 2 + 100)
    # random value of x and y in the limit 0 to screen boundaries.
    target = pygame.draw.rect(screen, red, [target_x, target_y, 20, 20])
    pos_x += vel_x
    pos_y += vel_y
    pygame.draw.rect(screen, white, [pos_x, pos_y, size_x, size_y])
    pygame.display.update()
    tick = clock.tick(60)
    