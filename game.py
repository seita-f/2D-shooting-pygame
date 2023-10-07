import pygame
from settings import *
from player import Player
from monster import Monster
from support import draw_text
import random


class Game:

    def __init__(self):
        self.screen = pygame.display.get_surface()

        # Create group
        self.create_group()

        # Player
        self.player = Player(self.player_group, 300, 500, self.monster_group)

        # Arrow
        # arrow = Arrow(self.arrow_group, 50, 100)

        # Background
        self.bg_img = pygame.image.load('assets/img/field.png')
        self.bg_y = 0  # initial y axis
        self.scroll_speed = 1
        self.timer = 0

        # Game over
        self.game_over = False

    def create_group(self):
        self.player_group = pygame.sprite.GroupSingle()
        self.monster_group = pygame.sprite.Group()
        self.arrow_group = pygame.sprite.Group()

    def create_monsters(self):
        self.timer += 1
        if self.timer > 50:
            monster = Monster(self.monster_group, random.randint(50, 550), 0, self.player.arrow_group)
            self.timer = 0

    def scroll_bg(self):
        self.bg_y = (self.bg_y + self.scroll_speed) % screen_height
        self.screen.blit(self.bg_img, (0, self.bg_y - screen_height))
        self.screen.blit(self.bg_img, (0, self.bg_y))

    def disp_game_over(self):
        if len(self.player_group) == 0:
            self.game_over = True
            draw_text(self.screen, "Game Over", screen_width // 2, screen_height // 2, 75, RED)
            draw_text(self.screen, "press RETURN to restart", screen_width // 2, screen_height // 2 + 100, 50, RED)

    def reset(self):
        key = pygame.key.get_pressed()

        # y-axis move
        if key[pygame.K_RETURN] and self.game_over:
            self.player = Player(self.player_group, 300, 500, self.monster_group)
            self.monster_group.empty()
            self.game_over = False
            # Debug
            print("Game is reset")

    def run(self):
        # self.screen.blit(self.bg_img, (0, 0))
        self.scroll_bg()

        # Generate monster
        self.create_monsters()

        # Draw Player
        self.player_group.draw(self.screen)
        self.player_group.update()

        # Draw Monster
        self.monster_group.draw(self.screen)
        self.monster_group.update()

        # Draw arrow
        self.arrow_group.draw(self.screen)
        self.arrow_group.update()

        # Game over
        self.disp_game_over()

        # Reset game
        self.reset()

