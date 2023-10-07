import pygame
from settings import *
from monster import Monster
from arrow import Arrow


class Player(pygame.sprite.Sprite):

    def __init__(self, groups, x, y, monster_group):
        super().__init__(groups)

        # Game screen
        self.screen = pygame.display.get_surface()

        # Enemy group
        self.monster_group = monster_group

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

        # Arrow group
        self.arrow_group = pygame.sprite.Group()

        # default arrow
        self.shoot = False
        self.timer = 0
        self.health = 1
        self.alive = True

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

        # Z key (arrow)
        if key[pygame.K_z] and self.shoot == False:
            arrow = Arrow(self.arrow_group, self.rect.centerx, self.rect.top)
            self.shoot = True

    def cooldown_arrow(self):
        if self.shoot:
            self.timer += 1
        if self.timer > 10:
            self.shoot = False
            self.timer = 0

    def collision_monster(self):
        for monster in self.monster_group:
            if self.rect.colliderect(monster.rect):
                self.health -= 1

        if self.health <= 0:
            self.alive = False

    def check_death(self):
        if self.alive == False:
            self.kill()

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

        # Draw group and update
        self.arrow_group.draw(self.screen)
        self.arrow_group.update()
        self.cooldown_arrow()

        self.collision_monster()
        self.check_death()

