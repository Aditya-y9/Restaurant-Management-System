import pygame
pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)


screen_width = 1200
screen_height = 600
snake_x = 45
snake_y = 55
snake_size = 10

gamewindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snakes Mini Project")
pygame.display.update()

end_game = False
game_over = True



while not end_game:
    for event in pygame.event.get():
        pass
        # print(event)
    gamewindow.fill(white)
    pygame.display.update()
    if event.type == pygame.QUIT:
        end_game = True

    pygame.draw.rect(gamewindow, red, [snake_x, snake_y, snake_size, snake_size])
    # arguments surface ,color , [list of x pos,y pos , x size, y size ]
    pygame.display.update()


