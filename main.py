import pygame
from settings import *
from game import Game

pygame.init()

# Create window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('2D Shooting')

# Setup for FPS
clock = pygame.time.Clock()

# Game
game = Game()

# Main loop for the game ------------------------------------
run = True
while run:

    # Background
    screen.fill(BLACK)

    # Run game
    game.run()

    # Get event
    for event in pygame.event.get():
        # Quit
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_ESCAPE:
                run = False

    # Update
    pygame.display.update()
    clock.tick(FPS)

# ------------------------------------------------------------
pygame.quit()
