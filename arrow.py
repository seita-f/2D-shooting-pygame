import pygame
from settings import *


class Arrow(pygame.sprite.Sprite):
    def __init__(self, groups, x, y):
        super().__init__(groups)

        # Image
        # self.image = pygame.Surface((10, 30))
        self.pre_image = pygame.image.load(f'assets/img/bow.png')
        self.image = pygame.transform.scale(self.pre_image, (24, 48))
        # Debug
        # self.image.fill(WHITE)
        self.rect = self.image.get_rect(midbottom=(x, y))

        # Move
        self.speed = 8

    def arrow_off_screen(self):
        if self.rect.bottom < 0:
            self.kill()

    def move(self):
        self.rect.y -= self.speed

    def update(self):
        self.move()
        self.arrow_off_screen()

