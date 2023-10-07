import pygame
from settings import *


class Damage(pygame.sprite.Sprite):
    def __init__(self, groups, x, y):
        super().__init__(groups)
        # Image
        self.image_list = []

        for i in range(3):
            image = pygame.image.load(f"assets/img/damage{i}.png")
            self.image_list.append(image)

        self.index = 0
        self.pre_image = self.image_list[self.index]
        self.image = pygame.transform.scale(self.pre_image, (50, 50))
        self.rect = self.image.get_rect(center = (x, y))

    def animation(self):

        if self.alive:
            self.index += 0.2

            if self.index < len(self.image_list):
                self.pre_image = self.image_list[int(self.index)]
                self.image = pygame.transform.scale(self.pre_image, (50, 50))
            else:
                self.kill()
        else:
            self.image.set_alpha(0)   # Hide monster during damage animation

    def update(self):
        self.animation()
