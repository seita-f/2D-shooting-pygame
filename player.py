import pygame
from settings import *


class Player(pygame.sprite.Sprite):

    def __init__(self, groups, x, y):
        super().__init__(groups)

        # Image
        self.image = pygame.Surface((50, 50))
        # Debug
        # self.image.fill(RED)

        # Player image
        self.image_list = []
        for i in range(2):
            image = pygame.image.load(f'assets/img/player{i}.png')
            self.image_list.append(image)

        self.index = 0  # 0-Right, 1-Left
        self.pre_image = self.image_list[self.index]
        self.image = pygame.transform.scale(self.pre_image, (50, 50))
        self.rect = self.image.get_rect(center = (x, y))

        # Move
        self.direction = pygame.math.Vector2()
        self.speed = 5

    def input(self):
        key = pygame.key.get_pressed()

        # y-axis move
        if key[pygame.K_UP]:
            self.direction.y = -1
        elif key[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        # x-axis move
        if key[pygame.K_LEFT]:
            self.direction.x = -1
            self.index = 1
        elif key[pygame.K_RIGHT]:
            self.direction.x = 1
            self.index = 0
        else:
            self.direction.x = 0
            self.index = 0

    def move(self):

        # Diagonal move won't be faster (not x speed + y speed)
        if self.direction.magnitude() != 0:
            self.direction.normalize()

        self.rect.x += self.direction.x * self.speed
        self.check_off_screen('horizontal')
        self.rect.y += self.direction.y * self.speed
        self.check_off_screen('vertical')

    # Set the border for player (only move in screen)
    def check_off_screen(self, direction):
        if direction == 'horizontal':
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > screen_width:
                self.rect.right = screen_width

        if direction == 'vertical':
            if self.rect.top < 0:
                self.rect.top = 0
            if self.rect.bottom > screen_height:
                self.rect.bottom = screen_height

    def update_image(self):
        self.pre_image = self.image_list[self.index]
        self.image = pygame.transform.scale(self.pre_image, (50, 50))

    def update(self):
        self.input()
        self.move()
        self.update_image()
        # Debug
        # print(self.direction)
