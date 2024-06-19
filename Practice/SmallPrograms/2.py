import pygame
pygame.init()
# to init the modules of library
gameWindow = pygame.display.set_mode((900,900))
# to display a window.

# 2

pygame.display.set_caption("Snakes")
# to set a for our game window.

exit_game = False
# variable
# till it is not true game will not exit

game_over = False
# variable to display game over and ask user if he wants to continue.

# 3

while not exit_game:
    for event in pygame.event.get():
        # konsa event?
        if event.type == pygame.QUIT: # x button click event
            exit_game=True
        if event.type == pygame.KEYDOWN:
            # kya key dabi?
            if event.key == pygame.K_RIGHT:
                # konsi key dabi?
                exit_game = True
        # used to get mouse position for loop in event
        print(pygame.display.is_fullscreen())

pygame.quit()
# reverse of pygame.init()

quit()


# 5
# event handling


