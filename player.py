import pygame
from pygame.sprite import Sprite
from settings import Settings

class Player(Sprite):
    def __init__(self, number, image):
        super().__init__()
        self.number = number
        self.image = image
        self.rect = self.image.get_rect()
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.player_speed = 2

        self.moving_right = False
        self.moving_left = False

        self.jumping_frame = 0
        self.jump_count = 0
        self.gravity_counter = 0

    def update(self):
        if self.moving_right and self.rect.right < 1200:
            self.x += self.player_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.player_speed

        if self.jumping_frame > 0 and self.jump_count < 3:
            self.y -= 1
            self.jumping_frame -=1
        elif self.y < 539:
            self.gravity_counter +=1
            self.y += 0.2 * self.gravity_counter
        if self.y > 538:
            self.jump_count = 0
            self.gravity_counter = 0

        self.rect.x = self.x
        self.rect.y = self.y

















