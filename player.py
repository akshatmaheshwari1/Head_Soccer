import pygame
from pygame.sprite import Sprite
from settings import Settings

class Player(Sprite):
    def __init__(self, number, image): #characteristic for player number and player image
        super().__init__()
        self.number = number
        self.image = image
        self.rect = self.image.get_rect()
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.player_speed = 5

        self.moving_right = False
        self.moving_left = False

        self.jumping_frame = 0
        self.jump_count = 0
        self.gravity_counter = 0

    def update(self):
        if self.moving_right and self.rect.right < 1200-64: #moving right
            self.x += self.player_speed

        if self.moving_left and self.rect.left > 64: #moving left
            self.x -= self.player_speed

        if self.jumping_frame > 0 and self.jump_count < 3: #only lets you jump twice
            self.y -= 3
            self.jumping_frame -=1
        elif self.y < 600 - self.image.get_height(): #gravity acts as a factor that makes the player fall back down faster and faster
            self.gravity_counter +=1
            self.y += 1.08 ** self.gravity_counter
        if self.y > 599 - self.image.get_height(): #once it reaches the bottom, all those values reset to 0
            self.jump_count = 0
            self.gravity_counter = 0
            self.y = 600 - self.image.get_height()

        self.rect.x = self.x
        self.rect.y = self.y



















