import pygame
from settings import *
from player import Player


class Game:

    def __init__(self):
        self.screen = pygame.display.get_surface()

        # Create group
        self.create_group()

        # Create instance
        player = Player(self.player_group, 300, 500)

        # Background
        self.bg_img = pygame.image.load('assets/img/field.png')
        self.bg_y = 0  # initial y axis
        self.scroll_speed = 1

    def create_group(self):
        self.player_group = pygame.sprite.GroupSingle()

    def scroll_bg(self):
        self.bg_y = (self.bg_y + self.scroll_speed) % screen_height
        self.screen.blit(self.bg_img, (0, self.bg_y - screen_height))
        self.screen.blit(self.bg_img, (0, self.bg_y))

    def run(self):
        # self.screen.blit(self.bg_img, (0, 0))
        self.scroll_bg()

        # Draw group
        self.player_group.draw(self.screen)
        self.player_group.update()
