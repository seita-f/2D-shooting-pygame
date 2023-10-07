import pygame
from settings import *
from arrow import Arrow
import random

class Monster(pygame.sprite.Sprite):
    def __init__(self, groups, x, y, arrow_group):
        super().__init__(groups)

        # Group
        self.arrow_group = arrow_group

        # Image
        self.image = pygame.Surface((50, 50))
        # Debug
        # self.image.fill(BLUE)
        self.image_list = []
        for i in range(2):
            image = pygame.image.load(f'assets/img/monster{i}.png')
            self.image_list.append(image)

        self.index = 0  # 0-Right, 1-Left
        self.pre_image = self.image_list[self.index]
        self.image = pygame.transform.scale(self.pre_image, (50, 50))
        self.rect = self.image.get_rect(center=(x, y))

        # Move
        # just y direction
        # self.direction = pygame.math.Vector2((0, 1))

        # x and y direction
        move_list = [-1, 1]
        self.direction = pygame.math.Vector2((random.choice(move_list), 1))
        self.speed = 1
        self.timer = 0

        # HP
        self.health = 3
        self.alive = True

    def update_image(self):
        self.pre_image = self.image_list[self.index]
        self.image = pygame.transform.scale(self.pre_image, (50, 50))

    def move(self):
        # Moving zigzag
        self.timer += 1
        if self.timer > 80:
            self.direction.x *= -1
            self.timer = 0

        self.rect.y += self.direction.y * self.speed
        self.rect.x += self.direction.x * self.speed

    def check_off_screen(self, direction):
        # remove monster who goes out of the screen
        if self.rect.top > screen_height:
            self.kill()

    def collision_arrow(self):
        for arrow in self.arrow_group:
            if self.rect.colliderect(arrow.rect):
                arrow.kill()
                self.health -= 1

        if self.health <= 0:
            self.alive = False

    def check_death(self):
        if self.alive == False:
            self.kill()

    def update(self):
        self.move()
        self.update_image()
        self.collision_arrow()
        self.check_death()
